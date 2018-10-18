# Q.1- Print the current day using Datetime module.
from datetime import date
import calendar
my_date=date.today()
print(calendar.day_name[my_date.weekday()])
print('-'*50)

# Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
import time
print('program started on :'+time.ctime())
time.sleep(5)
webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
print('-'*50)

# Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os 
i = 0      
for filename in os.listdir('C:\New Folder'): 
    dst ="FILE" + str(i) + ".jpg"
    src ='xyz'+ filename 
    dst ='xyz'+ dst 
    os.rename(src, dst) 
    i += 1