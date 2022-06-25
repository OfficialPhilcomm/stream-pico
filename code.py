import time
import usb_hid
from rgbkeypad import RGBKeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import shared
from recording_bar import RecordingBar
from scene import Scene
from button import Button
import scene_builder


keypad = RGBKeypad()
keyboard = Keyboard(usb_hid.devices)
shared.set_keypad(keypad)
shared.set_keyboard(keyboard)

recording_bar = RecordingBar(0)

scenes = [None] * 4
scene_builder.build(scenes)

active_scene = None

while True:
  for i in range(4):
    if scenes[i] and scenes[i].is_pressed() and scenes[i] != active_scene:
      for scene in scenes:
        if scene:
          scene.inactive()
      scenes[i].active()
      active_scene = scenes[i]

  if active_scene:
    active_scene.check_for_action_press()

  recording_bar.check_for_pressed()

  time.sleep(0.1)
