import json
from adafruit_hid.keycode import Keycode
from scene import Scene
from button import Button
from toggle import Toggle

def build(scenes_array):
  obj = json.loads(open("setup.json").read())

  for scene_obj in obj["scenes"]:
    scene = Scene(scene_obj["id"], resolve_color(scene_obj["color"]), list(map(resolve_key, scene_obj["keys"])))

    if "actions" in scene_obj.keys():
      for action_obj in scene_obj["actions"]:
        action = None
        if action_obj["type"] == "button":
          action = Button(action_obj["id"], resolve_color(action_obj["color"]), list(map(resolve_key, action_obj["keys"])))
        elif action_obj["type"] == "toggle":
          action = Toggle(
            action_obj["id"],
            resolve_color(action_obj["color"]),
            list(map(resolve_key, action_obj["keys_on"])),
            list(map(resolve_key, action_obj["keys_off"]))
          )

        if action:
          scene.add_action(action_obj["id"], action)

    scenes_array[scene_obj["id"]] = scene

def resolve_color(color_array):
  return (color_array[0], color_array[1], color_array[2])

def resolve_key(key_string):
  keys = {
    "LEFT_CONTROL": Keycode.LEFT_CONTROL,
    "ALT": Keycode.ALT,
    "KEYPAD_ZERO": Keycode.KEYPAD_ZERO,
    "KEYPAD_ONE": Keycode.KEYPAD_ONE,
    "KEYPAD_TWO": Keycode.KEYPAD_TWO,
    "KEYPAD_THREE": Keycode.KEYPAD_THREE,
    "KEYPAD_FOUR": Keycode.KEYPAD_FOUR,
    "KEYPAD_FIVE": Keycode.KEYPAD_FIVE,
    "KEYPAD_SIX": Keycode.KEYPAD_SIX,
    "KEYPAD_SEVEN": Keycode.KEYPAD_SEVEN,
    "KEYPAD_EIGHT": Keycode.KEYPAD_EIGHT,
    "KEYPAD_NINE": Keycode.KEYPAD_NINE
  }

  return keys[key_string]
