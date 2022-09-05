import time

print("----------------------------------------------------------")
print("NEXUS SNARL - Add Sound")
print("----------------------------------------------------------")
print()

folder = input("FOLDER:")
name = input("COMMAND NAME: ")
print()
print("""
@client.command()
async def {}(ctx,arg1):
    if checktokens(ctx.author.name) == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("["+ctx.author.name+" : "+current_time+"] {}")
        time.sleep(int(arg1))
        tx()
        playsound('sounds/{}/{}')
        stop()
        await ctx.send('>>> ***['+current_time+'] Sent!***')
        channel = client.get_channel(exifID)
        await channel.send("["+ctx.author.name+" : "+current_time+"] {}")
        exifPlot(ctx.author.name,"{}",current_time,today)
    elif checktokens(ctx.author.name) == False:
        await ctx.send('***['+ctx.author.name+'] - You have no more tokens to perform this action!***')
""".format(name, name, folder, name, name, name))

print()
print()
input("PRESS ENTER TO EXIT")
