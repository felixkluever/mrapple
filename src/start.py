import discord
import os
from dotenv import load_dotenv
import shower

load_dotenv()

KEY = os.getenv("DISCORD_KEY")

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith("!shower") or message.content.startswith("!showered"):
            await message.channel.send(shower.showered(message.author))

        if message.content.startswith("!leaderboard") or message.content.startswith("!lb"):
            await message.channel.send(shower.leaderboard())

        

    client.run(KEY)

if (__name__ == "__main__"):
    main()