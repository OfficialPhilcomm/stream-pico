import time
import usb_hid
from rgbkeypad import RGBKeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from random import randint
from keypadkey import KeypadKey

keypad = RGBKeypad()
keyboard = Keyboard(usb_hid.devices)

key0 = KeypadKey(0, 0, (Keycode.LEFT_CONTROL, Keycode.KEYPAD_ONE), keypad.keys[0], (247, 198, 2))
key1 = KeypadKey(0, 0, (Keycode.LEFT_CONTROL, Keycode.KEYPAD_TWO), keypad.keys[1], (2, 149, 247))

while True:
    if key0.is_pressed():
        key1.inactive()

        key0.handle_press(keyboard)
    if key1.is_pressed():
        key0.inactive()

        key1.handle_press(keyboard)
    time.sleep(0.01)
