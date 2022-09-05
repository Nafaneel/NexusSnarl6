import discord
from discord.ext import commands
from itertools import cycle
import os
import sys
import subprocess
#==MAIN LEVEL IMPORTS==
import time
from playsound import *
from datetime import datetime
from datetime import date
#==ENTERNAL .PY FILES IMPORT==
from externalCommands import *
import serial,serial.tools.list_ports

#STATE DATE AND START EXIF FILE
from tokenFile import *
today = date.today()

exifNow = datetime.now()
exifCurrent_time = exifNow.strftime("%H:%M:%S")


exifStart = """\n\nNEXUSSNARL3 - START: {} - DATE: {} """.format(exifCurrent_time, today)

myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]



def exifPlot(user,command,time,date):
    wr = open("files/exif.CSV","a")
    toEXIF = "\n|- [{} : {} : {}] {}".format(user,time,date,command)
    wr.write(toEXIF)
    wr.close()



#==CONFIGURE BOT PREFIX==
client = commands.Bot(command_prefix = '~')

#==STARTUP GUI CONFIGURE==
os.system('cls')
#os.system('color a') 
os.system('mode con: cols=64 lines=49') #<<< CHANGE SCREEN SIZE <<<

comGrab = open("NexusSnarl-Interface/nexusCOM.txt","r")
comID = str(comGrab.read())
comGrab.close()

def connectUSB():
    try:
        global ser
        ser = serial.Serial(comID)
    except:
        os.system('color 4')
        print(usbError)
        print("Couldn't connect to: "+comID)
        input("Press Enter To Exit Application...")
        exit()
connectUSB()

def tx():
    ser.write(b'on')

def stop():
    ser.write(b'off')

def termsRead():
    print(logoTerms)
    print(one)
    input()
    os.system('cls')
    print(logoTerms)
    print(two)
    input()
    os.system('cls')
    print(logoTerms)
    print(three)
    input()
    os.system('cls')
    print(logoTerms)
    print(four)
    input()
    os.system('cls')
    print(logoTerms)
    print(five)
    input()
    os.system('cls')
    print(logoTerms)
    print(six)
    input()
    wrr = open("files/accept.txt","w")
    wrr.write("True")
    wrr.close()
    os.system('cls')
    os.system('color a')
    time.sleep(0.5)
    

#==SPLASH SCREEN==
from terms import *
def splashConfig(waitTime):
    os.system('color 20') #<<< CHANGE SPLASH SCREEN COLOUR<<<
    splashScreen() 
    time.sleep(1)
    os.system('cls')
    os.system('color a')
    time.sleep(int(waitTime))
    termsAcceptFile = open("files/accept.txt","r")
    if termsAcceptFile.read() == "False":
        os.system("cls")
        os.system('color 6')
        termsRead()
        termsAcceptFile.close()
        os.system('cls')
splashConfig(1)





def userInterface():
    
    #==DISPLAY MAIN GUI
    print(mainGUI)

    #==DISPLAY TOKENS==
    print(" TOKENS:")
    for i in tokens:
        print("  ",i,"   ", tokens[i])
        
    print()
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print()
userInterface()

#==CHANNEL ID's GET======================
exifChannel = open("ids/exifChannel.id","r")
exifID = int(exifChannel.read())
exifChannel.close()

requestChannel = open("ids/request.id","r")
requestID = int(requestChannel.read())
requestChannel.close()

tokenGrab = open("ids/tokenFile.id","r")
tokenID = tokenGrab.read()
tokenGrab.close()



#==MAIN PROGRAM LOG==

print("[{}] Creating EXIF File For {}".format(exifCurrent_time, today))

w = open("files/exif.CSV","a")
w.write(exifStart)
w.close()

print("[!] Discord Bot Now Launching...")


#==ACTIVATE UPON CONNECT==
@client.event
async def on_ready():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("["+current_time+"] Discord Bot Online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="The Radio"))
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Thwarting the airwaves!"))

#==MAIN SOUNDS==
@client.command()
async def randomizer(ctx,stat):
    channel = client.get_channel(exifID)
    if stat =="stop":
        os.system('taskkill /fi "windowtitle eq C:\WINDOWS\py.exe"')
        await ctx.send(">>> **["+ctx.author.name+"]** Randomizer Stopped")
        await channel.send("["+ctx.author.name+"] - [RANDOMIZER] : (Stopped)")
    if stat =="help":
        await ctx.send(">>> **["+ctx.author.name+"]** Randomizer Help")
        await ctx.send(randomizerHelp)
    else:
        f = open("files/randomizerRuntime.txt","w")
        f.write(stat)
        f.close()
        os.startfile('randomizer.py') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ADD RANDOMIZER FILE
        await ctx.send(">>> **["+ctx.author.name+"]** Randomizer Started!")
        await channel.send("["+ctx.author.name+"] - [RANDOMIZER] : (Started)")

#==REMOTE KILL PROGRAM==
@client.command()
async def kill(ctx):
    exit()

@client.command()
async def reload(ctx):
    os.startfile('remoteRestart.py')
    exit()




#==TOKEN SUBTRACTOR==
#-ALWAYS ADD 1 MORE THAN NEEDED
def checktokens(name):
    if name =="Nafaneel":
        return True
    if name =="Andrew_mc":
        tokens[name] -= 1
        if tokens[name] > 0:
            return True
        elif tokens[name] == 0:
            return False
        else:
            return False
    if name =="Michael-Abr00NMujahid":
        tokens[name] -= 1
        if tokens[name] > 0:
            return True
        elif tokens[name] == 0:
            return False
        else:
            return False
    if name =="Nafaneel2":
        tokens[name] -= 1
        if tokens[name] > 0:
            return True
        elif tokens[name] == 0:
            return False
        else:
            return False

def accountCheck(name):
    if name in tokens:
        return True
    else:
        return False
    

#==CHECK ALL TOKENS==      
@client.command()
async def alltokens(ctx):
    await ctx.send(tokens)

checkSend = """
>>> __***NEXUSSNARL - NAFANEEL***__
http://nexussnarl.nafaneel.uk/
_USER:_  **{}**
_STATUS:_  **{}**
Type `~commands` for a list of options"""

@client.command()
async def request(ctx, option):
    #1005553204123156601
    channel = client.get_channel(requestID) 
    if option =="verify":
        embed=discord.Embed(title="Nexus Verification", url="https://main.nafaneel.repl.co/nexus-verify.html", description="An automated response has been submitted, Please click the link above to learn more about the verification process.", color=discord.Color.green())
        await ctx.send(embed=embed)
        await channel.send("> "+ctx.author.name+" Has requested nexus verification.")
    elif option == "tokens":
        await ctx.send("> **A request has been submitted**")
        await channel.send("> "+ctx.author.name+" Has requested nexus tokens.")
  
@client.command()
async def stopTX(ctx):
    stop()
    await ctx.send(">>> **Sent The Stop Signal**")
  
@client.command()
async def com(ctx):
    deviceCOM = ">>> The NexusSnarl Interface Is Connected On Port `{}`".format(ser)
    await ctx.send(deviceCOM)
    

    
@client.command()
async def info(ctx):
    embed=discord.Embed(title="NexusSnarl Ver. 5", url="http://nexussnarl.nafaneel.uk/", description="Learn more about the bot by clicking the link above", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
async def check(ctx):
    if accountCheck(ctx.author.name) == True:
        await ctx.send(checkSend.format(ctx.author.name, "NEXUS VERIFIED"))
    elif accountCheck(ctx.author.name) == False:
        await ctx.send(checkSend.format(ctx.author.name, "UNVERIFIED"))


#==ADD TOKENS TO ACCOUNT==
@client.command()
async def addtokens(ctx,name,ammount):
    if ctx.author.name =="Nafaneel":
        if name =="Jack":
            tokens["Andrew_mc"] += int(ammount)
        if name =="ZA":
            tokens["Michael-Abr00NMujahid"] += int(ammount)
        else:            
            tokens[name] += int(ammount)
            await ctx.send(tokens)
    else:
        await ctx.send("[!]You do not have permission to perform this action!")

#==REMOVE TOKENS FROM ACCOUNT==
@client.command()
async def removetokens(ctx,name,ammount):
    if ctx.author.name =="Nafaneel":
        if name =="Jack":
            tokens["Jack Phasey"] -= int(ammount)
            await ctx.send(tokens)
        else:
            tokens[name] -= int(ammount)
            await ctx.send(tokens)
    else:
        await ctx.send("[!]You do not have permission to perform this action!")
    
#==CHECK INDUVIDUALS TOKENS==          
@client.command()
async def viewtokens(ctx):
    tokensViewStr = ">>> `{}` - You have **{}** tokens"
    await ctx.send(tokensViewStr.format(ctx.author.name, tokens[ctx.author.name]))
    #await ctx.send("["+ctx.author.name+"] - You have the following ammount of tokens:")
    #await ctx.send(tokens[ctx.author.name])

#==AVAILABLE COMMANDS==
@client.command()
async def commands(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("["+ctx.author.name+" : "+current_time+"] Commands")
    #await ctx.send("**NexusSnarl↯ Is Online. Type '~commands' for a list of options available.**")
    #await ctx.send("**[!]KEEP IT LEGAL (As Much As Possible)** ( ͡~ ͜ʖ ͡°)")
    #await ctx.send("**[!]For Documentation visit**: https://www.nafaneel.repl.co/radio-projects/nexussnarl.html ")
    #await ctx.send("**[!]For Documentation visit**: https://www.nafaneel.repl.co/radio-projects/nexussnarl-help.html")
    await ctx.send(header)
    await ctx.send(commandsAll) #<<< LOCATED IN externalCommands
    await ctx.send(bruno)

    
@client.command()
async def clear(ctx):
    await ctx.channel.purge()

#SEND DONE COMMAND
@client.command()
async def raging(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~raging` Command Has Been Removed')

@client.command()
async def gay(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~gay` Command Has Been Removed')

@client.command()
async def queer(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~queer` Command Has Been Removed')   

@client.command()
async def batty(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~batty` Command Has Been Removed')

@client.command()
async def women(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~women` Command Has Been Removed')

@client.command()
async def massacre(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~massacre` Command Has Been Removed')

@client.command()
async def scream(ctx,arg1):
    await ctx.send('>>> ***['+ctx.author.name+']*** - The `~scream` Command Has Been Removed')

#=========================================================================================================
# MISC SOUNDS
#=========================================================================================================

@client.command()
async def bronson(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] bronson")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/bronson.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] bronson")
        exifPlot(ctx.author.name,"bronson",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def buggeroff(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] buggeroff")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/buggeroff.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] buggeroff")
        exifPlot(ctx.author.name,"buggeroff",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def jam(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] jam")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/jam.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] jam")
        exifPlot(ctx.author.name,"jam",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def laugh(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] laugh")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/laugh.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] laugh")
        exifPlot(ctx.author.name,"laugh",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def laugh2(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] laugh2")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/laugh2.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] laugh2")
        exifPlot(ctx.author.name,"laugh2",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def moore(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] moore")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/moore.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] moore")
        exifPlot(ctx.author.name,"moore",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def scream2(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] scream2")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/scream2.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] scream2")
        exifPlot(ctx.author.name,"scream2",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def shortjam(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] shortjam")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/shortjam.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] shortjam")
        exifPlot(ctx.author.name,"shortjam",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def soppy(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] soppy")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/misc/soppy.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] soppy")
        exifPlot(ctx.author.name,"soppy",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


#=========================================================================================================
# STEVEN DAWSON
#=========================================================================================================

@client.command()
async def bigc(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] bigc")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/bigc.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] bigc")
        exifPlot(ctx.author.name,"bigc",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def bitbad(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] bitbad")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/bitbad.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] bitbad")
        exifPlot(ctx.author.name,"bitbad",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def chatshit(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] chatshit")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/chatshit.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] chatshit")
        exifPlot(ctx.author.name,"chatshit",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def dognonce(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] dognonce")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/dognonce.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] dognonce")
        exifPlot(ctx.author.name,"dognonce",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def lizard(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] lizard")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/lizard.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] lizard")
        exifPlot(ctx.author.name,"lizard",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def orgasm(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] orgasm")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/orgasm.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] orgasm")
        exifPlot(ctx.author.name,"orgasm",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def orgasm2(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] orgasm2")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/orgasm2.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] orgasm2")
        exifPlot(ctx.author.name,"orgasm2",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def pussy(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] pussy")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/sd/pussy.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] pussy")
        exifPlot(ctx.author.name,"pussy",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')  

#=========================================================================================================
# BRUNO POWROZNIK
#=========================================================================================================

@client.command()
async def agewell(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] agewell")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/agewell.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] agewell")
        exifPlot(ctx.author.name,"agewell",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def analvirgin(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] analvirgin")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/analvirgin.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] analvirgin")
        exifPlot(ctx.author.name,"analvirgin",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def attribute(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] attribute")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/attribute.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] attribute")
        exifPlot(ctx.author.name,"attribute",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def beautyandbrains(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] beautyandbrains")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/beautyandbrains.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] beautyandbrains")
        exifPlot(ctx.author.name,"beautyandbrains",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def beckyb(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] beckyb")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/beckyb.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] beckyb")
        exifPlot(ctx.author.name,"beckyb",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def bigtits(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] bigtits")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/bigtits.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] bigtits")
        exifPlot(ctx.author.name,"bigtits",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def brownaction(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] brownaction")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/brownaction.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] brownaction")
        exifPlot(ctx.author.name,"brownaction",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def buggery(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] buggery")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/buggery.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] buggery")
        exifPlot(ctx.author.name,"buggery",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def doctor(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] doctor")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/doctor.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] doctor")
        exifPlot(ctx.author.name,"doctor",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def dontmix(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] dontmix")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/dontmix.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] dontmix")
        exifPlot(ctx.author.name,"dontmix",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def fantastic(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] fantastic")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/fantastic.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] fantastic")
        exifPlot(ctx.author.name,"fantastic",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def fuckoffstrscum(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] fuckoffstrscum")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/fuckoffstrscum.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] fuckoffstrscum")
        exifPlot(ctx.author.name,"fuckoffstrscum",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def fullof(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] fullof")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/fullof.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] fullof")
        exifPlot(ctx.author.name,"fullof",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def gov(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] gov")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/gov.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] gov")
        exifPlot(ctx.author.name,"gov",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def hetero(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] hetero")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/hetero.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] hetero")
        exifPlot(ctx.author.name,"hetero",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def ilove(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] ilove")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/ilove.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] ilove")
        exifPlot(ctx.author.name,"ilove",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def incomp(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] incomp")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/incomp.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] incomp")
        exifPlot(ctx.author.name,"incomp",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def intelligent(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] intelligent")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/intelligent.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] intelligent")
        exifPlot(ctx.author.name,"intelligent",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def inverse(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] inverse")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/inverse.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] inverse")
        exifPlot(ctx.author.name,"inverse",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def money(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] money")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/money.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] money")
        exifPlot(ctx.author.name,"money",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def nohope(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] nohope")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/nohope.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] nohope")
        exifPlot(ctx.author.name,"nohope",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def nutters(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] nutters")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/nutters.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] nutters")
        exifPlot(ctx.author.name,"nutters",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def pretend(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] pretend")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/pretend.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] pretend")
        exifPlot(ctx.author.name,"pretend",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def psycho(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] psycho")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/psycho.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] psycho")
        exifPlot(ctx.author.name,"psycho",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def queersexual(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] queersexual")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/queersexual.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] queersexual")
        exifPlot(ctx.author.name,"queersexual",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def rentforever_short(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] rentforever-short")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/rentforever-short.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] rentforever-short")
        exifPlot(ctx.author.name,"rentforever-short",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def rentforever(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] rentforever")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/rentforever.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] rentforever")
        exifPlot(ctx.author.name,"rentforever",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def satan(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] satan")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/satan.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] satan")
        exifPlot(ctx.author.name,"satan",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def shat(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] shat")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/shat.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] shat")
        exifPlot(ctx.author.name,"shat",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def spaz(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] spaz")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/spaz.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] spaz")
        exifPlot(ctx.author.name,"spaz",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def str(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] str")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/str.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] str")
        exifPlot(ctx.author.name,"str",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def strfuckers(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] strfuckers")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/strfuckers.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] strfuckers")
        exifPlot(ctx.author.name,"strfuckers",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def vag(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] vag")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/vag.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] vag")
        exifPlot(ctx.author.name,"vag",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def vag2(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] vag2")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/vag2.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] vag2")
        exifPlot(ctx.author.name,"vag2",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def wankers(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] wankers")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/wankers.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] wankers")
        exifPlot(ctx.author.name,"wankers",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')


@client.command()
async def website(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] website")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/bruno/website.wav')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] website")
        exifPlot(ctx.author.name,"website",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')







client.run(tokenID)
