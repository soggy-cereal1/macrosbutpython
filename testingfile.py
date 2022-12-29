import pyautogui
import time

def tabrefresh(index):   
    pyautogui.hotkey('command', 't') # open new tab when discord stops this from working
    pyautogui.hotkey('command', '1') # how to implement in below?
    pyautogui.hotkey('command', 'w')

    time.sleep(1)

    pyautogui.typewrite("https://discord.com/channels/@me \n", 0)
    time.sleep(7)
    pyautogui.click(778, 160, 1, 0, button='left') # clicks Add Friend
    time.sleep(1)

time.sleep(3)

for i in range (1,7):
    if ((i-1)%3 != 0):
        pyautogui.click(500, 300, 3, 0.2, button='left') # click box
        pyautogui.hotkey('command', 'a')
        pyautogui.typewrite(['backspace'], 0) # resets if there's old names

        pyautogui.typewrite("Someone_#0" + str(759) + "\n", 0)
        time.sleep(2)
        print("Completed task number " + str(i))
    else:
        tabrefresh(i)
        
        pyautogui.click(500, 300, 3, 0.2, button='left')
        pyautogui.hotkey('command', 'a')
        pyautogui.typewrite(['backspace'], 0)
        pyautogui.typewrite("Someone_#0" + str(759) + "\n", 0)
        time.sleep(2)
        print("Completed task number " + str(i))