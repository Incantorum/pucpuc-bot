# Work with Python 3.6
import discord
import json
import os
from common_embed import *

client = discord.Client()

info = [
    ["'1-3 Star Ema List'!D3:G", "Hitagi Crab"],
    ["'1-3 Star Ema List'!J3:M", "Mayoi Snail"],
    ["'1-3 Star Ema List'!P3:S", "Suruga Monkey"],
    ["'1-3 Star Ema List'!V3:Y", "Nadeko Snake"],
    ["'1-3 Star Ema List'!AB3:AE", "Tsubasa Cat"],
    ["'1-3 Star Ema List'!AH3:AK", "Karen Bee"],
    ["'1-3 Star Ema List'!AT3:AW", "Zaregoto"]
]

server_default_thumbnail = "https://cdn.discordapp.com/attachments/492461461113667605/568033372543385611/cha_block_madoka01_v01-CAB-c50120ac711700ee630d6512935a44fe-1479165618584560336.png"

permited_ema_stars = ['1','2','3','4','5','ANY','Any','any']
permited_ema_skill = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','ANY']

emaList = dict()
emaList4_5 = []

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.startswith('$hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await channel.send(msg)

    elif message.content.startswith('$searchEma'):
        emaList = loadEmaList1_3()
        msg = ""
        find = message.content.split(";")
        find[2] = find[2].upper()
        find[1] = find[1].upper()
        if ((len(find) != 3) or not(find[1] in permited_ema_stars) or not(find[2] in permited_ema_skill)):
            await channel.send(embed = error_embed())
        else:
            for arc in emaList:
                for ema in emaList[arc]:
                    print("{find[2]} - {find[2]}")
                    if((find[2]==ema[1] or find[2]=="ANY") and (find[1]==ema[2] or find[1].upper=="ANY")):
                        print("added")
                        msg = msg + "\t%s - %s - %s\n" % (ema[0],ema[1],ema[2])
            if(len(msg) > 2048):
                embed_msg = error_embed(error="Result too big")
            else:
                embed_msg = generic_embed("Ema Found", msg, "", server_default_thumbnail)
            await channel.send(embed = embed_msg)
    
    elif message.content.startswith('$searchCharEma'):
        emaList4_5 = loadEmaList4_5()
        msg = ""
        find = message.content.split()

        if (len(find) != 2):
            await channel.send(embed = error_embed())
        for ema in emaList4_5["data"]:
            if( find[1] in ema[0] ):
                msg = msg + "\t%s\n" % (ema[0])
        embed_msg = generic_embed("Ema found", msg, "", server_default_thumbnail)
        await channel.send(embed = embed_msg)
    
    elif message.content.startswith('$ema'):
        emaList4_5 = loadEmaList4_5()
        msg = ""
        find = message.content.split()

        if (len(find) != 2):
            await channel.send(embed = error_embed())
        try:
            num = int(find[1])-1
            if(num<len(emaList4_5["data"])):
                ema = emaList4_5["data"][num]
                embed_msg = generic_embed(ema[0], ema[2], ema[3], "")
                await channel.send(embed = embed_msg)
            else:
                await channel.send(error_embed(error="Not in range"))
        except ValueError:
            await channel.send(embed = error_embed(error = "Wrong format, %s is not a number" % find[1]))

    elif message.content.startswith('$quit'):
        exit()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def loadEmaList4_5():
    f = open("emaList4_5.json")
    jfile = json.load(f)
    return jfile

def loadEmaList1_3():
    f = open("emaList.json")
    jfile = json.load(f)
    db = dict()
    for arc in info:
        db[arc[1]]=[]
    for ema in jfile["data"]:
        db[ema[4]].append(ema)
    return db

client.run(os.getenv('TOKEN'))