
import pyautogui
import time
import threading
from multiprocessing.pool import ThreadPool

# To get input for time interval between screenshots by user
n = pyautogui.prompt(text='Interval in secs (+ integers)', title='Batch Screenshot' , default='')
# Changing datatype to integer
sec = int(n)
print(sec)

# Assigning cmd with 'Continue'
cmd = 'Continue'

# Creating a user-defined function to get input from user when to stop
def stop():
    global cmd
    cmd = pyautogui.confirm(text='Press Stop to end the process', title='Batch Screenshot', buttons=['Stop'])

# Creating a parallel thread
stop_thread = threading.Thread(target=stop)
rc = stop_thread.start()
print(rc)

# Creating an infinite loop to take screenshots at a given interval (sec) by the user
cnt=0
while cmd == 'Continue':
    pyautogui.hotkey('alt', 'printscreen')
    time.sleep(sec)
    print(cmd)
    print(cnt)
    cnt = cnt + 1
    # if cmd == 'Stop':
    #     pyautogui.confirm(text=r'Screenshots saved at C:\Users\abhi0\OneDrive\Pictures\Screenshots', title='Voila !', buttons=['Close'])
    # if cnt == 100:
    #     break

# update : The program flow breaks once the "User provides the Stop command" - Need to fix in next updates.
# update : The  issue seems due to threading
# Creating a user-defined function to get input from user when to stop
# def save_msg():
#     msg = pyautogui.confirm(text=r'Screenshots saved at C:\Users\abhi0\OneDrive\Pictures\Screenshots', title='Voila !', buttons=['Close'])
# save_msg()