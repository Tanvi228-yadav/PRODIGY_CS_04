# PROGIDY_CS_04: Basic Keylogger

## Description
This is a basic keylogger program created for educational purposes as part of an internship. It records keyboard keystrokes and saves them to a file in the `logs` directory.

**Note:**  
> Ethical considerations and explicit permission are absolutely required before running this program. Do NOT use it on any system without consent.

## Usage

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run the keylogger:
    ```
    python keylogger.py
    ```
3. Press `ESC` to stop logging.
4. Check the `logs/` folder for the output `.txt` file.

## Example Output

```
2025-06-19 12:10:01,123: Key pressed: a
2025-06-19 12:10:02,456: Key pressed: b
2025-06-19 12:10:03,789: Special key pressed: Key.space
```

## Requirements

- Python 3.x
- `pynput` package

## Disclaimer

This project is for educational use **only**.  
The use of keyloggers is strictly regulated by law.  
**Do not run or share this program without explicit legal permission.**