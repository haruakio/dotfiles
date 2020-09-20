# -*- mode: python; coding: utf-8-with-signature-dos -*-

import keyhac_keymap
from keyhac import *

def configure(keymap):

    
    # ChgKeyでCapslockを左Winにしている。それを存在しないキー235に割り当て
    keymap_global = keymap.defineWindowKeymap()
    keymap.replaceKey( "LWin", 235 )

    # Capslockのモディファイア
    keymap.defineModifier( 235, "User0" )
    keymap_global["O-235"] = "Esc"
    
    keymap_global[ "U0-J"] = "Enter"
    keymap_global[ "U0-N"] = "Down"
    keymap_global[ "U0-F"] = "Right"
    keymap_global[ "U0-E"] = "End"
    keymap_global[ "U0-A"] = "Home"
    keymap_global[ "U0-H"] = "Back"
    keymap_global[ "U0-D"] = "Delete"
    keymap_global[ "U0-U"] = "Ctrl-U"
    keymap_global[ "U0-Z"] = "Ctrl-Z"
    keymap_global[ "U0-C"] = "Ctrl-C"
    keymap_global[ "U0-X"] = "Ctrl-X"
    keymap_global[ "U0-V"] = "Ctrl-V"


    # セミコロンでカーソル移動
    keymap.defineModifier( "Semicolon", "User1" )
    keymap_global["O-Semicolon"] = "Semicolon"
    keymap_global["S-Semicolon"] = "S-Semicolon"

    keymap_global[ "U1-I" ] = "Up"
    keymap_global[ "U1-K" ] = "Down"
    keymap_global[ "U1-J" ] = "Left"
    keymap_global[ "U1-L" ] = "Right"
    keymap_global[ "U1-U" ] = "PageUp"
    keymap_global[ "U1-M" ] = "PageDown"
    keymap_global[ "U1-S-H" ] = "S-Home"
    keymap_global[ "U1-S-I" ] = "S-Up"
    keymap_global[ "U1-S-K" ] = "S-Down"
    keymap_global[ "U1-S-J" ] = "S-Left"
    keymap_global[ "U1-S-L" ] = "S-Right"
    keymap_global[ "U1-S-U" ] = "S-PageUp"
    keymap_global[ "U1-S-M" ] = "S-PageDown"
    keymap_global[ "U1-S-H" ] = "S-Home"
    # セミコロンでかっこ入力
    keymap_global[ "U1-A" ] = "S-OpenBracket"
    keymap_global[ "U1-S" ] = "S-CloseBracket"
    keymap_global[ "U1-D" ] = "S-9"
    keymap_global[ "U1-F" ] = "S-0"

    # 右Ctrlでよく使う記号入力
    keymap_global[ "LCtrl-J"] = "Minus"
    keymap_global[ "LCtrl-K"] = "Plus"
    keymap_global[ "LCtrl-S-J"] = "S-Minus"
    keymap_global[ "LCtrl-S-K"] = "S-Plus"
    keymap_global[ "Ctrl-Tab"] = "Alt-Tab"

    # CtrlでIMEオンオフ
    def ime_on():
	    keymap.wnd.setImeStatus( 1 )

    def ime_off():
        keymap.wnd.setImeStatus( 0 )

    keymap_global[ "O-LCtrl" ] = ime_on
    keymap_global[ "O-RCtrl" ] = ime_off

    # Clipboard history related
    keymap_global[ "C-S-V"   ] = keymap.command_ClipboardList