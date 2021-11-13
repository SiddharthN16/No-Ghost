import serial
import time
import discord
import asyncio
from datetime import datetime
from plyer import notification
from dotenv import load_dotenv
import os


def msgOutput(message):
    now = datetime.now()
    currTime = now.strftime("%H:%M:%S")

    with open("log.txt", 'a') as output:
        output.write(
            f"{message.author.name}#{message.author.discriminator} Sent a Message at {currTime}.\n")


def noGhost():
    client = discord.Client()

    # Get Discord Token from .env file
    load_dotenv()
    token = os.environ.get('DISCORD_TOKEN')

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user} (ID: {client.user.id})")
        print("------")

    @ client.event
    async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author.id == client.user.id:
            return

        name = str(client.user).split("#")[0]
        response = f'***{name} is currently AFK, and cannot respond to your message. {name} will be notified of your message when they return. Thank You! (This message is created by a BOT, not {name})***'

        for user in message.mentions:  # If there are multiple mentions in message, search for client user
            # DMS
            if (user == client.user and message.guild == None):
                print("received")
                msg = await message.reply(response, mention_author=True)

                msgOutput(message)

                await asyncio.sleep(1.0)

                for i in range(10):
                    await msg.edit(content=f"{response} *Deleting in {10-i}...*")
                    await asyncio.sleep(0.5)

                await msg.delete()
        client.run(token)


noGhost()

arduino = serial.Serial('COM14', 9600)
while True:

    while True:
        incoming = arduino.readline()
        onState = int(incoming.decode('ascii'))

        if (onState == 1):
            noGhost()
        else:
            with open("log.txt", "r") as content:
                messageList = content.read()

            notification.notify(
                title="NoGhost: Misses Notifications",
                message=messageList,
                app_icon="assets\icon.icon.ico",
                timeout=5
            )

            with open("log.txt", "w") as reset:
                reset.write("")

            break
