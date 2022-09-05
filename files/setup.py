import time
import os
import sys

os.system('cls')
os.system('color 9')
os.system('mode con: cols=64 lines=20')

header = """
================================================================
  NEXUSSNARL - SETUP  | Ver 1.0  | NAFANEEL
================================================================
"""

print(header)
print("Welcome to the Nexus Snarl Setup Tool.")

print("""
This tool will install all the packages needed to run
NexusSnarl. The setup tool will detect any packages and install
them on your system using python PIP.

""")

input("Press Enter To Continue...")


os.system("cls")
print(header)
#Install packages

try:
    import playsound
    print("Found Playsound")
except:
    print("Playsound Not Found...")
    input("press enter to install...")
    os.system('pip3 install playsound')
try:
    import discord
    print("Found Discord.py")
except:
    print("Discord.py Not Found...")
    input("press enter to install...")
    os.system('pip3 install discord')
try:
    import serial
    print("Found serial")
except:
    print("serial Not Found...")
    input("press enter to install...")
    os.system('pip3 install serial')

print()
print()
input("Thats Setup Complete! \nPress ENTER to exit...")




