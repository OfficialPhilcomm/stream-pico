import shared
from scene import Scene
from keypadkey import KeypadKey
from adafruit_hid.keycode import Keycode

class IntroScene(Scene):
  def __init__(self, id):
    self.id = id

    self.scene_button = KeypadKey(shared.keypad.keys[4 + id], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_THREE), (247, 198, 2))
    self.scene_button.inactive()

    self.action0 = KeypadKey(shared.keypad.keys[8], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_SEVEN), (240, 5, 228))

  def trigger_action(self, id):
    if id == 0:
      self.action0.press(shared.keyboard)
      self.action0.blink_for(2)

  def active(self):
    self.action0.inactive()
    Scene.active(self)

  def inactive(self):
    self.action0.off()
    Scene.inactive(self)
