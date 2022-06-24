import time
import usb_hid
from rgbkeypad import RGBKeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from random import randint
from keypadkey import KeypadKey
from recording_bar import RecordingBar
from scene import Scene
import shared

keypad = RGBKeypad()
keyboard = Keyboard(usb_hid.devices)
shared.set_keypad(keypad)
shared.set_keyboard(keyboard)

recording_bar = RecordingBar(0)

scene_intro = Scene(0, (247, 198, 2))
scene_intro.add_action(0, (Keycode.LEFT_CONTROL, Keycode.KEYPAD_SEVEN), (240, 5, 228)),

scene_secondary = Scene(1, (2, 149, 247))

scenes = [None] * 4

scenes[0] = scene_intro
scenes[1] = scene_secondary

active_scene = None

streaming = False

while True:
  for i in range(4):
    if scenes[i] and scenes[i] != active_scene and scenes[i].is_pressed():
      for scene in scenes:
        if scene:
          scene.inactive()
      scenes[i].active()
      active_scene = scenes[i]

  for i in range(8):
    if keypad.keys[8 + i].is_pressed():
      active_scene.trigger_action(i)

  recording_bar.check_for_pressed()

  time.sleep(0.1)
