import time
import usb_hid
from rgbkeypad import RGBKeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from random import randint
from keypadkey import KeypadKey
from recording_bar import RecordingBar
from intro_scene import IntroScene
from zoom_scene import ZoomScene
import shared

keypad = RGBKeypad()
keyboard = Keyboard(usb_hid.devices)
shared.set_keypad(keypad)
shared.set_keyboard(keyboard)

recording_bar = RecordingBar(0)

scene_intro = IntroScene(0)
scene_zoom = ZoomScene(1)

scenes = [None] * 4
scenes[0] = scene_intro
scenes[1] = scene_zoom

active_scene = None

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
