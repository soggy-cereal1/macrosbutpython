import pyautogui
import time

username = 'ParalelUs'

def tabrefresh():   
    pyautogui.hotkey('ctrl', 't') # open new tab when discord stops this from working
    pyautogui.hotkey('ctrl', '1') # how to implement in below?
    pyautogui.hotkey('ctrl', 'w')

    time.sleep(1)

    pyautogui.typewrite("https://discord.com/channels/@me \n")
    time.sleep(5)
    pyautogui.click(1200, 190, 1, 0, button='left') # clicks Add Friend
    #time.sleep(1)

def log():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite('\n')
    pyautogui.hotkey('alt','tab')

    pyautogui.click(550, 380, 1, 0, button='left')
    pyautogui.typewrite('\n')

def clear():
    pyautogui.click(550, 380, 3, 0.2, button='left')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(['backspace'])

time.sleep(3)
pyautogui.click(1200, 190, 1, 0, button='left') # clicks Add Friend
# switch to discord.com/channels/@me at that point under All(no DM open)

# the above is extraneous if you have no friends

for i in range (4001,6767):
    if (len(str(i)) == 1):    
       if ((i-1)%3 != 0):
            clear()
            pyautogui.typewrite(username + "#000" + str(i)) 

            log()
            time.sleep(2.5)

       else:
            tabrefresh()

            clear()

            pyautogui.typewrite(username + "#000" + str(i))

            log()
            time.sleep(2.5)

    elif (len(str(i)) == 2):
        if ((i-1)%3 != 0):
            clear()

            pyautogui.typewrite(username + "#00" + str(i))
            
            log()
            time.sleep(2.5)
        else:
            tabrefresh()

            clear()

            pyautogui.typewrite(username + "#00" + str(i))

            log()
            time.sleep(2.5)
    elif (len(str(i)) == 3):
        if ((i-1)%3 != 0):
            clear()

            pyautogui.typewrite(username + "#0" + str(i))

            log()
            time.sleep(2.5)
        else:
            tabrefresh()
            
            clear()

            pyautogui.typewrite(username+ "#0" + str(i))

            log()
            time.sleep(2.5)
    elif (len(str(i)) == 4):
        if ((i-1)%3 != 0):
            clear()

            pyautogui.typewrite(username + "#" + str(i))

            log()
            time.sleep(2.5)
        else:
            tabrefresh()

            clear()

            pyautogui.typewrite(username + "#" + str(i))

            log()
            time.sleep(2.5)
