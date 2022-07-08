from libqtile import widget
from libqtile.lazy import lazy

from dracula import dracula
from catpuccin import catpuccin

widgets = [
    widget.CurrentLayoutIcon(
        scale=.75,
        background=catpuccin["darklavender"],
        foreground=dracula["white"]
    ),
    widget.GroupBox(
        #border=dracula["cyan"],
        active=dracula["white"],
        #background=dracula["orange"],
        block_highlight_text_color=dracula["gray"],
        highlight_method="block",
        highlight_color=dracula["red"],
        hide_unused=True,
        round=True,
        margin_x=5,
        spacing=5,
        this_current_screen_border=catpuccin["peach"],
        #this_screen_border=catpuccin["mauve"]
    ),
    widget.WindowName(
        max_chars=30,
        #background=dracula["black"],
        foreground=dracula["white"],
    ),
    widget.TextBox(
        "🕰 Time",
        background=dracula["red"],
        foreground=dracula["gray"]
    ),
    widget.Clock(
        format="%I:%M %p",
        foreground=dracula["white"]
    ),
    widget.TextBox(
        "🕬 Vol",
        background=catpuccin["sapphire"],
        foreground=dracula["gray"]
    ),
    widget.PulseVolume(
        fmt="{}",
        limit_max_volume=True,
        foreground=dracula["white"],
        update_interval=.02,
        mouse_callbacks={"Button1":lazy.spawn("alacritty -e alsamixer -c 2")}
    ),
    widget.TextBox(
        "🖧 Net",
        mouse_callbacks={"Button1":lazy.spawn("alacritty -e '/home/jonah/.config/qtile/bin/launch_nmtui.sh'")},
        background=catpuccin["yellow"],
        foreground=dracula["gray"]
    ),
    widget.Wlan(
        interface="wlp2s0",
        format="{essid} {percent:2.0%}",
        foreground=dracula["white"]
    ),
    widget.TextBox(
        "🌩 Batt",
        background=catpuccin["green"],
        foreground=dracula["gray"]
    ),
    widget.Battery(
        format="{char} {percent:2.0%} {hour:d}:{min:02d}",
        foreground=dracula["white"]
    ),
    widget.WidgetBox(
        [
            widget.LaunchBar(
                progs=[
                    ("🛆", "slock", "locks the screen using SLock"),
                ],
                text_only=True,
                background=catpuccin["black"],
                foreground=catpuccin["sky"]
            ),
            widget.LaunchBar(
                progs=[
                    ("⏾", "systemctl suspend", "suspend session"),
                ],
                text_only=True,
                background=catpuccin["black"],
                foreground=dracula["yellow"]
            ),
            widget.QuickExit(
                default_text='➜',
                countdown_format='[{}]',
                background=catpuccin["black"],
                foreground=dracula["orange"]
            ),
            widget.LaunchBar(
                progs=[
                    ("⏻", "shutdown now", "shutdown computer"),
                ],
                text_only=True,
                background=catpuccin["black"],
                foreground=dracula["red"]
            ),
        ],
        text_closed="[⚙]",
        text_open="[⚙]",
        background=catpuccin["darklavender"],
        foreground=dracula["white"],
        fontsize=24
    )
    
]