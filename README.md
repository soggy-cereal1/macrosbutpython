# macrosbutpython

First, and possibly most importantly, I used pyautogui, which basically allows Python to give keyboard and mouse outputs.
I had to run pip3 install pyautogui 
in order to get it, so do that for it to work
There's supposedly a means to screenshot and locateOnScreen, which would be helpful for different types of devices, but I'm not sure I can do it.

This works on my MacBook Air M1 with 2960x1600 screen resolution. pyautogui simplifies it to 1440x960.
Basically, taking a full-screen screenshot and putting it into pixlr.com/e/, finding a pixel on the buttons, taking pixelX/totalX and multiplying it by 1440 gives X and the same with Y.

I used this in Google Chrome with Bookmarks bar open on normal zoom/magnify for discord.com

