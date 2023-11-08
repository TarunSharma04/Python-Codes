import pyautogui as spam
import time

limit = input("Enter the no. of messages:")
message = input("Message you want to send")
timing = input("Enter spam timing")
i = 0

time.sleep(1)
1
while i<int(limit):

    spam.typewrite(message)
    spam.press('Enter')

i+=1