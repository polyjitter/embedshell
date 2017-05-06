print("Starting up...\n")

import discord
from discord.ext import commands
print("imports finalized.\n")

bot = commands.Bot(command_prefix='embed!', 
                   description='Wrapped up EmbedShell', 
                   self_bot=True)
print("bot created.\n")

startup_extensions=['embedshell']

print("globals created.\n")

bot.get_command("help").hidden = True

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')        

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

print("Logging in...")
bot.run('**USERTOKEN**', 
        bot=False)