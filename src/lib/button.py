import asyncio
from keypadkey import KeypadKey
import shared

class Button:
  def __init__(self, id, color, keys):
    self.button = KeypadKey(8 + id, color)
    self.color = color
    self.keys = keys
    self.triggered = False

  async def trigger(self):
    self.triggered = True
    shared.keyboard.send(*self.keys)
    self.button.active()
    await asyncio.sleep(1)
    self.button.inactive()
    self.triggered = False

  def active(self):
    self.button.set_color()
    self.button.inactive()

  def inactive(self):
    self.button.off()

  def is_pressed(self):
    return not self.triggered and self.button.is_pressed()
