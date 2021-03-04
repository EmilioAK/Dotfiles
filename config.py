# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.LEFT_META,
    Key.LEFT_META: Key.LEFT_ALT,
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_META,
    Key.RIGHT_CTRL: Key.RIGHT_META,
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile(r'Emacs'), {
    Key.CAPSLOCK: Key.RIGHT_CTRL,
    Key.LEFT_ALT: Key.LEFT_ALT,
})

define_conditional_modmap(re.compile(r'dota2'), {
    Key.CAPSLOCK: Key.RIGHT_CTRL,
    Key.LEFT_ALT: Key.LEFT_ALT,
    Key.LEFT_META: Key.LEFT_ALT,
})

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt"), {
    # Cursor
    K("Win-b"): with_mark(K("left")),
    K("Win-f"): with_mark(K("right")),
    K("Win-p"): with_mark(K("up")),
    K("Win-n"): with_mark(K("down")),
    K("Win-h"): with_mark(K("backspace")),
    # Beginning/End of line
    K("Win-a"): with_mark(K("home")),
    K("Win-e"): with_mark(K("end")),
    #Kill line
    K("Win-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Cancel
    K("C-g"): [K("esc"), set_mark(False)],
    # Escape
    K("C-q"): escape_next_key,
}, "Emacs-like keys")
