# Crush Crush Robot

Auto-plays the silly but fun [Crush Crush](http://www.kongregate.com/games/SadPandaStudios/crush-crush).
It's a dating sim. It's an incremental clicker. It's probably not safe for work.

Only works on my computer at the moment. Requires [pyautogui](https://github.com/asweigart/pyautogui).

In particular, the offset of the upper-left corner of the *Crush Crush* game
window is hard-coded in the variable `ul`. It's probably in a different place
on your machine.

Assumes you have a high enough multiplier already that "Sorry" and dates are
instantaneous, and that you already have enough timeblocks open to work all
jobs and all hobbies at once.

Starts by **resetting your game**, then starts fulfulling the requirements for
girls in order. Hit CTRL-C if it's out of control.

Basically gets Alpha to lover status (if it can), then switches to manual mode.

Once in manual mode, type the girl's name and the current status to run the
next steps like so:

```
> pamu crush
```

Type `quit` when you're done.

