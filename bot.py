import pyautogui
import time
import win10toast

from win10toast import ToastNotifier
from pynput import keyboard

toaster = ToastNotifier()
#toaster.show_toast("AlerTi","You are away from PC")
#timer
bool = True
timer = 0
restTime = 5
while(bool):

    time.sleep(1)
    timer = timer + 1
    print(str(timer) + " second")
    #rest time reminder will pop out every 30 minute
    if timer < restTime:

        x = pyautogui.position()
        time.sleep(1)
        timer = timer + 1
        y = pyautogui.position()
        if x == y:
            toaster.show_toast("AlerTi","You are away from PC")

            restTime = restTime + 5

        else:
            print("Unknown")


    elif timer > restTime:
        bool = False
        toaster.show_toast("AlerTi","Time to rest up")
