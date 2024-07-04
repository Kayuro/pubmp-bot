from watermark import *

import pystyle
import discord
from discord.ext import commands

import json
import time

def pubmp(token, link, message):
    print(f'{pystyle.Colors.cyan}')

    bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
    discord.Intents.all().presences = True

    @bot.event
    async def on_ready():
        print(f'\n{pystyle.Colors.dark_green}{bot.user} {pystyle.Colors.light_green}est prêt !')
        try:
            await bot.tree.sync()
        except Exception as e:
            print(e)
    
    @bot.event
    async def on_guild_join(guild):
        print('')
        for member in guild.members:
            try:
                await member.send(f'{message}\n\n{link}')
                print(f'{pystyle.Colors.light_blue}Message envoyé à {member}')
            except:
                print(f'{pystyle.Colors.light_red}Message non envoyé à {member}')
            time.sleep(0.25)
            
        await guild.leave()

    @bot.tree.command(name='pub', description= 'Lancez-le')
    async def pub(
    interaction: discord.Interaction,
    ):
        print('')
        for member in interaction.guild.members:
            try:
                await member.send(f'{message}\n\n{link}')
                print(f'{pystyle.Colors.light_blue}Message envoyé à {member}')
            except:
                print(f'{pystyle.Colors.light_red}Message non envoyé à {member}')
            time.sleep(0.25)
            
        await interaction.guild.leave()

    bot.run(token)

if __name__ == '__main__':
    __config__ = json.load(open('config.json', 'r'))

    token = __config__['token']
    link = __config__['lien']
    message = __config__['message']

    try:
        pubmp(token, link, message)
    except Exception as error:
        print(f'\n{pystyle.Colors.red}{error}')
        print(f'\n{pystyle.Colors.gray}Le programme va se fermer')
        time.sleep(5)
