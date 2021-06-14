import discord
import time
import asyncio

intents = discord.Intents.all()
client = commands.AutoShardedBot(
    shard_count=2,
    command_prefix= "bl!",
    description='Definetly a proper bot description',
    owner_id=(394506589350002688),
    case_insensitive=True,
    intents=intents
    )

token = "token"

all_available_cogs = []

@client.event
async def on_ready():
    print('Logged in as: {}'.format(client.user))
    print('User ID: {}'.format(client.user.id))
    print(f'Created At: {client.user.created_at}')
    print(f'Current Time: {stTimeFormatted}')
    print("Servers I'm in: " + str(len(client.guilds)))
    print("~ ~ ~ ~ ~ ~")
    async for guild in client.fetch_guilds(limit=150):
        try:
            print(f"- {guild.name} - {guild.id}")
        except:
            print(f"- - {guild.id}")
    print("~ ~ ~ ~ ~ ~")
    print("Now we're ready!")
    if len(all_available_cogs) != 0:
        for cog in all_available_cogs:
            try:
                client.load_extension(f"cogs.{cog}")
                print(f"Loaded cogs.{cog}")
            except:
                try:
                    client.unload_extension(f"cogs.{cog}")
                    client.load_extension(f"cogs.{cog}")
                    print(f"Loaded cogs.{cog}")
                except Exception as e:
                    print(f"Exception occured loading cogs.{cog}:\n{str(e)}")

client.run(token)
