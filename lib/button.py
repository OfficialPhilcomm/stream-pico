import time
from keypadkey import KeypadKey
import shared

class Button:
  def __init__(self, id, color, keys):
    self.button = KeypadKey(8 + id, color)
    self.color = color
    self.keys = keys

  def trigger(self):
    shared.keyboard.send(*self.keys)
    self.button.active()
    time.sleep(1)
    self.button.inactive()

  def active(self):
    self.button.inactive()

  def inactive(self):
    self.button.off()

  def is_pressed(self):
    return self.button.is_pressed()
