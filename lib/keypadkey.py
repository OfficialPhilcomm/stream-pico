import time
from adafruit_hid.keycode import Keycode

class KeypadKey:
    def __init__(self, keypad, keys, color):
        self.keypad = keypad
        self.keys = keys
        self.off()
        self.color(color)

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

    def off(self):
        self.brightness(0)

    def handle_press(self, keyboard):
        self.press(keyboard)
        while self.is_pressed():
            time.sleep(0.01)
