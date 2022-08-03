import discord
from discord.ext import commands
import asyncio
import json

pingr = commands.Bot(command_prefix="_", help_command=None)

# full credits of this code goes to Geb#1337

with open("config.json") as f:
    geb = json.load(f)
with open("config.json") as f:
    guildid = int(geb["spam_guild_id"])
    roleid = geb["ping_role_id"]
    bottoken = geb["bot_token"]

async def ping_task():
    while True:
        guild = pingr.get_guild(guildid)
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                if channel.name.startswith('ping'):
                    await channel.send(f"<@&{roleid}>")
                    await asyncio.sleep(0.1)
                else:
                    pass
                  
@pingr.event
async def on_ready():
    pingr.loop.create_task(ping_task())

@pingr.slash_command(guild_ids=[guildid])
async def ping(ctx):
    await ctx.respond(f"{round(pingr.latency * 1000)}ms")


pingr.run(bottoken)
