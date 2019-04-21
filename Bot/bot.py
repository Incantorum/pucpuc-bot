# Work with Python 3.6
import discord
from spreadsheets import *
from common_embed import *

TOKEN = 'NTIwNjQ3OTI2MjA1MzgyNjY2.XLtzkA.vQ88_HoWqXWrOKHT1QyMyg_UybI'

client = discord.Client()

server_default_thumbnail = "https://cdn.discordapp.com/attachments/492461461113667605/568033372543385611/cha_block_madoka01_v01-CAB-c50120ac711700ee630d6512935a44fe-1479165618584560336.png"

permited_ema_stars = ['1','2','3','4','5','ANY','Any','any']
permited_ema_skill = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','ANY']

emaList = dict()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await channel.send(msg)

    if message.content.startswith('!updateDB'):
        updateDB1_3()
        updateDB4_5()
        await channel.send("```Database Updated```")

    if message.content.startswith('!searchEma'):
        emaList = loadEmaList1_3()
        msg = ""
        find = message.content.split(";")
        find[2] = find[2].upper()
        if ((len(find) != 3) or not(find[1] in permited_ema_stars) or not(find[2] in permited_ema_skill)):
            embed_msg = generic_embed("Error", "Wrong format", "", server_default_thumbnail)
            await channel.send("```Wrong Format```")
        else:
            for arc in emaList:
                for ema in emaList[arc]:
                    if((find[2]==ema[1]) and (find[1]==ema[2])):
                        msg = msg + "\t%s - %s - %s\n" % (ema[0],ema[1],ema[2])
            embed_msg = generic_embed("Ema Found", msg, "", server_default_thumbnail)
            await channel.send(embed = embed_msg)
    
    if message.content.startswith('!searchEmaOf'):
        emaList = loadEmaList4_5()
        msg = ""
        find = message.content.split()
        
        if (len(find) != 2):
            await channel.send("")
        for arc in emaList:
            for ema in emaList[arc]:
                if( find[1] in ema ):
                    msg = msg + "\t%s - %s - %s\n" % (ema[0],ema[1],ema[2])
        await channel.send("```Ema found```")
        

    if message.content.startswith('!quit'):
        exit()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)