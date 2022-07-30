import time
from keypadkey import KeypadKey
import shared

class Toggle:
  def __init__(self, id, color, keys_on, keys_off, remember_state):
    self.toggle = KeypadKey(8 + id, color)
    self.color = color
    self.keys_on = keys_on
    self.keys_off = keys_off
    self.remember_state = remember_state
    self.is_on = True

  def trigger(self):
    if self.is_on:
      shared.keyboard.send(*self.keys_off)
      self.toggle.inactive()
      time.sleep(1)
      self.is_on = False
    else:
      shared.keyboard.send(*self.keys_on)
      self.toggle.active()
      time.sleep(1)
      self.is_on = True

  def active(self):
    self.toggle.set_color()

    if not self.remember_state:
      self.is_on = True
    if self.is_on:
      self.toggle.active()
    else:
      self.toggle.inactive()

  def inactive(self):
    self.toggle.off()

  def is_pressed(self):
    return self.toggle.is_pressed()
