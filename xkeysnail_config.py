# -*- coding: utf-8 -*-

# setup follow https://qiita.com/samurai20000@github/items/2e1d779e806a7e8543d6
# sudo groupadd uinput
# sudo usermod -aG input,uinput sekitan
# create /etc/udev/rules.d/40-udev-xkeysnail.rules
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
    Key.CAPSLOCK: [Key.ESC, Key.RIGHT_ALT],
    # CapsLockではなくCtrlの場合
    # Key.LEFT_CTRL: [Key.ESC, Key.LEFT_CTRL],

    Key.MUHENKAN: [Key.MUHENKAN, Key.LEFT_CTRL],
    Key.HENKAN: [Key.HENKAN, Key.RIGHT_CTRL]
})

define_keymap(None, {
    K("RC-U"): K("page_up"),
    K("RC-O"): K("page_down"),
    K("RC-I"): K("up"),
    K("RC-J"): K("left"),
    K("RC-K"): K("down"),
    K("RC-L"): K("right"),

    # Emacs style Cursor. Use Capslock as Right-Alt
    K("RM-b"): with_mark(K("left")),
    K("RM-f"): with_mark(K("right")),
    K("RM-p"): with_mark(K("up")),
    K("RM-n"): with_mark(K("down")),
    K("RM-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("C-left")),
    K("M-f"): with_mark(K("C-right")),
    # Beginning/End of line
    K("RM-a"): with_mark(K("home")),
    K("RM-e"): with_mark(K("end")),
    # Page up/down
    K("RM-j"): K("enter"),
    # Ctrl-c as normal kill command
    K("RM-c"): K("C-c"),
    # Ctrl-u as normal clear command
    K("RM-u"): K("C-u"),
    # Delete
    K("RM-d"): [K("delete"), set_mark(False)],
    # Kill line
    K("RM-k"): [K("Shift-end"), K("C-x"), set_mark(False)]
})

define_keymap(None, {
    ## 日本語キーボード上で英語配列を使う設定
    K(      "GRAVE"): K("Shift-LEFT_BRACE"), # [半角/全角]
    K("Shift-GRAVE"): K("Shift-EQUAL"),
    K("Shift-KEY_2"): K("LEFT_BRACE"),
    K("Shift-KEY_6"): K("EQUAL"),
    K("Shift-KEY_7"): K("Shift-KEY_6"),
    K("Shift-KEY_8"): K("Shift-APOSTROPHE"),
    K("Shift-KEY_9"): K("Shift-KEY_8"),
    K("Shift-KEY_0"): K("Shift-KEY_9"),
    ## [Minus]は共通
    K("Shift-MINUS"):       K("Shift-RO"),
    K(      "EQUAL"):       K("Shift-MINUS"),
    K("Shift-EQUAL"):       K("Shift-SEMICOLON"),
    K(      "YEN"):         K("BACKSPACE"),
    K(      "LEFT_BRACE"):  K("RIGHT_BRACE"),
    K("Shift-LEFT_BRACE"):  K("Shift-RIGHT_BRACE"),
    K(      "RIGHT_BRACE"): K("BACKSLASH"),
    K("Shift-RIGHT_BRACE"): K("Shift-BACKSLASH"),
    ## [Semicolon]は共通
    K("Shift-SEMICOLON"):   K("APOSTROPHE"),
    K(      "APOSTROPHE"):  K("Shift-KEY_7"),
    K("Shift-APOSTROPHE"):  K("Shift-KEY_2"),
    K(      "BACKSLASH"):   K("YEN"),
    K("Shift-BACKSLASH"):   K("Shift-YEN"),
}, "Global")