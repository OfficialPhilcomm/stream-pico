
import time
from keypadkey import KeypadKey
import shared
import asyncio

class Scene:
  def __init__(self, id, color, keys):
    self.scene_button = KeypadKey(4 + id, color)
    self.scene_button.inactive()

    self.keys = keys

    self.actions = [None] * 8

  def add_action(self, id, action):
    self.actions[id] = action

  def active(self):
    for action in self.actions:
      if action:
        action.active()

    shared.keyboard.send(*self.keys)
    for x in range(2):
      self.scene_button.active()
      time.sleep(0.5)
      self.scene_button.inactive()
      time.sleep(0.5)
    self.scene_button.active()

  def inactive(self):
    for action in self.actions:
      if action:
        action.inactive()

    self.scene_button.inactive()

  def is_pressed(self):
    return self.scene_button.is_pressed()

  async def check_for_action_press(self):
    for i in range(8):
      if self.actions[i] and self.actions[i].is_pressed():
        asyncio.create_task(self.actions[i].trigger())
