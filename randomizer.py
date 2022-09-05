import time
from sys import argv
import random
from playsound import *
import os


#num = argv[1]
#num = int(num)

f = open("files/randomizerRuntime.txt","r")
num = f.read()
num = int(num)
print(num)
f.close()

os.system('mode con: cols=64 lines=49')
os.system('color 6')

logo = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
       __                 _                 _              
      /__\ __ _ _ __   __| | ___  _ __ ___ (_)_______ _ __ 
     / \/// _` | '_ \ / _` |/ _ \| '_ ` _ \| |_  / _ \ '__|
    / _  \ (_| | | | | (_| | (_) | | | | | | |/ /  __/ |   
    \/ \_/\__,_|_| |_|\__,_|\___/|_| |_| |_|_/___\___|_|   
    VERSION 1.0 for the NexusSnarl Software - NAFANEEL

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
print(logo)
time.sleep(1)
print("""This software is fully automatic and is dependant on
the NexusSnarl Software to be running. The program will close
when the shutdown command is sent!

[WARNING!] - Program will start right after this message after
             around 10 seconds
""")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print()
time.sleep(1)
for i in range(num):
    delay = random.randint(10,30)
    current_time = time.strftime("%H:%M:%S")
    print("["+current_time+"] Sound Sent")
    arr = os.listdir('H:\\RADIO\\NexusSnarl4\\sounds\\bruno')
    randSound = random.choice(arr)
    print(randSound)
    playsound('sounds/sqlbreak.wav')
    playsound("sounds/bruno/"+randSound)
    time.sleep(int(delay))
exit()

