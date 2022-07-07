# https://patreon.renpy.org/timed-choice-menus.html

# How long the player has to make a choice in timeout seconds.
default timeout = 10.0

# The label the player is sent to if they fail to make a choice in the time
# allotted. If None, the timeout is disabled.
default timeout_label = None

# A preference that enables or disables timed choices.
default persistent.timed_choices = True

default showscore = False

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action
    if showscore:
        text "{color=#801a34}Your current score is [score1]{/color}":
            xalign 0.5
            yalign 0.7
            size 50

    if (timeout_label is not None) and persistent.timed_choices:

        bar:
            xalign 0.5
            ypos 60
            xsize 740
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action Jump(timeout_label)
        timer timeout action SetVariable("isshake", True)
