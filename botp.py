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
    await ctx.send("heh" * count_heh)

@bot.command()
async def hah(ctx, count_hah = 5):
    await ctx.send("hah" * count_hah)

@bot.command()
async def hooh(ctx, count_hooh = 5):
    await ctx.send("hooh" * count_hooh)

@bot.command()
async def xixi(ctx, count_xixi = 5):
    await ctx.send("xixi" * count_xixi)

bot.run("Your Client Bot(token)")

