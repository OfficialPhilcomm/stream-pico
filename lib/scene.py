import shared
from keypadkey import KeypadKey

class Scene:
  def is_pressed(self):
    return self.scene_button.is_pressed()

  def active(self):
    self.scene_button.press(shared.keyboard)
    self.scene_button.blink_for(2)
    self.scene_button.active()

  def inactive(self):
    self.scene_button.inactive()
