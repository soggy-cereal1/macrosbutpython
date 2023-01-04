import pyautogui
import time

username = 'ParalelUs'

def tabrefresh(index):   
    pyautogui.hotkey('command', 't') # open new tab when discord stops this from working
    pyautogui.hotkey('command', '1') # how to implement in below?
    pyautogui.hotkey('command', 'w')

    time.sleep(1)

    pyautogui.typewrite("https://discord.com/channels/@me \n", 0)
    time.sleep(5)
    pyautogui.click(778, 160, 1, 0, button='left') # clicks Add Friend
    #time.sleep(1)

time.sleep(3)
pyautogui.click(778, 160, 1, 0, button='left') # clicks Add Friend
# switch to discord.com/channels/@me at that point under All(no DM open)

# the above is extraneous if you have no friends

for i in range (2766,6767):
    if (len(str(i)) == 1):    
       if ((i-1)%3 != 0):
            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username + "#000" + str(i) + "\n", 0)
            time.sleep(2)

       else:
            tabrefresh(i)

            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)

            pyautogui.typewrite(username + "#000" + str(i) + "\n", 0)
            time.sleep(2)

    elif (len(str(i)) == 2):
        if ((i-1)%3 != 0):
            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username + "#00" + str(i) + "\n", 0)
            time.sleep(2)
        else:
            tabrefresh(i)

            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username + "#00" + str(i) + "\n", 0)
            time.sleep(2)
    elif (len(str(i)) == 3):
        if ((i-1)%3 != 0):
            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username + "#0" + str(i) + "\n", 0)
            time.sleep(2.5)
        else:
            tabrefresh(i)
            
            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username+ "#0" + str(i) + "\n", 0)
            time.sleep(2.5)
    elif (len(str(i)) == 4):
        if ((i-1)%3 != 0):
            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username + "#" + str(i) + "\n", 0)
            time.sleep(2.5)
        else:
            tabrefresh(i)

            pyautogui.click(500, 300, 3, 0.2, button='left')
            pyautogui.hotkey('command', 'a')
            pyautogui.typewrite(['backspace'], 0)
            pyautogui.typewrite(username + "#" + str(i) + "\n", 0)
            time.sleep(2.5)
