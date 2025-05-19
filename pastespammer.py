import keyboard
import pyautogui
import time

spamming = False
last_state = None 

def toggle_spam():
    global spamming
    spamming = not spamming

keyboard.add_hotkey('space', toggle_spam)

print("* SPACE to start - or stop spamming, and CTRL + Z, X, C, V to exit.")

try:
    while True:
        if spamming != last_state:
            last_state = spamming
            print(f"Spamming: {'TRUE' if spamming else 'FALSE'}")
            
        if spamming:
            pyautogui.hotkey('ctrl', 'v', 'x', 'c', 'v')
            pyautogui.press('enter')
            time.sleep(0.2)
        else:
            time.sleep(0.1)  
            
except KeyboardInterrupt:
    print("Exit")
