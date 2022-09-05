import serial,serial.tools.list_ports

myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]

print("NEXUSSNARL-SETUP")
print()
print("Please Find A Connection With The Name 'Arduino UNO'")
print()
for i in myports:
    print(i)
print()
print("Enter NEXUSSNARL INTERFACE COM port below:")
com = input("COM_: ")

f = open("nexusCOM.txt","w")
f.write("COM"+com)
f.close()
print("Changes Have Been Made Successfully")
print()
print("NEXUSSNARL-INTERFACE set to COM"+com)
print()
input("Press ENTER to exit...")
