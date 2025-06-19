# PROGIDY_CS_04: Basic Keylogger

## Description
A basic keylogger program that records and logs keystrokes. The program logs every key pressed and saves them to a file inside the `logs` directory.

> **Note:** This project is for educational purposes only. **Ethical considerations and explicit permissions are crucial. Do NOT run this on any computer without legal and authorized consent.**

---

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/Tanvi228-yadav/PRODIGY_CS_04.git
   cd PRODIGY_CS_04
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the keylogger:**
   ```
   python keylogger.py
   ```
2. **To stop logging:**  
   Press the `ESC` key.

3. **View the logs:**  
   Check the `logs/` folder for files named like `log_YYYYMMDD_HHMMSS.txt`.

---

## Example Output

```
2025-06-19 12:10:01,123: Key pressed: a
2025-06-19 12:10:02,456: Key pressed: b
2025-06-19 12:10:03,789: Special key pressed: Key.space
```

---

## Requirements

- Python 3.x
- `pynput` package

---

## Disclaimer

- This project is for **educational purposes only**.
- The use of keyloggers is regulated by law in many jurisdictions.
- **Do not use, share, or run this program without explicit legal permission.**
