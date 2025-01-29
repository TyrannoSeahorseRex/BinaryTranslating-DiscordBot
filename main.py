import discord
from discord import app_commands
import discord.ext
from discord.ext import tasks

####################################################################################################################################################################################
## CLIENT
####################################################################################################################################################################################

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents= discord.Intents.all())
        self.synced = False
        self.added = False
        self.activity_index = 0
        self.activities = [
            discord.Game(name=f"Convert to Binary"), 
            discord.Game(name=f"73 is 1001001"), 
            discord.Game(name=f"I luv Binary"), 
            discord.Game(name=f"Binary is Cooool"),
            discord.Game(name=f"/text_to_binary")
            ]

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        if not self.added:
            self.added = True
        print(f"We have logged in as User: {self.user}. ID: {self.user.id}.")
        await self.activity_change_loop.start()
