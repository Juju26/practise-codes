import random
from pynput.keyboard import Key, Controller
import time
def met():
    keyboard = Controller()
    for i in range(7):    # <--coloumns of excel
        s=random.randint(25,30)
        s=str(s)                    
        keyboard.press(str(s[0]))    
        keyboard.release(str(s[0]))
        keyboard.press(str(s[1]))
        keyboard.release(str(s[1]))
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)    
time.sleep(5)
for i in range(10):   # <--rows of excel
    met()
print('Done')
 