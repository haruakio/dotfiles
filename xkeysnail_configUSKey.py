# -*- coding: utf-8 -*-

# setup follow https://qiita.com/samurai20000@github/items/2e1d779e806a7e8543d6
# sudo groupadd uinput
# sudo usermod -aG input,uinput sekitan
# echo "" /etc/udev/rules.d/40-udev-xkeysnail.rules
# KERNEL=="uinput", GROUP="uinput"
# copy xkeysnail.service to /home/sekitan/.config/systemd/user/xkeysnail.service
# systemctl --user enable xkeysnail
# systemctl --user start xkeysnail
# systemctl --user status xkeysnail
# if it's not working check
# journalctl | grep xkey
import re
from xkeysnail.transform import *

define_multipurpose_modmap({
    Key.CAPSLOCK: [Key.ESC, Key.RIGHT_CTRL],
    Key.SEMICOLON: [Key.SEMICOLON, Key.RIGHT_META],
    # CapsLockではなくCtrlの場合
    # Key.LEFT_CTRL: [Key.ESC, Key.LEFT_CTRL],

    Key.LEFT_ALT: [Key.MUHENKAN, Key.LEFT_CTRL],
    Key.RIGHT_ALT: [Key.HENKAN, Key.RIGHT_ALT]
})

define_keymap(None, {
    K("RWin-COMMA"): K("page_up"),
    K("RWin-Shift-COMMA"): K("Shift-page_up"),
    K("RWin-M"): K("page_down"),
    K("RWin-Shift-M"): K("Shift-page_down"),
    K("RWin-U"): K("home"),
    K("RWin-Shift-U"): K("Shift-home"),
    K("RWin-O"): K("end"),
    K("RWin-Shift-O"): K("Shift-end"),
    K("RWin-I"): K("up"),
    K("RWin-Shift-I"): K("Shift-up"),
    K("RWin-J"): K("left"),
    K("RWin-Shift-J"): K("Shift-left"),
    K("RWin-K"): K("down"),
    K("RWin-Shift-K"): K("Shift-down"),
    K("RWin-L"): K("right"),
    K("RWin-Shift-L"): K("Shift-right"),
    K("RWin-D"): K("KPLEFTPAREN"),
    K("RWin-F"): K("KPRIGHTPAREN"),
    K("RWin-A"): K("Shift-LEFT_BRACE"),
    K("RWin-Shift-A"): K("LEFT_BRACE"),
    K("RWin-S"): K("Shift-RIGHT_BRACE"),
    K("RWin-Shift-S"): K("RIGHT_BRACE"),

    # Emacs style Cursor. Use Capslock as Right-Alt
    K("RC-b"): with_mark(K("left")),
    K("RC-Shift-b"): with_mark(K("Shift-left")),
    K("RC-f"): with_mark(K("right")),
    K("RC-Shift-f"): with_mark(K("Shift-right")), 
    K("RC-p"): with_mark(K("up")),
    K("RC-Shift-p"): with_mark(K("Shift-up")),
    K("RC-n"): with_mark(K("down")),
    K("RC-Shift-n"): with_mark(K("Shift-down")),
    K("RC-h"): with_mark(K("backspace")),
    K("RC-Shift-h"): with_mark(K("Shift-backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("C-left")),
    K("M-Shift-b"): with_mark(K("C-Shift-left")),
    K("M-f"): with_mark(K("C-right")),
    K("M-Shift-f"): with_mark(K("C-Shift-right")),
    # Beginning/End of line
    K("RC-a"): with_mark(K("home")),
    K("RC-Shift-a"): with_mark(K("Shift-home")),
    K("RC-e"): with_mark(K("end")),
    K("RC-Shift-e"): with_mark(K("Shift-end")),
    # Page up/down
    K("RC-j"): K("enter"),
    # Ctrl-c as normal kill command
    # K("RC-c"): K("C-c"),
    # Ctrl-u as normal clear command
    # K("RC-u"): K("C-u"),
    # Delete
    K("RC-d"): [K("delete"), set_mark(False)],
    # Kill line
    K("RC-k"): [K("Shift-end"), K("C-x"), set_mark(False)]
}, "cursor keys")
