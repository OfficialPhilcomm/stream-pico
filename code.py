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
color_green = (3, 252, 15)

key0 = KeypadKey(keypad.keys[0], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_ONE), color_red)
key0.inactive()
key1 = KeypadKey(keypad.keys[1], None, color_green)
key2 = KeypadKey(keypad.keys[2], None, color_green)

key3 = KeypadKey(keypad.keys[3], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_TWO), color_red)

key4 = KeypadKey(keypad.keys[4], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_THREE), (247, 198, 2))
key4.inactive()
key5 = KeypadKey(keypad.keys[5], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_FOUR), (2, 149, 247))
key5.inactive()

key8 = KeypadKey(keypad.keys[8], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_SEVEN), (240, 5, 228))

active_scene = 0

streaming = False

while True:
  if not streaming and key0.is_pressed():
    streaming = True

    key0.color(color_green)
    key0.active()

    time.sleep(1)
    key1.active()
    time.sleep(1)
    key2.active()
    time.sleep(1)

    key3.active()

    key0.handle_press(keyboard)
  elif streaming and key3.is_pressed():
    key0.color(color_red)
    key0.inactive()

    key1.off()
    key2.off()
    key3.off()

    streaming = False

    key3.handle_press(keyboard)

  if key4.is_pressed():
    key5.inactive()
    key8.active()

    key4.press(keyboard)
    key4.blink_for(2)
    key4.active()

    active_scene = 1
  elif key5.is_pressed():
    key4.inactive()
    key8.off()

    key5.press(keyboard)
    key5.blink_for(2)
    key5.active()

    active_scene = 2
  elif active_scene == 1 and key8.is_pressed():
    key8.press(keyboard)
    key8.inactive()
    time.sleep(0.5)
    key8.blink_for(2)
    key8.active()

  time.sleep(0.01)
