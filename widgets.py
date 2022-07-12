from libqtile import widget
from libqtile.lazy import lazy

from subprocess import  check_output

def widget_producer(theme: dict) -> list[widget]:
    
    widgets = [
        widget.CurrentLayoutIcon(
            scale=.75,
            background=theme["current_layout_background"],
            #foreground=dracula["white"]
        ),
        widget.GroupBox(
            #border=dracula["cyan"],
            active=theme["widget_default_foreground"],
            #background=dracula["orange"],
            block_highlight_text_color=theme["active_foreground"],
            highlight_method="block",
            #highlight_color=dracula["red"],
            hide_unused=True,
            round=True,
            margin_x=5,
            spacing=5,
            this_current_screen_border=theme["current_group"],
            #this_screen_border=catpuccin["mauve"]
        ),
        widget.WindowName(
            max_chars=30,
            #background=dracula["black"],
            #foreground=dracula["white"],
        ),
        widget.TextBox(
            "◻",
            background=theme["wallpaper_color"],
            foreground=theme["wallpaper_foreground"]
        ),
        widget.Wallpaper(
            max_chars=8,
            #foreground=dracula["white"],
            directory="~/Pictures/Wallpapers",
            wallpaper_command=["nitrogen", "--set-scaled"],
            random_selection=True
        ),
        widget.Spacer(
            8
        ),
        widget.TextBox(
            "🕰",
            background=theme["clock_color"],
            foreground=theme["clock_foreground"]
        ),
        widget.Clock(
            format="%I:%M %p",
            #foreground=dracula["white"]
        ),
        widget.TextBox(
            "🕬",
            background=theme["volume_background"],
            foreground=theme["volume_foreground"]
        ),
        widget.PulseVolume(
            fmt="{}",
            limit_max_volume=True,
            #foreground=dracula["white"],
            update_interval=.02,
            mouse_callbacks={"Button1":lazy.spawn("alacritty -e alsamixer -c 2")}
        ),
        widget.TextBox(
            "🖧",
            mouse_callbacks={"Button1":lazy.spawn("alacritty -e '/home/jonah/.config/qtile/bin/launch_nmtui.sh'")},
            background=theme["net_background"],
            foreground=theme["net_foreground"]
        ),
        widget.GenPollText(
            func=(lambda: check_output(["/home/jonah/.config/qtile/bin/check_internet.sh"]).decode()),
            #foreground=dracula["white"]
        ),
        #widget.Wlan(
        #    interface="wlp2s0",
        #    format="{essid} {percent:2.0%}",
        #    foreground=dracula["white"]
        #),
        widget.TextBox(
            "🌩",
            background=theme["bat_background"],
            foreground=theme["bat_foreground"]
        ),
        widget.Battery(
            format="{char} {percent:2.0%} {hour:d}:{min:02d}",
            #foreground=dracula["white"]
        ),
        widget.WidgetBox(
            [
                widget.LaunchBar(
                    progs=[
                        ("🛆", "slock", "locks the screen using SLock"),
                    ],
                    text_only=True,
                    background=theme["launcher_background"],
                    foreground=theme["lock"]
                ),
                widget.LaunchBar(
                    progs=[
                        ("⏾", "systemctl suspend", "suspend session"),
                    ],
                    text_only=True,
                    background=theme["launcher_background"],
                    foreground=theme["sleep"]
                ),
                widget.TextBox(
                    text='➜',
                    mouse_callbacks={
                        "Button1":lazy.shutdown()
                    },
                    background=theme["launcher_background"],
                    foreground=theme["exit"]
                ),
                widget.LaunchBar(
                    progs=[
                        ("⏻", "shutdown now", "shutdown computer"),
                    ],
                    text_only=True,
                    background=theme["launcher_background"],
                    foreground=theme["poweroff"]
                ),
            ],
            #text_closed="[⚙]",
            #text_open="[⚙]",
            #text_closed=" 🛳 ",
            #text_open=" 🛳 "
            text_closed=" 🖳 ",
            text_open=" 🖳 ",
            background=theme["widgetbox_background"],
            foreground=theme["widgetbox_foreground"],
            fontsize=24
        )
        
    ]

    return widgets
