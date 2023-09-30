import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bro(ctx):
    await ctx.send(f'bro! {bot.user}, how are you?')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE1NzU4NjU2NDU0MTU4MzQxMA.GxLatV.4xsEr5p4HPtTQgGG890A7VHvjwgJ57TOxAGK6Q")