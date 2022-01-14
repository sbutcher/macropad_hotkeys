# MACROPAD Hotkeys example: Git commands

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Git', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'status', 'git status\n'),
        (0x004000, 'commit', 'git commit -a\n'),
        (0x400000, 'log', 'git log\n'),
        # 2nd row ----------
        (0x202000, 'master', 'git checkout master\n'),
        (0x202000, 'uat', 'git checkout uat\n'),
        (0x400000, 'pull', 'git pull\n'),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'co branch', 'git checkout -b '),
        (0x000040, ' ', ' '),
        (0x000040, ' ', ' '),
        # 4th row ----------
        (0x101010, ' ', ' '),     #
        (0x101010, ' ', ' '),     #
        (0x101010, 'q', 'q'),     # q to quit git log
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'd']) # Close window/tab
    ]
}
