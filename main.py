import asyncio
import json
import time

import discord
from discord.ext import commands
from watermark import *
import pystyle

def pubmp(token, link, message):
    print(f'{pystyle.Colors.cyan}')

    intents = discord.Intents.all()
    intents.presences = True

    bot = commands.Bot(command_prefix=".", intents=intents)
    semaphore = asyncio.Semaphore(1)

    @bot.event
    async def on_ready():
        bot_id = bot.user.id
        invite_link = f"https://discord.com/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot%20applications.commands"
        print(f'\n{pystyle.Colors.dark_green}{bot.user} {pystyle.Colors.light_green}est prêt !')
        print(f'{pystyle.Colors.yellow}🔗 Lien d\'invitation du bot : {invite_link}')
        try:
            await bot.tree.sync()
        except Exception as e:
            print(f'{pystyle.Colors.red}Erreur lors de la synchronisation des commandes : {e}')
    
    async def send_message(member, msg, link):
        async with semaphore:
            formatted_message = msg.replace("{user}", member.mention)
            try:
                await member.send(f'{formatted_message}\n\n{link}')
                print(f'{pystyle.Colors.light_blue}Message envoyé à {member}')
            except:
                print(f'{pystyle.Colors.light_red}Message non envoyé à {member}')
            await asyncio.sleep(0.6)

    async def send_messages_to_all(members, msg, link):
        tasks = [send_message(member, msg, link) for member in members if not member.bot]
        await asyncio.gather(*tasks)
        print(f'{pystyle.Colors.green}✅ Tous les messages ont été envoyés !')

    @bot.event
    async def on_guild_join(guild):
        print(f'{pystyle.Colors.light_green}Rejoint le serveur : {guild.name}')
        await send_messages_to_all(guild.members, message, link)
        await guild.leave()
        print(f'{pystyle.Colors.red}❌ Quitte le serveur : {guild.name}')

    @bot.tree.command(name='pub', description='Lancez le pub-mp')
    async def pub(interaction: discord.Interaction):
        print(f'{pystyle.Colors.light_blue}Commande /pub exécutée')
        await send_messages_to_all(interaction.guild.members, message, link)
        await interaction.guild.leave()
        print(f'{pystyle.Colors.red}❌ Quitte le serveur : {interaction.guild.name}')

    bot.run(token)

if __name__ == '__main__':
    with open('config.json', 'r', encoding='utf-8') as file:
        __config__ = json.load(file)

    token = __config__['token']
    link = __config__['lien']
    message = __config__['message']

    try:
        pubmp(token, link, message)
    except Exception as error:
        print(f'\n{pystyle.Colors.red}Erreur : {error}')
        print(f'\n{pystyle.Colors.gray}Le programme va se fermer dans 5 secondes...')
        time.sleep(5)
