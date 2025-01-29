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

    @tasks.loop(seconds=10.0)
    async def activity_change_loop(self):
        self.activity_index = (self.activity_index + 1) % len(self.activities)
        await self.change_presence(activity=self.activities[self.activity_index])
        
    @activity_change_loop.before_loop
    async def before_activity_change_loop(self):
        await self.wait_until_ready()
        self.activities = [discord.Game(name=f"{len(self.guilds)} servers")] + self.activities

client = aclient()
tree = app_commands.CommandTree(client)

####################################################################################################################################################################################
## TEXT TO BINARY COMMAND
####################################################################################################################################################################################

@tree.command(name="text_to_binary", description="Translate text to binary!")
@app_commands.describe(text = "Text you want to translate.")
async def text_to_binary(interaction: discord.Interaction, text: str):
  message = text
  binary = " ".join(format(ord(c), "b") for c in message)
  await interaction.response.send_message(f"Hi {interaction.user.mention}. Your message `'{text}'` in binary is: `{binary}`", ephemeral=True)
  try: 
      await interaction.user.create_dm()
      await interaction.user.dm_channel.send(f"Hi {interaction.user.mention}. Your message `'{text}'` in binary is: `{binary}`")
      await interaction.user.dm_channel.send("https://tenor.com/view/openbsd-puffy-binary-gif-22717840")
  except: pass

####################################################################################################################################################################################
## RUN 
####################################################################################################################################################################################

TOKEN = 'ENTER YOUR TOKEN HERE'
client.run(TOKEN)
