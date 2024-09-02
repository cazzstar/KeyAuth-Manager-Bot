import discord, os, sys
from discord import Option
from functions import *
import json



config = json.load(open("config.json", encoding="utf-8"))


def load_apps():
    
    apps = json.load(open("apps.json", encoding="utf-8"))
    applications = []
    for app in apps:
        applications.append(app)
        
    return applications

activity = discord.Activity(type=discord.ActivityType.watching, name = "#1 public")
bot = discord.Bot(command_prefix = ">", intents = discord.Intents.all(), activity = activity)


# Terminal Print
@bot.event
async def on_ready():
    print()
    print(f"[+] {bot.user} is online.")
    print(f" Code Returned 500 : Success")


@bot.slash_command(guild_ids = [config["guildID"]], name="addapp", description="Add an application.")
async def addapp(ctx, sellerkey: Option(str, "Keyauth application seller key", required = True)):
    
    if ctx.author.id not in config["whitelist"]:
        return await ctx.respond(embed = discord.Embed(description = f"You don't have permission to use this comamnd.", color = 0xFF0000))

    apps = json.load(open("apps.json", encoding="utf-8"))
    appName = app_info(sellerkey)
    if appName != False:
        data = {appName : sellerkey}
        
        apps.update(data)
        with open("apps.json", "w") as appdatafile:
            json.dump(apps, appdatafile, indent=4)

        await ctx.respond(embed = discord.Embed(description = f"Added `{appName}` to the database.", color = 0x4598d2))
    
    else:
        await ctx.respond(embed = discord.Embed(description = f"Failed to add `{appName}` to the database.", color = 0xFF0000))

    

    
# HWID Reset Command
@bot.slash_command(guild_ids = [config["guildID"]], name="hwidreset", description="Reset HWID of a user.")
async def hwidreset(ctx, application: Option(str, "Choose an application", choices = load_apps(), required = True), user: Option(str, "Keyauth username.", required = True)):
    
    if ctx.author.id not in config["whitelist"]:
        return await ctx.respond(embed = discord.Embed(description = f"You don't have permission to use this comamnd.", color = 0xFF0000))
    
    sellerkey = json.load(open("apps.json", encoding="utf-8"))[application]
    message = reset_hwid(user, sellerkey)
    
    return await ctx.respond(embed = discord.Embed(description = message, color = 0x4598d2))





# Restart Command
@bot.slash_command(guild_ids = [config["guildID"]], name="restart", description="Restarts the bot.")
async def restart(ctx):
    await ctx.respond(embed = discord.Embed(description = "Succesfully Restarted Modules.", color = 0x4598d2))
    os.execv(sys.executable, ['python'] + sys.argv)



# Download Loader Command    
@bot.slash_command(guild_ids = [config["guildID"]], name="download", description="Sends the loader")
async def download(ctx):
    await ctx.respond(embed = discord.Embed(description = "[Click me to download](https://cdn.discordapp.com/attachments/1167845168288911571/1180772148948775013/odysseyapi.exe?ex=65bf3c41&is=65acc741&hm=e300575da1374131c7247fcc7e4a0cb4d7fb7b3b861aa668b99c1cdebd408c1c&)", color = 0x4598d2)) 




# Debug Logs
@bot.slash_command(guild_ids = [config["guildID"]], name="debug", description="Sends the latest debug logs to the user")
async def debug(ctx):
    await ctx.respond(embed = discord.Embed(description = "Sent debug logs from terminal to 1167646329644789861.", color = 0x4598d2))





# Instructions Command
@bot.slash_command(guild_ids = [config["guildID"]], name="instructions", description="Sends the latest instructions.")
async def instructions(ctx):
    await ctx.respond(embed = discord.Embed(description = "Soon.", color = 0x4598d2))





# Fetch Error Commmmand
@bot.slash_command(guild_ids = [config["guildID"]], name="fetcherror", description="Fetches the latest terminal error.")
async def fetcherror(ctx):
    await ctx.respond(embed = discord.Embed(description = "[433] Cannot find error codes in terminal.", color = 0x4598d2))



bot.run(config['token'])
