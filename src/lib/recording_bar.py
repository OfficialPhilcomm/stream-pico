import time
import shared
from keypadkey import KeypadKey
from adafruit_hid.keycode import Keycode

color_red = (252, 36, 3)
color_green = (3, 252, 15)

class RecordingBar:
  def __init__(self, row):
    self.row = row

    self.key_start = KeypadKey((row * 4), color_red)
    self.key_start.inactive()
    self.key_countdown_two = KeypadKey((row * 4) + 1, color_green)
    self.key_countdown_one = KeypadKey((row * 4) + 2, color_green)
    self.key_recording = KeypadKey((row * 4) + 3, color_red)

    self.streaming = False

  def check_for_pressed(self):
    if not self.streaming and self.key_start.is_pressed():
      self.streaming = True

      self.key_start.color(color_green)
      self.key_start.active()

      time.sleep(1)
      self.key_countdown_two.active()
      time.sleep(1)
      self.key_countdown_one.active()
      time.sleep(1)

      self.key_recording.active()

      self.key_start.inactive()
      self.key_countdown_two.inactive()
      self.key_countdown_one.inactive()

      shared.keyboard.send(Keycode.LEFT_CONTROL, Keycode.F11)
    elif self.streaming and self.key_recording.is_pressed():
      self.key_start.color(color_red)
      self.key_start.inactive()

      self.key_countdown_two.off()
      self.key_countdown_one.off()
      self.key_recording.off()

      self.streaming = False

      shared.keyboard.send(Keycode.LEFT_CONTROL, Keycode.F12)
