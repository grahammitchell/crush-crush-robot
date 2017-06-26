# Crush Crush Robot

Auto-plays the silly but fun [Crush Crush](http://www.kongregate.com/games/SadPandaStudios/crush-crush).
It's a dating sim. It's an incremental clicker. It's probably not safe for work.

Only works on my computer at the moment. Requires [pyautogui](https://github.com/asweigart/pyautogui).

In particular, the offset of the upper-left corner of the *Crush Crush* game
window is hard-coded in the variable `ul`. It's probably in a different place
on your machine.

Starts by **resetting your game**, then fulfills the requirements for Cassie up
to "Friendzoned" and Mio up to "Acquaintance".

Assumes you have a high enough multiplier already that "Sorry" and dates are
instantaneous, and that you already have enough timeblocks open to work all
jobs and all hobbies at once.

