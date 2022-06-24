import shared
from keypadkey import KeypadKey

class Scene:
  def __init__(self, id, keys, color):
    self.id = id
    self.actions = [None] * 8

    self.scene_button = KeypadKey(shared.keypad.keys[4 + id], keys, color)
    self.scene_button.inactive()

  def add_action(self, id, keys, color):
    action = KeypadKey(shared.keypad.keys[8 + id], keys, color)

    self.actions[id] = action

  def is_pressed(self):
    return self.scene_button.is_pressed()

  def active(self):
    for action in self.actions:
      if action:
        action.inactive()
    self.scene_button.press(shared.keyboard)
    self.scene_button.blink_for(2)
    self.scene_button.active()

  def inactive(self):
    for action in self.actions:
      if action:
        action.off()
    self.scene_button.inactive()

  def trigger_action(self, id):
    if self.actions[id]:
      self.actions[id].press(shared.keyboard)
      self.actions[id].blink_for(2)
