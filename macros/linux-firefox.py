# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Linux Firefox', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.CONTROL, '[']),
        (0x004000, 'Fwd >', [Keycode.CONTROL, ']']),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Refresh', [Keycode.CONTROL, 'r']),
        (0x000040, 'tab X', [Keycode.CONTROL, 'w']),
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'p']),
        # 4th row ----------
        (0x101010, 'Zoom -', [Keycode.CONTROL, '-']), 
        (0x000040, 'Dloads', [Keycode.CONTROL, Keycode.SHIFT, 'y']),     # ctrl-shift-y for downloads
        (0x101010, 'Zoom +', [Keycode.CONTROL, '=']), 
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
