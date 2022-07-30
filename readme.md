# StreamPICO

The StreamPICO is using a Raspberry Pi Pico and the Pimoroni RGB Keypad to create a StreamDeck like device.

- [StreamPICO](#streampico)
  - [Installation](#installation)
    - [Install Circuitpython](#install-circuitpython)
    - [Install Martin O'Hanlon's RGB Keypad Wrapper](#install-martin-ohanlons-rgb-keypad-wrapper)
    - [Install StreamPICO code](#install-streampico-code)
  - [How it works](#how-it-works)
  - [Create config](#create-config)

## Installation

### Install Circuitpython
First you need to install CircuitPython. You can download it here: https://circuitpython.org/downloads. After downloading the `.uf2` file, you can install it like MicroPython.

### Install Martin O'Hanlon's RGB Keypad Wrapper
Instructions for this can be found here: https://github.com/martinohanlon/pico-rgbkeypad.

A shorter version:
Either download https://github.com/martinohanlon/pico-rgbkeypad/blob/main/rgbkeypad/rgbkeypad.py and put it into the `lib/` file on the pico, or put both files in https://github.com/martinohanlon/pico-rgbkeypad/tree/main/rgbkeypad into a subfolder of `lib/`.

### Install StreamPICO code
Now everything that is left is to copy everything from the `src/` folder onto the root of the Pico, and you are done.

## How it works
The StreamPICO registers as a Keyboard to the computer. In your streaming software, you can then setup shortcuts that are sent by the device.

The 4 upper buttons is what the StreamPICO calls a Recording Bar. It allows you to easily see if you are streaming/recording.
When pressing on the red left button, it counts down from 3 to 0. You can see this by the bar "filling"  with green lights. As soon as the top right button is red, it sends the keyboard shortcut `Left Control + F11`. When pressing that red button, it sends `Left Control + F12`, which resets the bar.

The second row from the top is the scenes bar. The StreamPICO allows you to have 4 scenes at once. When pressing one of these buttons, it sends the configured shortcut. It also switches out the scene specific actions, more on that in the next section.
After pressing it, there is a 2 second cooldown until anything else can be pressed.
You can identify the active scene by it's button being the brightest.

The bottom half of the keypad are the scene specific actions. So far, two action types are available:
- Button, well, its a button that when pressed, sends a specific shortcut
- Toggle, which can have two states, sending two different shortcuts depending on the state. Can also optionally remember the state between scene switches

## Create config
To make it as easy as possible to create a new config, I created a small webapp that allows you to drag and drop elements and import an existing config. It then gives you the json which can then be dropped as `setup.json` onto the Pico's root.

The webapp can be found here: https://philcomm.dev/stream_pico
