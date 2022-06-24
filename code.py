import time
import usb_hid
from rgbkeypad import RGBKeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from random import randint
from keypadkey import KeypadKey

keypad = RGBKeypad()
keyboard = Keyboard(usb_hid.devices)

color_red = (252, 36, 3)
# color_green = (3, 252, 136)
color_green = (3, 252, 15)

key0 = KeypadKey(keypad.keys[0], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_ONE), color_red)
key0.inactive()
key3 = KeypadKey(keypad.keys[3], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_TWO), color_red)

key4 = KeypadKey(keypad.keys[4], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_THREE), (247, 198, 2))
key4.inactive()
key5 = KeypadKey(keypad.keys[5], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_FOUR), (2, 149, 247))
key5.inactive()

streaming = False

while True:
  if not streaming and key0.is_pressed():
    streaming = True

    key0.color(color_green)
    key0.active()

    key3.inactive()

    key0.handle_press(keyboard)
  elif streaming and key3.is_pressed():
    key0.color(color_red)
    key0.inactive()

    key3.off()

    streaming = False

    key3.handle_press(keyboard)

  if key4.is_pressed():
    key5.inactive()

    key4.active()
    key4.handle_press(keyboard)
  elif key5.is_pressed():
    key4.inactive()

    key5.active()
    key5.handle_press(keyboard)
  time.sleep(0.01)
