import discord
import random
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

#Moderation part
@bot.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="no reason provided."
    await ctx.guild.kick(member)
    await ctx.send(f"User {member.mention} has been kicked for {reason}")


class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=883450960784011275))
        self.synced = True
        print("Bot Is Online")

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="ping", description="Ping the user", guild=discord.Object(id=883450960784011275))
async def self(interation: discord.Interaction):
    await interation.response.send_message(f"umu!")

@tree.command(name="eightball", description="gives you an answer", guild=discord.Object(id=883450960784011275))
async def self(interation: discord.Interaction, question:str):
    responses = ["As i see it, yes.", "Ask later again.", "Better not tell you now.", "Cannot predict now", "Concentrate and ask again.", "UMU!"
                 "Don't count on it.", "It is certain.", "Most likely."]
    await interation.response.send_message(f"**Question: **{question}\n**Answer: ** {random.choice(responses)}")


#Starup, token should be hidden but PCP is dumb
bot.run("MTA0MDQwMTUxMDMwNTEwODA2OQ.G5XPMp.f4Qgzqf_ppWGkk_Z9XCvGg-7HkETpLTPN4B3_U")

