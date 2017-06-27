# Crush Crush Robot

Auto-plays the silly but fun [Crush Crush](http://www.kongregate.com/games/SadPandaStudios/crush-crush).
It's a dating sim. It's an incremental clicker. It's probably not safe for work.

Requires [pyautogui](https://github.com/asweigart/pyautogui).

Make sure the *Crush Crush* game window is visible when you run the script,
because it begins by taking a screenshot and using that to try to figure out
the upper-left-hand corner of the game.

Assumes you have a high enough multiplier already that "Sorry" and dates are
instantaneous, and that you already have enough timeblocks open to work all
hobbies and most jobs at once.

Starts by **resetting your game**, then starts fulfulling the requirements for
girls in order. Hit CTRL-C if it's out of control.

Basically gets Alpha to lover status (if it can), then switches to manual mode.

Once in manual mode, type the girl's name and the current status to run the
next steps like so:

```
> pamu crush
```

Type `quit` when you're done.

