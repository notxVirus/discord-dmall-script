import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

owners = [1,2,3,4,5] # https://github.com/notxVirus

@client.event # https://github.com/notxVirus
async def on_ready():
	print(f"Logged in as {client.user}") # https://github.com/notxVirus

@client.command() # https://github.com/notxVirus
async def dmall(ctx, *, message):
	if ctx.author.id in owners:
		for member in ctx.guild.members:
			try:
				await member.send(message)
				print(f"Sent message to {member} ({member.id})")
			except:
				print(f"Failed to dm to {member} ({member.id})")

@client.command() # https://github.com/notxVirus
async def fetch(ctx): # https://github.com/notxVirus
	if ctx.author.id in owners:
		members = ctx.guild.members
		non_offline_members = [member for member in ctx.guild.members if member.status != discord.Status.offline]
		non_offline_member_ids = [member.id for member in non_offline_members]

		with open("users.txt", "w") as file:
			file.write("\n".join(str(id) for id in non_offline_member_ids))

		await ctx.send(f"Fetched `{len(non_offline_member_ids)}` users successfully")

		with open("users.txt", "r") as file:
			user_ids = [int(line.strip()) for line in file]

		print(user_ids)

@client.command(aliases = ['dmall_online', 'online_dmall']) # https://github.com/notxVirus
async def online(ctx, *, message):
	if ctx.author.id in owners:
		users = []

		try:
			with open("users.txt", "r") as file:
				user_ids = [int(line.strip()) for line in file]
		except:
			await ctx.send("Error. Please, use `!fetch` command.")

		for user in user_ids:
			try:
				member = client.get_user(user)
				await member.send(message)
				print(f"Sent message to {member} ({member.id})")
			except:
				print(f"Failed to dm to {member} ({member.id})")

client.run("YOUR DISCORD BOT TOKEN") # https://github.com/notxVirus