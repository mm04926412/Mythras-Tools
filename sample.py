# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:20:42 2020

@author: mm049
"""

# Work with Python 3.6
import discord
from discord.ext import commands
import random
from math import ceil

diff_dic = {'veryeasy':2.,'easy':1.5,'normal':1.,'hard':2/3,'formidable':1/2,'herculean':1/10}

TOKEN = 'Nearly forgot to remove this'

client = discord.Client()

bot = commands.Bot('$')

@bot.command()
async def skillroll(ctx,skill1,difficulty1):
    skill1 = int(skill1)
    effective_skill1 = ceil(skill1*diff_dic[difficulty1])
    roll = random.randint(1,100)
    if roll < effective_skill1/10:
        success1 = 'Critical Success!!!'
    elif roll < effective_skill1:
        success1 = 'Success'
    elif roll > effective_skill1:
        success1 = 'Failed'
    elif roll == 100:
        success1 = 'Critical Failure!!! Good luck!'

    await ctx.send('rolled ' + str(roll) + ' against the required ' + str(effective_skill1))
    await ctx.send(success1)

@bot.command()
async def contestedroll(ctx,skill1,difficulty1,skill2,difficulty2):
    
    print(skill1)
    print(difficulty1)
    print(skill2)
    print(difficulty2)
    
    skill1 = int(skill1)
    skill2= int(skill2)
    
    roll1 = random.randint(1,100)
    roll2 = random.randint(1,100)    
    
    effective_skill1 = ceil(skill1*diff_dic[difficulty1])
    effective_skill2 = ceil(skill2*diff_dic[difficulty2])
    
    if roll1 < effective_skill1/10:
        success1 = 1
    elif roll1 < effective_skill1:
        success1 = 2
    elif roll1 > effective_skill1:
        success1 = 3
    elif roll1 == 100:
        success1 = 4
        
    if roll2 < effective_skill2/10:
        success2 = 1
    elif roll2 < effective_skill2:
        success2 = 2
    elif roll2 > effective_skill2:
        success2 = 3
    elif roll2 == 100:
        success2 = 4
        
    if success1 != success2:
        if success1 < success2:
            winner = 'Attacker'
            degrees = success2-success1
        if success1 > success2:
            winner = 'Defender'
            degrees = success1-success2
    else:
        if roll1>roll2:
            winner='Attacker'
            degrees = 0
        else:
            winner='Defender'
            degrees = 0 
    
    attacker_string = ('Attacker rolls ' + str(roll1) + ' with requirement of ' + str(effective_skill1))
    defender_string = ('Defender rolls ' + str(roll2) + ' with requirement of ' + str(effective_skill2))
    result_string   = (winner + ' wins with ' + str(degrees) + ' degree/s of success')
    await ctx.send(attacker_string)
    await ctx.send(defender_string)
    await ctx.send(result_string)
bot.run(TOKEN)
