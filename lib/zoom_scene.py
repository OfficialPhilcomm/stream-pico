import shared
from scene import Scene
from keypadkey import KeypadKey
from adafruit_hid.keycode import Keycode

class ZoomScene(Scene):
  def __init__(self, id):
    self.id = id

    self.scene_button = KeypadKey(shared.keypad.keys[4 + id], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_FOUR), (2, 149, 247))
    self.scene_button.inactive()

  def trigger_action(self, id):
    pass

  def active(self):
    Scene.active(self)

  def inactive(self):
    Scene.inactive(self)
