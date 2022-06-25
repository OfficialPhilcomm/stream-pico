import time
import shared
from scene import Scene
from keypadkey import KeypadKey
from adafruit_hid.keycode import Keycode

class IntroScene(Scene):
  def __init__(self, id):
    self.id = id

    self.scene_button = KeypadKey(shared.keypad.keys[4 + id], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_THREE), (247, 198, 2))
    self.scene_button.inactive()

    self.action_reset_music = KeypadKey(shared.keypad.keys[8], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_SEVEN), (240, 5, 228))
    self.action_reset_countdown = KeypadKey(shared.keypad.keys[9], (Keycode.LEFT_CONTROL, Keycode.KEYPAD_EIGHT), (255, 234, 0))

    self.action_toggle_logo_and_countdown = KeypadKey(shared.keypad.keys[11], None, (64, 255, 0))
    self.logo_and_countdown_visible = True

    self.action_play_video = KeypadKey(shared.keypad.keys[15], (Keycode.ALT, Keycode.KEYPAD_ONE), (2, 149, 247))

  def trigger_action(self, id):
    if id == 0:
      self.action_reset_music.press(shared.keyboard)
      self.action_reset_music.blink_for(1)
    elif id == 1:
      self.action_reset_countdown.press(shared.keyboard)
      self.action_reset_countdown.blink_for(1)
    elif id == 3:
      if self.logo_and_countdown_visible:
        self.logo_and_countdown_visible = False
        shared.keyboard.send(Keycode.LEFT_CONTROL, Keycode.KEYPAD_NINE)
        self.action_toggle_logo_and_countdown.inactive()
        time.sleep(0.5)
        self.action_toggle_logo_and_countdown.active()
        time.sleep(0.5)
        self.action_toggle_logo_and_countdown.inactive()
      else:
        self.logo_and_countdown_visible = True
        shared.keyboard.send(Keycode.LEFT_CONTROL, Keycode.KEYPAD_ZERO)
        self.action_toggle_logo_and_countdown.active()
        time.sleep(0.5)
        self.action_toggle_logo_and_countdown.inactive()
        time.sleep(0.5)
        self.action_toggle_logo_and_countdown.active()
    elif id == 7:
      self.action_play_video.press(shared.keyboard)
      self.action_play_video.blink_for(1)

  def active(self):
    self.logo_and_countdown_visible = True

    self.action_reset_music.inactive()
    self.action_reset_countdown.inactive()
    self.action_toggle_logo_and_countdown.active()
    self.action_play_video.inactive()

    Scene.active(self)

  def inactive(self):
    self.action_reset_music.off()
    self.action_reset_countdown.off()
    self.action_toggle_logo_and_countdown.off()
    self.action_play_video.off()

    Scene.inactive(self)
