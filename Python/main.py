import discord
from discord.ext import commands

Token = "MTEyODI5MjE1MDE3ODc1NDU5MQ.GQoS7O.nlIb8OVD8ltyc8Irf2-QtVPdLi8eLsAKleFrS4"

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Привет")

bot.run("MTA2MTYyMjk3MDkwNjMxNjgyMA.GvIaHH.yhClnsRsra54lR8WB87QvVyBXsXeiq2zZHRa0M")