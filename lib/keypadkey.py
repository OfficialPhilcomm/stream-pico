import shared

class KeypadKey:
  def __init__(self, id, color):
    self.key = shared.keypad.keys[id]
    self.off()
    self.color(color)

  def color(self, color):
    self.key.color = color

  def brightness(self, brightness):
    self.key.brightness = brightness

  def is_pressed(self):
    return self.key.is_pressed()

  def active(self):
    self.brightness(1)

  def inactive(self):
    self.brightness(0.1)

  def off(self):
    self.brightness(0)
