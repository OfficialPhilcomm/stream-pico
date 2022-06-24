import time
from adafruit_hid.keycode import Keycode

class KeypadKey:
    def __init__(self, x, y, keys, keypad, color):
        self.x = x
        self.y = y
        self.keys = keys
        self.keypad = keypad
        self.keypad.color = color
        self.inactive()
    
    def press(self, keyboard):
        keyboard.send(*self.keys)
    
    def color(self, color):
        self.keypad.color = color
    
    def brightness(self, brightness):
        self.keypad.brightness = brightness
    
    def is_pressed(self):
        return self.keypad.is_pressed()

    def active(self):
        self.brightness(1)

    def inactive(self):
        self.brightness(0.1)

    def handle_press(self, keyboard):
        self.active()
        self.press(keyboard)
        while self.is_pressed():
            time.sleep(0.01)
