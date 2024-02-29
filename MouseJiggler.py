#Mouse Jiggler

import pyautogui
import time
import random

def move_mouse():
    x, y = pyautogui.position() #get the current mouse position
    
    #generate random offsets for mouse movements
    offset_x = random.randint(-10,10)
    offset_y = random.randint(-10,10)

    #move the mouse cursor
    pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.1)

def click_mouse():
    pyautogui.click()

def main():
    print("Mouse Jiggler running...")
    try:
        while True:
            move_mouse()
            click_mouse() #Add clicking action
            time.sleep(5) #Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("Mouse Jiggler stopped.")

if __name__ == "__main__":
    main()
