import discord
from discord.ext import commands
import asyncio

pingr = commands.Bot(command_prefix="_", help_command=None)

# full credits of this code goes to Geb#1337
# working versions of this bot can be found in https://discord.gg/pings

spam_guild = #put guild id here
ping_role = #put role id here

async def ping_task():
    while True:
        guild = pingr.get_guild(spam_guild)
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                if channel.name.startswith('ping'):
                    await channel.send(f"<@&{ping_role}>")
                    await asyncio.sleep(1)
                else:
                    pass
                  
@pingr.event
async def on_ready():
    pingr.loop.create_task(ping_task())

@pingr.slash_command(guild_ids=[spam_guild])
async def ping(ctx):
    await ctx.respond(f"{round(pingr.latency * 1000)}ms")


#paste token below
pingr.run("")
