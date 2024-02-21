
ilist = []


style = '''
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #1e1e24;
        margin: 10px 0 0 0; /* Changed margin-top to 10px */
        padding: 0;
        font-family: "Roboto", sans-serif;
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    .chat-header {
        text-align: center;
        margin-bottom: 20px;
    }
    .chat-title {
        font-size: 36px;
        color: #fff;
        margin: 0;
    }
    .chat-description {
        color: #8e8ea1;
        font-size: 18px;
        margin-top: 10px;
    }
    .message {
        background-color: #292a31;
        border-radius: 15px;
        margin: 10px 0;
        padding: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.5s ease-in-out;
    }
    .timestamp {
        color: #72767d;
        font-size: 12px;
    }
    .author {
        font-weight: bold;
        color: #8e8ea1;
        margin-right: 10px;
    }
    .content {
        color: #ccc;
        font-size: 16px;
        line-height: 1.4;
        margin-top: 5px;
    }
    .additional-info {
        color: #72767d;
        font-size: 14px;
        margin-top: 20px;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
</head>
<body>
'''

#Config And Settings --------------------




try:
    import os
except ImportError:
    print(Fore.RED + "Error: You must do the command \"pip install os\" in the command line")
    sys.exit(1)
os.system("title Discord Bot by Lmao4745")

try:
    import discord
    from discord.ext import commands
    from discord import ui
    from discord.ext import tasks
    from discord import app_commands
except ImportError:
    os.system("pip install discord")
    os.system("pip install discord.py")
    import discord
    from discord.ext import commands
    from discord import ui
    from discord.ext import tasks
    from discord import app_commands

try:
    import tracemalloc
except ImportError:
    os.system("pip install tracemalloc")
    import tracemalloc

try:
    from datetime import datetime, timedelta, timezone
except ImportError:
    os.system("pip install datetime")
    from datetime import datetime, timedelta, timezone

try:
    import json
except ImportError:
    os.system("pip install json")
    import json

try:
    from PIL import Image
except ImportError:
    os.system("pip install pillow")
    from PIL import Image

try:
    from colorama import Fore, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, init
try:
    import logging
except ImportError:
    os.system("pip install logging")
    import logging

try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

import string
import random
import fivem_client
import time
import sys
import asyncio

# Libraries Systems --------------------------


#switch case
class SwitchCase:
    class Switch:
        mylist = []

        def __init__(self, casee):
            SwitchCase.Switch.mylist.append(casee)

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_value, traceback):
            SwitchCase.Switch.mylist.clear()

    class Case:
        def __init__(self, check):
            self.true = SwitchCase.Switch.mylist[0] == check
            self.false = SwitchCase.Switch.mylist[0] != check
    class DictCase:
        def __init__(self, check):
            SwitchCase.Switch.mylist.remove[0]
            self.true = dict(SwitchCase.Switch.mylist[0])[check] == "True"
            self.false = dict(SwitchCase.Switch.mylist[0])[check] == "False"

switch = SwitchCase.Switch
case = SwitchCase.Case
dictcase = SwitchCase.DictCase

def sort_and_select_max(*args, n=None):
    sorted_numbers = sorted(args, reverse=True)
    if n is not None:
        return sorted_numbers[:n]
    else:
        return sorted_numbers




def close():
    os.system("TASKKILL /F /PID %s" % os.getpid())


logging.basicConfig(level=logging.WARNING)
logging.getLogger("discord").setLevel(logging.WARNING)
logging.getLogger("discord.http").setLevel(logging.WARNING)
logging.getLogger("discord.gateway").setLevel(logging.WARNING)
logging.getLogger("discord.client").setLevel(logging.WARNING)
logging.getLogger("Requirement already satisfied:").setLevel(logging.WARNING)

#Console Hide --------------------------
def error(text):
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.RED} Error: {Fore.LIGHTRED_EX}{text}")
def acc(text):
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.LIGHTCYAN_EX} {text}")



def read_text_file_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            text_data = file.read()
            data_dict = json.loads(text_data)
            return data_dict
    except FileNotFoundError:
        error(f"The file '{file_path}' does not exist.")
        return {}
    except json.JSONDecodeError:
        error(f"An error occurred while reading the file '{file_path}'. The file is not valid JSON.")
        return {}
    except Exception as e:
        error(f"An error occurred: {str(e)}")
        return {}


def read_value_from_text_file(file_path, key, closee=None, errorcmd=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)

        if key in data_dict:
            return data_dict[key]
        else:
            if errorcmd is None:
                error(f"Key '{key}' not found in the dictionary.")
            return None
    except FileNotFoundError:
        if errorcmd is None:
            error(f"The file '{file_path}' does not exist.")
        if closee is None:
            close()
        return None
    except json.JSONDecodeError:
        error(f"An error occurred while reading the file '{file_path}'. The file is not valid JSON.")
        close()
        return None
    except Exception as e:
        error(f"An error occurred: {str(e)}")
        close()
        return None


def create_text_file(file_path):
    try:
        existing_data = {}
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
                acc(f"Data has been created in the file '{file_path}'")
    except Exception as e:
        error(f"An error occurred while saving to the file '{file_path}': \n{str(e)}")
        


def update_text_file(file_path, new_key, new_value, input=None):
    try:
        existing_data = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}

        existing_data.update({new_key: new_value})

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
            if input is None:
                acc(f"Data has been saved in the file '{file_path}'")
    except Exception as e:
        error(f"An error occurred while saving to the file '{file_path}': \n{str(e)}")


def add_data_text_file(file_path, new_key, new_value):
    try:
        existing_data = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}
        if new_key not in existing_data:
            existing_data.update({new_key: new_value})

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
                acc(f"Data has been saved in the file '{file_path}'")
    except Exception as e:
        error(f"An error occurred while saving to the file '{file_path}': \n{str(e)}")


def delete_data_or_category(json_file, category_name):
    try:
        with open(json_file, 'r') as json_filee:
            data = json.load(json_filee)
    except FileNotFoundError:
        return

    if category_name in data:
        del data[category_name]

        with open(json_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

def create_or_update_category(json_file, category_name):
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as json_filee:
            data = json.load(json_filee)
    else:
        data = {}
    
    if category_name not in data:
        data[category_name] = {}
    
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_subdata_to_category(json_filee, category_name, subdata_name, subdata_value):
    try:
        with open(json_filee, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}
    
    if category_name not in data:
        data[category_name] = {}
    
    if subdata_name not in data[category_name]:
        data[category_name][subdata_name] = subdata_value
    
    with open(json_filee, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def delete_subdata_from_category(json_filee, category_name, subdata_name):
    try:
        with open(json_filee, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return
    
    if category_name in data and subdata_name in data[category_name]:
        del data[category_name][subdata_name]
        
        with open(json_filee, 'w') as json_file:
            json.dump(data, json_file, indent=4)


def read_subdata_from_json(file_path, main_key, subdata_key, message=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)

        if main_key in data_dict and subdata_key in data_dict[main_key]:
            return data_dict[main_key][subdata_key]
        else:
            if message is True:
                error(f"Main key '{main_key}' or subdata key '{subdata_key}' not found in the dictionary.")
            return None
    except FileNotFoundError:
        error(f"The file '{file_path}' does not exist.")
        return None
    except json.JSONDecodeError:
        error(f"An error occurred while reading the file '{file_path}'. The file is not valid JSON.")
        return None
    except Exception as e:
        error(f"An error occurred: \n{str(e)}")
        return None

def update_subdata(json_file, category_name, subdata_to_update, new_value):
    try:
        with open(json_file, 'r') as json_filee:
            data = json.load(json_filee)
    except FileNotFoundError:
        pass

    if category_name in data and subdata_to_update in data[category_name]:
        data[category_name][subdata_to_update] = new_value

        with open(json_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return

def read_category_data(file_path, category_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)

        if category_name in data_dict:
            return data_dict[category_name]
        else:
            error(f"Category '{category_name}' not found in the dictionary.")
            return None
    except FileNotFoundError:
        error(f"The file '{file_path}' does not exist.")
        return None
    except json.JSONDecodeError:
        error(f"An error occurred while reading the file '{file_path}'. The file is not valid JSON.")
        return None
    except Exception as e:
        error(f"An error occurred: \n{str(e)}")
        return None



# Example usage:
file_path = "data.json"  # Change this to the path of the file you want to update
data_to_add_or_update = {"new_key": "new_value"}  # New data to add or update

#Global Functions -----------------------










init(autoreset=True)

def load_config():
    if not os.path.exists("bot"):
        os.mkdir("bot")
    create_text_file("bot\\botconfig.json")
    bottoken = read_value_from_text_file("bot\\botconfig.json", "bottoken")
    botprefix = read_value_from_text_file("bot\\botconfig.json", "botprefix")
    guildid = read_value_from_text_file("bot\\botconfig.json", "guildid")
    guildname = read_value_from_text_file("bot\\botconfig.json", "guildname")
    guildiconlink = read_value_from_text_file("bot\\botconfig.json", "guildiconlink")
    BotOwner = read_value_from_text_file("bot\\botconfig.json", "BotOwner")

    if bottoken is None:
        bottoken = input("Your bot's token: ")
        update_text_file("bot\\botconfig.json", "bottoken", f"{bottoken}")
    ilist.append(bottoken)
    #0

    if botprefix is None:
        botprefix = input("Your bot's prefix: ")
        update_text_file("bot\\botconfig.json", "botprefix", f"{botprefix}")
    ilist.append(botprefix)
    #1

    if guildid is None:
        guildid = input("Your bot's Guild ID: ")
        update_text_file("bot\\botconfig.json", "guildid", f"{guildid}")
    ilist.append(int(guildid))
    #2

    if guildname is None:
        guildname = input("Your bot's Guild Name: ")
        update_text_file("bot\\botconfig.json", "guildname", f"{guildname}")
    ilist.append(guildname)
    #3

    if guildiconlink is None:
        guildiconlink = input("Your bot's Guild Icon Link: ")
        update_text_file("bot\\botconfig.json", "guildiconlink", f"{guildiconlink}")
    ilist.append(guildiconlink)
    #4

    if BotOwner is None:
        BotOwner = input("Your Server OwnerShip: ")
        update_text_file("bot\\botconfig.json", "BotOwner", f"{BotOwner}")
    ilist.append(BotOwner)
    #5

    if not os.path.exists("SystemDB"):
        os.mkdir("SystemDB")
load_config()
servername = ilist[3]
servericon = ilist[4]

#Load Configs --------------------

#Configg
def system_config():
    if not os.path.exists("bot\\emojis.json"):
        create_text_file("bot\\emojis.json")
    if not os.path.exists("bot\\system_config.json"):
        file = "bot\\system_config.json"
        create_text_file(file)
        create_or_update_category(file, "config")
        add_subdata_to_category(file, "config", "Welcome", "False")
        add_subdata_to_category(file, "config", "Welcome-Channel", "0")
        add_subdata_to_category(file, "config", "Verify", "False")
        add_subdata_to_category(file, "config", "Verify-AntiAlt", "False")
        add_subdata_to_category(file, "config", "Verify-Captcha", "False")
        add_subdata_to_category(file, "config", "Verify-Channel", "0")
        add_subdata_to_category(file, "config", "Verify-Role", "0")
        add_subdata_to_category(file, "config", "Ticket", "False")
        add_subdata_to_category(file, "config", "Ticket-Category", "0")
        add_subdata_to_category(file, "config", "Ticket-StaffRoleID", "0")
        add_subdata_to_category(file, "config", "Ticket-Channel", "0")
        add_subdata_to_category(file, "config", "BanList", "False")
        add_subdata_to_category(file, "config", "AutoRole", "False")
        add_subdata_to_category(file, "config", "AutoRole-Role", "0")


system_config()



def ticketset():
    ticketcategoryid = read_subdata_from_json("bot\\system_config.json", "config", "Ticket-Category")
    ticketroleid = read_subdata_from_json("bot\\system_config.json", "config", "Ticket-StaffRoleID")
    listt = [ticketcategoryid, ticketroleid]
    return listt






number = 0
id = None
# 1 = role Error
# 2 = guild error
# 3 = user error

def role_id_check(role_id):
    def action(ctx):
        global number
        global id
        role = discord.utils.get(ctx.author.roles, id=role_id)
        id = role_id
        if role is not None and role in ctx.author.roles:
            return True
        else:
            number = 1
            return False
    return commands.check(action)


def role_name_check(role_name):
    def action(ctx):
        global number
        global id
        role = discord.utils.get(ctx.author.roles, id=role_name)
        id = role.id
        if role is not None and role in ctx.author.roles:
            return True
        else:
            number = 1
            return False
    return commands.check(action)


def guild_check(guild_id):
    def action(ctx):
        global number
        global id
        id = guild_id
        guild = bot.get_guild(guild_id)
        if ctx.guild == guild:
            return True
        else:
            number = 2
            return False
    return commands.check(action)


def is_member(member_id):
    def action(ctx):
        global number
        global id
        id = member_id
        if ctx.author.id == member_id:
            return True
        else:
            number = 3
            return False
    return commands.check(action)

async def log_check(limit=None, time=None):
    if limit is None:
        limitt = 1
    if time is None:
        time = False
    async for entry in guild.audit_logs(limit=limitt, oldest_first=time):
        pass
    return entry

def inter_member(member_id):
    def action(interaction):
        if interaction.user.id == member_id:
            return True
        else:
            return False
    return commands.check(action)





async def add_emoji_to_server(EmojiFile, EmojiName):
    emoji = discord.utils.get(guild.emojis, name=f"{EmojiName}")
    if not emoji:
        with open(f"{EmojiFile}", 'rb') as file:
            emoji_bytes = file.read()
            file.close()

        emoji_data = {
            'name': f"{EmojiName}",
            'image': emoji_bytes
        }
        emoji = await guild.create_custom_emoji(**emoji_data)
        if not os.path.exists("bot\\emojis.json"):
            create_text_file("bot\\emojis.json")
        delete_data_or_category("bot\\emojis.json", f"{EmojiName}")
        update_text_file("bot\\emojis.json", f"{EmojiName}", f"{str(emoji)}")
        await asyncio.sleep(2)
        return
    
    
    
    
        


def read_emojis():
    try:
        emojisValue = read_text_file_to_dict("bot\\emojis.json")
        return emojisValue
    except:
        pass

async def def_category():
    categoryDef = discord.utils.get(guild.categories, name="〈⚙〉management-category")
    if not categoryDef:
        await guild.create_category(name="〈⚙〉management-category")
        acc(f"Def category Created")

    categoryDef = discord.utils.get(guild.categories, name="〈⚙〉management-category")
    return categoryDef

async def emoji_ui(image_path=None):
    categoryBot = await def_category()
    Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
    if not Imagem:
        Imagem = await guild.create_text_channel(name="〈💍〉bot-messages", category=categoryBot)
        await Imagem.set_permissions(guild.default_role, view_channel=False, send_messages=False)
    Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
    if image_path is not None:
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_system = messageurl.attachments[0].url
        return image_system

async def check_category(namee, ConsoleName):
    category = discord.utils.get(guild.categories, name=f"{namee}")
    if category:
        pass
    if not category:
        await guild.create_category(name=f"{namee}")
        acc(f"category {ConsoleName} Created {Fore.WHITE}")
    category = discord.utils.get(guild.categories, name=f"{namee}")
    return category



async def check_channel(namee, ConsoleName, CategoryName=None, hide=bool):
        channel = discord.utils.get(guild.channels, name=f"{namee}")
        category = discord.utils.get(guild.categories, name=f"{CategoryName}")
        if channel:
            pass
        if not channel:
            channel = await guild.create_text_channel(name=f"{namee}", category=category)
            if hide is not False:
                await channel.set_permissions(guild.default_role, view_channel=False, send_messages=False)
            acc(f"{ConsoleName} Created")
        channel = discord.utils.get(guild.channels, name=f"{namee}")
        return channel



#Bot Functions -----------------------


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=f"{ilist[1]}", intents=discord.Intents.all())
bot = Bot()
tracemalloc.start()

@bot.event
async def on_ready():
    global guild
    guild = bot.get_guild(ilist[2])
    await def_category()
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.LIGHTYELLOW_EX} All actions have been loaded")
    time.sleep(0.200)
    verify = read_subdata_from_json("bot\\system_config.json", "config", "Verify")
    if verify == "True":
        antialt = read_subdata_from_json("bot\\system_config.json", "config", "Verify-AntiAlt")
        CAPTCHAProtecion = read_subdata_from_json("bot\\system_config.json", "config", "Verify-Captcha")
        role = read_subdata_from_json("bot\\system_config.json", "config", "Verify-Role")
        channel = read_subdata_from_json("bot\\system_config.json", "config", "Verify-Channel")
        if antialt == "False":
            antialt = False
        else:
            antialt = True
        if CAPTCHAProtecion == "False":
            CAPTCHAProtecion = False
        else:
            CAPTCHAProtecion = True
        try:
            await AutoSystems.VerifySystemC.VerifySystem(int(channel), int(role), None, antialt, CAPTCHAProtecion)
        except:
            error(f"Verify System\n{e}")
            await asyncio.sleep(3)
            os.system("start cmd.bat")
            close()
    ticket = read_subdata_from_json("bot\\system_config.json", "config", "Ticket")
    if ticket == "True":
        channelid = read_subdata_from_json("bot\\system_config.json", "config", "Ticket-Channel")
        await AutoSystems.Tickets.TicketSystem(int(channelid), None)
    banlist = read_subdata_from_json("bot\\system_config.json", "config", "BanList")
    if banlist == "True":
        await AutoSystems.BanList.StartBanList(None)
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.CYAN} All settings have been loaded")
    time.sleep(0.200)
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.LIGHTMAGENTA_EX} Logged in as {bot.user.name}")
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        if "WARNING:discord.http" in str(e):
            error_message = f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}] {Fore.RED}Error: {Fore.LIGHTRED_EX}Cooldown from Discord Wait 10 seconds and the bot will return"
            error(f"{error_message}")
            await asyncio.sleep(10)
        else:
            print(e)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        if number == 2:
            error_message = f"The user does not have permission to execute the command on this server.\n{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}] {Fore.RED}Info: {Fore.LIGHTRED_EX}(GuildID: {id}, UserID: {ctx.author.id})"
            print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.RED} Command Error: {Fore.LIGHTRED_EX}{error_message}")
            return
        elif number == 1:
            error_message = f"User lacks the required role to proceed.\n{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}] {Fore.RED}Info: {Fore.LIGHTRED_EX}(RoleID: {id}, UserID: {ctx.author.id})"
            print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.RED} Command Error: {Fore.LIGHTRED_EX}{error_message}")
            return
        elif number == 3:
            error_message = f"The user does not have permission to execute the command.\n{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}] {Fore.RED}Info: {Fore.LIGHTRED_EX}(MemberOnlyID: {id}, UserID: {ctx.author.id})"
            print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.RED} Command Error: {Fore.LIGHTRED_EX}{error_message}")
            return
    print(error)


@bot.event
async def on_command_completion(ctx):
    acc(f"Command [{ctx.command.name}] completed successfully")

#Bot Systems ------------------------
Messages = []
bot_data = {}
cursingg = ["סארס", "סרטן", "אוטיסט", "זונה", "שרמוטה", "זדיין", "Palestine", "palestine", "הומו", "קוקסינל", "גיי"]
SPAM_THRESHOLD = 8 
SPAM_COOLDOWN = 3
AntiSpam = False
AntiSpamLog = False
last_execution_time = 0


def Rwords(num1=int, num2=int):
    letters_and_digits = string.ascii_letters + string.digits
    random_word = ''.join(random.choice(letters_and_digits) for _ in range(random.randint(num1, num2)))
    return random_word

def Rnum(num1=int, num2=int):
    numbers = random.randint(num1, num2)
    return numbers

emojisValues = read_emojis()
try:
    emojiiOpenTicket = emojisValues["openticket"]
    ServerRules = emojisValues["ServerRules"]
    Giveaway = emojisValues["Giveaway"]
    question = emojisValues["question"]
except:
    pass


class addmember(ui.Modal, title='Add a Member to the Ticket'):
    memberid = ui.TextInput(label="Member ID")
    

    async def on_submit(self, interaction: discord.Interaction):
        memberid = int(self.memberid.value)
        member = guild.get_member(memberid)
        channel = discord.utils.get(guild.channels, id=interaction.channel.id)
        await channel.set_permissions(member, read_messages=True, send_messages=True)
        embed=discord.Embed(title="Add Member", timestamp=datetime.now(), description=f"**{member.mention} Added To Ticket**", color=0x36FF33)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)

class deletemember(ui.Modal, title='Delete a Member to the Ticket'):
    memberid = ui.TextInput(label="Member ID")
    

    async def on_submit(self, interaction: discord.Interaction):
        memberid = int(self.memberid.value)
        member = guild.get_member(memberid)
        channel = discord.utils.get(guild.channels, id=interaction.channel.id)
        await channel.set_permissions(member, read_messages=False, send_messages=False)
        embed=discord.Embed(title="Remove Member", timestamp=datetime.now(), description=f"**{member.mention} Removed from the ticket**", color=0xff0000)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)

            

class rename(ui.Modal, title='Changing the name of the ticket'):
    name = ui.TextInput(label="New name")
    

    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel = discord.utils.get(guild.channels, id=interaction.channel.id)
            await interaction.response.send_message(f'The name change was successful\nThe name will change in 5 seconds', ephemeral=True)
            await asyncio.sleep(5)
            await channel.edit(name=f"{self.name}")
        except:
            pass





try:
    class selectmenus:
        class ticketselect(discord.ui.View):
            @discord.ui.select(
                placeholder = "select menu",
                min_values = 1,
                max_values = 1,
                options = [
                    discord.SelectOption(
                        label=f"question",
                        description=f"A user who wants to ask a question",
                        emoji=f"{question}"
                    ),
                    discord.SelectOption(
                        label=f"Report a user/staff team",
                        description=f"Report a user who has violated the server rules.",
                        emoji=f"{ServerRules}"
                    ),
                    discord.SelectOption(
                        label=f"Winning in a lottery",
                        description=f"Intended for users who have won a lottery on the server.",
                        emoji=f"{Giveaway}"
                    ),
                    discord.SelectOption(
                        label=f"Other",
                        description=f"Something else that is not in the category",
                        emoji=f"{emojiiOpenTicket}"
                    ),
                ]
            )
            async def select_callback(self, select, interaction: discord.Interaction,):
                emojilink = await emoji_ui("emojis\\openticket.png")
                ticset = ticketset()
                ticketchannel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if ticketchannel:
                    await select.response.send_message(f"You have an open ticket {ticketchannel.mention}", ephemeral = True)
                    return
                else:
                    user = discord.utils.get(guild.members, id=select.user.id)
                    staffrole = discord.utils.get(guild.roles, id=int(ticset[1]))
                    category = discord.utils.get(guild.categories, id=int(ticset[0]))
                    button = await AutoSystems.Tickets.Buttonss(staffrole)
                    if not staffrole:
                        return error(f"The server is missing a team role to continue")
                    if not category:
                        return error(f"Missing category to continue")
                    if interaction.values[0] == "Other":
                        class iddt(ui.Modal, title='Opening a ticket'):
                            reasonn = ui.TextInput(label="Type a reason for opening the ticket")
                            

                            async def on_submit(self, interaction: discord.Interaction):
                                await interaction.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                description = f"Username: {user.name}#{user.discriminator}\nID: {user.id}\nTicket Creation time: {datetime.now()}"
                                ticketchannel = await guild.create_text_channel(name=f"{user.id}-ticket", topic=description, category=category)
                                await ticketchannel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                                await ticketchannel.set_permissions(user, read_messages=True, send_messages=True)
                                await ticketchannel.set_permissions(staffrole, read_messages=True, send_messages=True)
                                message = await ticketchannel.send(f"{staffrole.mention} | {user.mention}")
                                await message.delete()
                                embeddd=discord.Embed(title="Ticket Tool", timestamp=datetime.now(), description=f"**{staffrole.mention}**\n__**ticket was opened by {user.mention}**__\n•** User Name: {user.name}#{user.discriminator}**\n•** User ID: {user.id}**\n\n__**General Information**__\n•** Ticket Creation time: ``{time.strftime(f'%d/%m/%Y, %H:%M:%S')}``**\n•** Reason: {self.reasonn.value}**\n•** __Thank you for contacting us, The staff team will contact you__**", color=0x00f5f1)
                                embeddd.set_author(name=f"{servername}", icon_url=f"{servericon}")
                                embeddd.set_thumbnail(url=emojilink)
                                embeddd.set_footer(text="© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
                                await ticketchannel.send(embed=embeddd, view=button)
                                    


                                channellogs = await AutoSystems.Tickets.OpenTicket.CreateTicketLogs("〈📋〉ticketlogs")
                                TicketLogsEmbed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is has been created\n``Information about the user - \n\nUser Name: {user.name}#{user.discriminator}\nUser ID: {user.id}\nTicket Creation time: {datetime.now()}\nReason: {self.reasonn.value}``**", color=0x33FFC7)
                                TicketLogsEmbed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                TicketLogsEmbed.set_thumbnail(url=f"{servericon}")
                                TicketLogsEmbed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
                                await channellogs.send(embed=TicketLogsEmbed)
                        await select.response.send_modal(iddt())
                    elif interaction.values[0] != "Other":
                            await select.response.send_message(f"The ticket was created successfully", ephemeral = True)   
                            description = f"Username: {user.name}#{user.discriminator}\nID: {user.id}\nTicket Creation time: {datetime.now()}"
                            ticketchannel = await guild.create_text_channel(name=f"{user.id}-ticket", topic=description, category=category)
                            await ticketchannel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                            await ticketchannel.set_permissions(user, read_messages=True, send_messages=True)
                            await ticketchannel.set_permissions(staffrole, read_messages=True, send_messages=True)
                            message = await ticketchannel.send(f"{staffrole.mention} | {user.mention}")
                            await message.delete()
                            embeddd=discord.Embed(title="Ticket Tool", timestamp=datetime.now(), description=f"**{staffrole.mention}**\n__**ticket was opened by {user.mention}**__\n•** User Name: {user.name}#{user.discriminator}**\n•** User ID: {user.id}**\n\n__**General Information**__\n•** Ticket Creation time: ``{time.strftime(f'%d/%m/%Y, %H:%M:%S')}``**\n•** Reason: {interaction.values[0]}**\n•** __Thank you for contacting us, The staff team will contact you__**", color=0x00f5f1)
                            embeddd.set_author(name=f"{servername}", icon_url=f"{servericon}")
                            embeddd.set_thumbnail(url=emojilink)
                            embeddd.set_footer(text="© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
                            await ticketchannel.send(embed=embeddd, view=button)
                            channellogs = await AutoSystems.Tickets.OpenTicket.CreateTicketLogs("〈📋〉ticketlogs")
                            TicketLogsEmbed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is has been created\n``Information about the user - \n\nUser Name: {user.name}#{user.discriminator}\nUser ID: {user.id}\nTicket Creation time: {datetime.now()}\nReason: {interaction.values[0]}``**", color=0x33FFC7)
                            TicketLogsEmbed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            TicketLogsEmbed.set_thumbnail(url=f"{servericon}")
                            TicketLogsEmbed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
                            await channellogs.send(embed=TicketLogsEmbed)
except NameError as e:
    pass






























class AutoSystems:
    class AutoRole:
        async def autorole(member):
            try:
                role = read_subdata_from_json("bot\\system_config.json", "config", "AutoRole-Role")
                roleget = discord.utils.get(guild.roles, id=int(role))
            except:
                error(f"AutoRole System, The bot fails to get the role")
            await member.add_roles(roleget)



    class Setstatus:
        async def activity(txt):
            activity = discord.Activity(type=discord.ActivityType.playing, name=f'{txt}')
            await bot.change_presence(activity=activity)

    class VerifySystemC:
        async def CAPTCHA(menu, botrole):
            mylist = []
            num1 = Rwords(1,10)
            num2 = Rwords(1,10)
            num3 = Rwords(1,10)
            num4 = Rwords(1,10)
            num5 = Rwords(1,10)
            mylist.append(num1)
            mylist.append(num2)
            mylist.append(num3)
            mylist.append(num4)
            mylist.append(num5)
            se1 = random.choice(mylist)
            mylist.remove(se1)
            se2 = random.choice(mylist)
            mylist.remove(se2)
            se3 = random.choice(mylist)
            mylist.remove(se3)
            se4 = random.choice(mylist)
            mylist.remove(se4)
            se5 = random.choice(mylist)
            mylist.remove(se5)
            class Verify2(discord.ui.View,):
                def __init__(self):
                    super().__init__(timeout=None)
                @discord.ui.button(label=f'{se1}', style=discord.ButtonStyle.green, custom_id='Verify1_view:add1')
                async def add1(self, interaction: discord.Interaction, button: discord.ui.Button):
                    member = interaction.user
                    if se1 == num3:
                        if botrole not in member.roles:
                            await member.add_roles(botrole)
                            await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                        else:
                            await interaction.response.send_message(f"You already have the role", ephemeral=True)
                    else:
                        try:
                            await member.kick()
                        except:
                            await interaction.response.send_message(f"You failed to pass the verification", ephemeral=True)
                @discord.ui.button(label=f'{se3}', style=discord.ButtonStyle.green, custom_id='Verify1_view:add2')
                async def add2(self, interaction: discord.Interaction, button: discord.ui.Button):
                    member = interaction.user
                    if se3 == num3:
                        if botrole not in member.roles:
                            await member.add_roles(botrole)
                            await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                        else:
                            await interaction.response.send_message(f"You already have the role", ephemeral=True)
                    else:
                        try:
                            await member.kick()
                        except:
                            await interaction.response.send_message(f"You failed to pass the verification", ephemeral=True)
                @discord.ui.button(label=f'{se5}', style=discord.ButtonStyle.green, custom_id='Verify1_view:add4')
                async def add4(self, interaction: discord.Interaction, button: discord.ui.Button):
                    member = interaction.user
                    if se5 == num3:
                        if botrole not in member.roles:
                            await member.add_roles(botrole)
                            await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                        else:
                            await interaction.response.send_message(f"You already have the role", ephemeral=True)
                    else:
                        try:
                            await member.kick()
                        except:
                            await interaction.response.send_message(f"You failed to pass the verification", ephemeral=True)
                @discord.ui.button(label=f'{se4}', style=discord.ButtonStyle.green, custom_id='Verify1_view:add5')
                async def add5(self, interaction: discord.Interaction, button: discord.ui.Button):
                    member = interaction.user
                    if se4 == num3:
                        if botrole not in member.roles:
                            await member.add_roles(botrole)
                            await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                        else:
                            await interaction.response.send_message(f"You already have the role", ephemeral=True)
                    else:
                        try:
                            await member.kick()
                        except:
                            await interaction.response.send_message(f"You failed to pass the verification", ephemeral=True)
                @discord.ui.button(label=f'{se2}', style=discord.ButtonStyle.green, custom_id='Verify1_view:add3')
                async def add3(self, interaction: discord.Interaction, button: discord.ui.Button):
                    member = interaction.user
                    if se2 == num3:
                        if botrole not in member.roles:
                            await member.add_roles(botrole)
                            await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                        else:
                            await interaction.response.send_message(f"You already have the role", ephemeral=True)
                    else:
                        try:
                            await member.kick()
                        except:
                            await interaction.response.send_message(f"You failed to pass the verification", ephemeral=True)
            message = await menu.response.send_message(f"The security system asks for additional authentication, select the button with the identical characters ||[{num3}]||", ephemeral=True, view=Verify2())


        async def VerifySystem(VerifyChannel, MemberRole, embedd=None, TimeProtecion=bool, CAPTCHAProtecion=bool):
            try:
                await add_emoji_to_server("emojis\\verify.gif", "verify")
                await asyncio.sleep(4)
                emojii = emojisValues["verify"]
            except:
                await add_emoji_to_server("emojis\\verify.gif", "verify")
                await asyncio.sleep(4)
                emojiis = read_emojis()
                emojii = emojiis["verify"]
            channel = guild.get_channel(VerifyChannel)
            try:
                await channel.purge()
            except:
                pass
            if not channel:
                return error(f"Command Error Verify System, The Channel was not found")
            botrole = guild.get_role(MemberRole)
            if not botrole:
                return error(f"Command Error Verify System, The Role was not found")
            class Verify1(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)

                @discord.ui.button(label='verify', style=discord.ButtonStyle.green, custom_id='Verify1_view:verify', emoji=emojii)
                async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
                    week2 = datetime.now(tz=timezone.utc) - timedelta(days=14)
                    month = datetime.now(tz=timezone.utc) - timedelta(days=30)
                    user = interaction.user
                    member = guild.get_member(user.id)
                    created_at = member.created_at
                    if TimeProtecion is True:
                        created_at_offset_aware = datetime.utcfromtimestamp(created_at.timestamp()).replace(tzinfo=timezone.utc)
                        if created_at_offset_aware > week2:
                            await member.ban(reason=f"The user has been removed from the server because it was created in the last two weeks")
                            return
                        elif created_at_offset_aware > month:
                            duration = timedelta(days=7.1)
                            await member.timeout(duration)
                            await interaction.response.send_message(f"The user was created less than a month ago", ephemeral=True)
                            return
                    if CAPTCHAProtecion is True:
                        await AutoSystems.VerifySystemC.CAPTCHA(interaction, botrole)
                        return
                    if CAPTCHAProtecion is False:
                        if botrole not in member.roles:
                            await member.add_roles(botrole)
                            try:
                                await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                            except:
                                pass
                        else:
                            try:
                                await interaction.response.send_message(f"You already have the role", ephemeral=True)
                            except:
                                pass
            if embedd is not None:
                await channel.send(embed=embedd, view=Verify1())
                return
            else:
                emojilinkVerify = await emoji_ui("emojis\\verify2.gif")
                embedV=discord.Embed(title=f"The authentication system", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**User authentication system for server security**", color=0x00ff89)
                embedV.set_thumbnail(url=f"{emojilinkVerify}")
                embedV.set_author(name=f"{guild.name} Bot", icon_url=servericon)
                embedV.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=servericon)
                await channel.send(embed=embedV, view=Verify1())


    class Tickets:
        class OpenTicket:
            


            async def transcript(channelid):
                channel = bot.get_channel(channelid)
                messages = channel.history(limit=None)

                transcript = f'{style}<div class="chat-header">\n    <h1 class="chat-title">{servername}</h1>\n    <p class="chat-description">Channel Name: {channel.name}\nChannel ID: {channel.id}</p>\n</div>\n<div class="chat-container">'
                async for msg in messages:
                    timestamp = msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    author = msg.author.name
                    content = msg.content.replace('\n', '<br>')
                    transcript += f'\n    <div class="message">\n        <span class="timestamp">{timestamp} </span>\n        <span class="author">{author}: </span>\n        <div class="content">{content}</div>\n    </div>'

                transcript += '</body></html>'
                return transcript

            

            async def CreateTicketLogs(channelname):
                categoryBot = await def_category()
                channel = discord.utils.get(guild.channels, name=f"{channelname}")
                if not channel:
                    await guild.create_text_channel(name=f"{channelname}", category=categoryBot)
                    channel = discord.utils.get(guild.channels, name=f"{channelname}")
                    await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                channel = discord.utils.get(guild.channels, name=f"{channelname}")
                return channel

        async def Buttonss(staffrole):
            class CreateButtonsClass(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)



                @discord.ui.button(label='〈❌〉Close Ticket', style=discord.ButtonStyle.red, custom_id='ticket_view:CloseTicket')
                async def CloseTicket(self, interaction: discord.Interaction, button: discord.ui.Button):
                    if staffrole not in interaction.user.roles:
                        await interaction.response.send_message(f"You do not have this role: {staffrole}", ephemeral = True)
                    else:
                        script = await AutoSystems.Tickets.OpenTicket.transcript(interaction.channel.id)
                        channellogs = await AutoSystems.Tickets.OpenTicket.CreateTicketLogs("〈📋〉ticketlogs")
                        with open(f'transcript.html', 'w', encoding='utf-8') as file:
                            file.write(script)
                        with open(f'transcript.html', 'r', encoding='utf-8') as file:
                            htmltext = file.read()
                            filee = discord.File(f'transcript.html')
                        embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is Closed\n``Information about the user who Closed the ticket\n\nUser Name: {interaction.user.name}#{interaction.user.discriminator}\nUser ID: {interaction.user.id}\nTicket: {interaction.channel}\nClosed Time: {datetime.now()}``**", color=0xff0000)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
                        await channellogs.send(embed=embed, file=filee)
                        os.system("del transcript.html")
                        await interaction.channel.delete()
                

                @discord.ui.button(label="〈👥〉Add Member", style=discord.ButtonStyle.green, custom_id="ccticket_view:addmember")
                async def addmember(self, interaction: discord.Interaction, button: discord.ui.Button):
                    if staffrole in interaction.user.roles:
                        try:
                            await interaction.response.send_modal(addmember())
                        except:
                            pass
                    if staffrole not in interaction.user.roles:
                        await interaction.response.send_message(f'You do not have permissions', ephemeral=True)

                @discord.ui.button(label="〈👤〉Delete Member", style=discord.ButtonStyle.green, custom_id="ccticket_view:deletemember")
                async def deletemember(self, interaction: discord.Interaction, button: discord.ui.Button):
                    if staffrole in interaction.user.roles:
                        try:
                            await interaction.response.send_modal(deletemember())
                        except:
                            pass
                    if staffrole not in interaction.user.roles:
                        await interaction.response.send_message(f'You do not have permissions', ephemeral=True)

                

                @discord.ui.button(label="〈👏〉Rename", style=discord.ButtonStyle.blurple, custom_id="ccticket_view:rename")
                async def rename(self, interaction: discord.Interaction, button: discord.ui.Button):
                    if staffrole in interaction.user.roles:
                        try:
                            await interaction.response.send_modal(rename())
                        except:
                            pass
                    if staffrole not in interaction.user.roles:
                        await interaction.response.send_message(f'You do not have permissions', ephemeral=True)
            return CreateButtonsClass()




        async def TicketButton(emojilink):
            try:
                emojiiOpenTicket = emojisValues["openticket"]
                ServerRules = emojisValues["ServerRules"]
                Giveaway = emojisValues["Giveaway"]
                question = emojisValues["question"]
            except:
                await add_emoji_to_server("emojis\\openticket2.png", "openticket")
                await asyncio.sleep(4)
                await add_emoji_to_server("emojis\\ServerRules.png", "ServerRules")
                await asyncio.sleep(4)
                await add_emoji_to_server("emojis\\Giveaway.gif", "Giveaway")
                await asyncio.sleep(4)
                await add_emoji_to_server("emojis\\question.gif", "question")
                await asyncio.sleep(4)
            try:
                emojii = emojisValues["openticket"]
            except:
                await add_emoji_to_server("emojis\\openticket2.png", "openticket")
                await asyncio.sleep(4)
                emojiss = read_emojis()
                await asyncio.sleep(4)
                emojii = emojiss["openticket"]
            class Tickett(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)

                @discord.ui.button(label='Create Ticket', style=discord.ButtonStyle.blurple, custom_id='bt_view:cticket', emoji=emojii)
                async def cticket(self, interaction: discord.Interaction, button: discord.ui.Button):
                    try:
                        await interaction.response.send_message(f"Choose a reason", ephemeral = True, view=selectmenus.ticketselect())
                    except:
                        os.system("start main.exe")
                        close()
            return Tickett()
        


        async def TicketSystem(ChannelID, embedd=None):
            try:
                emojiiOpenTicket = emojisValues["openticket"]
                ServerRules = emojisValues["ServerRules"]
                Giveaway = emojisValues["Giveaway"]
                question = emojisValues["question"]
            except:
                await add_emoji_to_server("emojis\\openticket2.png", "openticket")
                await asyncio.sleep(4)
                await add_emoji_to_server("emojis\\ServerRules.png", "ServerRules")
                await asyncio.sleep(4)
                await add_emoji_to_server("emojis\\Giveaway.gif", "Giveaway")
                await asyncio.sleep(4)
                await add_emoji_to_server("emojis\\question.gif", "question")
                await asyncio.sleep(4)
            emojilink = await emoji_ui("emojis\\openticket.png")
            try:
                button = await AutoSystems.Tickets.TicketButton(emojilink)
            except:
                pass
            channel = bot.get_channel(ChannelID)
            if not channel:
                return error(f"Command Error Ticket System, The Channel was not found")
            try:
                await channel.purge()
            except:
                pass
            if embedd is not None:
                await channel.send(embed=embedd, view=button)
            else:
                embed=discord.Embed(title="Ticket Tool", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**You can open a response/help ticket on the server**", color=0x00ffff)
                embed.set_author(name=f"{guild.name} Bot", icon_url=servericon)
                embed.set_thumbnail(url=f"{emojilink}")
                embed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=servericon)
                await channel.send(embed=embed, view=button)


    class BanList:
        def CreateBanList():
            create_text_file("SystemDB\\banlist.json")
        
        async def AddMember(memberid, reason):
            AutoSystems.BanList.CreateBanList()
            update_text_file("SystemDB\\banlist.json", f"{memberid}", f"{reason}")
            try:
                member = guild.get_member(memberid)
                await member.ban(reason="A user is on the banlist")
            except:
                pass

        async def RemoveMember(memberid):
            try:
                AutoSystems.BanList.CreateBanList()
                delete_data_or_category("SystemDB\\banlist.json", f"{memberid}")
                delete_data_or_category("SystemDB\\PublicBanList.json", f"{memberid}")
                member = guild.get_member(memberid)
                await member.unban(reason="A user is on the banlist")
            except:
                pass
        
        def CheckMember(memberid):
            AutoSystems.BanList.CreateBanList()
            value = read_value_from_text_file("SystemDB\\banlist.json", f"{memberid}", False, False)
            value2 = read_value_from_text_file("SystemDB\\PublicBanList.json", f"{memberid}", False, False)
            if value is not None or value2 is not None:
                return True
            else:
                return False
        
        def GetReason(memberid):
            AutoSystems.BanList.CreateBanList()
            banlist = []
            value = read_value_from_text_file("SystemDB\\banlist.json", f"{memberid}")
            value2 = read_value_from_text_file("SystemDB\\PublicBanList.json", f"{memberid}", False, False)
            banlist.append(value)
            banlist.append(value2)
            return banlist
        
        def UpdatePasteBin(code):
            url = f"https://pastebin.com/raw/{code}"
            response = requests.get(url)
            if response.status_code == 200:
                text = response.text
                try:
                    data = json.loads(text)
                    for key, value in data.items():
                        update_text_file("SystemDB\\PublicBanList.json", f"{key}", f"{value}", False)     
                except json.JSONDecodeError as e:
                    error(f"Failed to decode JSON: \n{e}")
            else:
                error(f"Information access problem")


        async def banlistButtonss():     
            class banlistButtons(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)



                @discord.ui.button(label="〈🚫〉Scan BanList", style=discord.ButtonStyle.red, custom_id="banlist_view:scanbanlist")
                async def scanbanlist(self, interaction: discord.Interaction, button: discord.ui.Button):
                    await interaction.response.send_message(f'All the people on the ban list were removed from the server.', ephemeral=True)
                    for member in guild.members:
                        
                        await AutoSystems.BanList.banlistAction(member.id)
                
                @discord.ui.button(label="〈⭕️〉Add BanList", style=discord.ButtonStyle.red, custom_id="banlist_view:addmember")
                async def addmember(self, interaction: discord.Interaction, button: discord.ui.Button):
                    class textinputer(ui.Modal, title=f'BanList Response'):
                        memberid = ui.TextInput(label=f'Member ID')
                        reason = ui.TextInput(label=f'Reason')

                        async def on_submit(self, interaction: discord.Interaction):
                            await AutoSystems.BanList.AddMember(int(self.memberid.value), self.reason.value)
                            await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
                    await interaction.response.send_modal(textinputer())
                


                @discord.ui.button(label="〈❌〉Remove BanList", style=discord.ButtonStyle.red, custom_id="banlist_view:removemember")
                async def removemember(self, interaction: discord.Interaction, button: discord.ui.Button):
                    class textinputer(ui.Modal, title=f'BanList Response'):
                        memberid = ui.TextInput(label=f'Member ID')

                        async def on_submit(self, interaction: discord.Interaction):
                            await AutoSystems.BanList.RemoveMember(int(self.memberid.value))
                            await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
                    await interaction.response.send_modal(textinputer())
                

                @discord.ui.button(label="〈🔍〉Update BanList", style=discord.ButtonStyle.green, custom_id="banlist_view:updatemember")
                async def updatemember(self, interaction: discord.Interaction, button: discord.ui.Button):
                    await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
                    AutoSystems.BanList.UpdatePasteBin("u2QxrFZB")
                    
                    



            return banlistButtons()


        async def banlistAction(memberid):
            value = AutoSystems.BanList.CheckMember(memberid)
            if value is True:
                member = guild.get_member(memberid)
                reasonn = AutoSystems.BanList.GetReason(memberid)
                try:
                    await member.ban(reason=f"A user is on the banlist\n{reasonn[0]}")
                except:
                    pass

        

        async def StartBanList(embedd=None):
            Botcategory = await def_category()
            channel = await check_channel("〈✏〉admin-panel", "BanList Channel", f"{Botcategory.name}", True)
            buttons = await AutoSystems.BanList.banlistButtonss()
            if embedd is None:
                emojilink = await emoji_ui(f"emojis\\staff.gif")
                embed=discord.Embed(title=f"✨ Administrator Panel | {servername}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**__The admin control panel on the server and most of the things on the server__**", color=0xcc00ff)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{emojilink}")
                embed.set_footer(text=f"© Copyright by LogicLab 2022 - 2024", icon_url=f"{servericon}")
                try:
                    await channel.purge()
                except:
                    pass
                await channel.send(embed=embed, view=buttons)
            else:
                await channel.send(embed=embedd, view=buttons)
        

    class welcome:
        async def welcome(member):
            channelid = read_subdata_from_json("bot\\system_config.json", "config", "Welcome-Channel")
            try:
                channel = discord.utils.get(guild.channels, id=int(channelid))
            except:
                return error(f"Welcome Error, The channel was not found")
            if not channel:
                return error(f"Welcome Error, The channel was not found")
            embed = discord.Embed(title="〈👋〉Welcome to the server", timestamp=datetime.now(), description=f"__**Welcome to the server**__\n**Member Name: ``{member.name}``**\n**Member ID: ``{member.id}``**\n**Server Name: __{servername}__**", color=discord.Colour.random())
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embed.set_thumbnail(url=f"{servericon}")
            await channel.send(embed=embed)








        










        

#Systems Functions -----------------------













#Basic Command
"""
@bot.command(name='test')
async def test(ctx: commands.Context):
    pass
"""

#Tree Command
"""
@bot.tree.command(name="ping", description="pong")
@app_commands.describe(test='test')
@app_commands.choices(test=[
    app_commands.Choice(name='test', value=1),
])
async def ping(interaction: discord.Interaction, test: app_commands.Choice[int]=False):
    await interaction.response.send_message(f"Pong")
"""



# Commands Actions

#@bot.command(name='test')
#async def test(ctx: commands.Context):
#    pass



def VerifyCommands():
    @bot.tree.command(name="verify-status", description="Status change for the authentication system")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(status='Turn the system on or off')
    @app_commands.choices(status=[
        app_commands.Choice(name='True', value=1),
        app_commands.Choice(name='False', value=2),
    ])
    @app_commands.describe(system='Choose a system')
    @app_commands.choices(system=[
        app_commands.Choice(name='Verify', value=1),
        app_commands.Choice(name='Verify-AntiAlt', value=2),
        app_commands.Choice(name='Verify-Captcha', value=3),
    ])
    async def cmd(interaction: discord.Interaction, status: app_commands.Choice[int], system: app_commands.Choice[int]):
        if interaction.user.id == int(ilist[5]):
            update_subdata("bot\\system_config.json", "config", f"{system.name}", f"{status.name}")
            await interaction.response.send_message("operation completed", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)



    @bot.tree.command(name="verify-settings", description="Set Channel or Role to Verify System")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(system='Choose a system')
    @app_commands.choices(system=[
        app_commands.Choice(name='Channel', value=1),
        app_commands.Choice(name='Role', value=2),
    ])
    async def cmd(interaction: discord.Interaction, system: app_commands.Choice[int]):
        if interaction.user.id == int(ilist[5]):
            class id(ui.Modal, title='Role or Channel'):
                idd = ui.TextInput(label="Role or Channel ID")
                

                async def on_submit(self, interaction: discord.Interaction):
                    with switch(system.name):
                        if case("Channel").true:
                            update_subdata("bot\\system_config.json", "config", f"Verify-Channel", f"{self.idd.value}")
                        elif case("Role").true:
                            update_subdata("bot\\system_config.json", "config", f"Verify-Role", f"{self.idd.value}")
                    await interaction.response.send_message("operation completed", ephemeral=True)
            
            await interaction.response.send_modal(id())
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)


    @bot.tree.command(name="verify-refresh", description="Refresh the authentication system")
    @app_commands.default_permissions(administrator=True)
    async def cmd(interaction: discord.Interaction):
        if interaction.user.id == int(ilist[5]):
            verify = read_subdata_from_json("bot\\system_config.json", "config", "Verify")
            if verify == "False":
                return await interaction.response.send_message("The authentication system is turned off", ephemeral=True)
            else:
                await interaction.response.send_message("operation completed", ephemeral=True)
                antialt = read_subdata_from_json("bot\\system_config.json", "config", "Verify-AntiAlt")
                CAPTCHAProtecion = read_subdata_from_json("bot\\system_config.json", "config", "Verify-Captcha")
                role = read_subdata_from_json("bot\\system_config.json", "config", "Verify-Role")
                channel = read_subdata_from_json("bot\\system_config.json", "config", "Verify-Channel")
                if antialt == "False":
                    antialt = False
                else:
                    antialt = True
                if CAPTCHAProtecion == "False":
                    CAPTCHAProtecion = False
                else:
                    CAPTCHAProtecion = True
                await AutoSystems.VerifySystemC.VerifySystem(int(channel), int(role), None, antialt, CAPTCHAProtecion)
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)


def TicketCommands():
    @bot.tree.command(name="ticket-status", description="Changing the status of the ticket system")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(status='Turn the system on or off')
    @app_commands.choices(status=[
        app_commands.Choice(name='True', value=1),
        app_commands.Choice(name='False', value=2),
    ])
    @app_commands.describe(system='Choose a system')
    @app_commands.choices(system=[
        app_commands.Choice(name='Ticket', value=1),
    ])
    async def cmd(interaction: discord.Interaction, status: app_commands.Choice[int], system: app_commands.Choice[int]):
        if interaction.user.id == int(ilist[5]):      
            update_subdata("bot\\system_config.json", "config", f"{system.name}", f"{status.name}")
            await interaction.response.send_message("operation completed", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)

    @bot.tree.command(name="ticket-settings", description="Changing the status of the ticket system")
    @app_commands.default_permissions(administrator=True)
    async def cmd(interaction: discord.Interaction):
            if interaction.user.id == int(ilist[5]):
                class id(ui.Modal, title='Changing ticket system settings'):
                    categoryid = ui.TextInput(label="The ID of the category")
                    roleid = ui.TextInput(label="ID of the staff Team Role")
                    cid = ui.TextInput(label="The ID of the ticket Channel")
                    

                    async def on_submit(self, interaction: discord.Interaction):
                        update_subdata("bot\\system_config.json", "config", f"Ticket-Category", f"{self.categoryid.value}")
                        update_subdata("bot\\system_config.json", "config", f"Ticket-StaffRoleID", f"{self.roleid.value}")
                        update_subdata("bot\\system_config.json", "config", f"Ticket-Channel", f"{self.cid.value}")
                        await interaction.response.send_message("operation completed", ephemeral=True)
                
                await interaction.response.send_modal(id())
            else:
                await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)
    

    @bot.tree.command(name="ticket-refresh", description="Refreshment of the ticket system")
    @app_commands.default_permissions(administrator=True)
    async def cmd(interaction: discord.Interaction):
        if interaction.user.id == int(ilist[5]):
            ticket = read_subdata_from_json("bot\\system_config.json", "config", "Ticket")
            if ticket == "True":
                await interaction.response.send_message("operation completed", ephemeral=True)
                channelid = read_subdata_from_json("bot\\system_config.json", "config", "Ticket-Channel")
                await AutoSystems.Tickets.TicketSystem(int(channelid), None)
            else:
                await interaction.response.send_message("The Ticket system is not active", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)



def BanListCommands():
    @bot.tree.command(name="banlist-status", description="Changing the status of the automatic ban system")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(status='Turn the system on or off')
    @app_commands.choices(status=[
        app_commands.Choice(name='True', value=1),
        app_commands.Choice(name='False', value=2),
    ])
    @app_commands.describe(system='Choose a system')
    @app_commands.choices(system=[
        app_commands.Choice(name='BanList', value=1),
    ])
    async def cmd(interaction: discord.Interaction, status: app_commands.Choice[int], system: app_commands.Choice[int]):
        if interaction.user.id == int(ilist[5]):
            update_subdata("bot\\system_config.json", "config", f"{system.name}", f"{status.name}")
            await interaction.response.send_message("operation completed", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to the bot's security system", ephemeral=True)
    
    @bot.tree.command(name="banlist-refresh", description="Refreshing the automatic ban system")
    @app_commands.default_permissions(administrator=True)
    async def cmd(interaction: discord.Interaction):
        if interaction.user.id == int(ilist[5]):
            banlist = read_subdata_from_json("bot\\system_config.json", "config", "BanList")
            if banlist == "True":
                await AutoSystems.BanList.StartBanList(None)
                await interaction.response.send_message("operation completed", ephemeral=True)
            else:
                await interaction.response.send_message("The BanList system is not active", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to the bot's security system", ephemeral=True)


def WelcomeCommands():
    @bot.tree.command(name="welcome-status", description="A system that sends a message about every user who joins the server")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(status='Turn the system on or off')
    @app_commands.choices(status=[
        app_commands.Choice(name='True', value=1),
        app_commands.Choice(name='False', value=2),
    ])
    @app_commands.describe(system='Choose a system')
    @app_commands.choices(system=[
        app_commands.Choice(name='Welcome', value=1),
    ])
    async def cmd(interaction: discord.Interaction, status: app_commands.Choice[int], system: app_commands.Choice[int]):
        if interaction.user.id == int(ilist[5]):
            update_subdata("bot\\system_config.json", "config", f"{system.name}", f"{status.name}")
            await interaction.response.send_message("operation completed", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)
    

    @bot.tree.command(name="welcome-settings", description="A system that sends a message about every user who joins the server")
    @app_commands.default_permissions(administrator=True)
    async def cmd(interaction: discord.Interaction):
        if interaction.user.id == int(ilist[5]):
            class id(ui.Modal, title='Channel'):
                idd = ui.TextInput(label="Channel ID")
                

                async def on_submit(self, interaction: discord.Interaction):
                    update_subdata("bot\\system_config.json", "config", f"Welcome-Channel", f"{self.idd.value}")
                    await interaction.response.send_message("operation completed", ephemeral=True)
            await interaction.response.send_modal(id())
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)
    

    @bot.tree.command(name="autorole-settings", description="A system that automatically assigns a role when someone enters a Discord server")
    @app_commands.default_permissions(administrator=True)
    async def cmd(interaction: discord.Interaction):
        if interaction.user.id == int(ilist[5]):
            class id(ui.Modal, title='Discord Role'):
                idd = ui.TextInput(label="Role ID")
                

                async def on_submit(self, interaction: discord.Interaction):
                    update_subdata("bot\\system_config.json", "config", f"AutoRole-Role", f"{self.idd.value}")
                    await interaction.response.send_message("operation completed", ephemeral=True)
            await interaction.response.send_modal(id())
        else:
            await interaction.response.send_message("You do not have permission to the bot's systems", ephemeral=True)



VerifyCommands()
TicketCommands()
BanListCommands()
WelcomeCommands()


# Commands Actions

#Bot Commands ---------------------











# Event Actions

@bot.event
async def on_member_join(member):
    try:
        banlist = read_subdata_from_json("bot\\system_config.json", "config", "BanList")
        if banlist == "True":
            await AutoSystems.BanList.banlistAction(member.id)
        memberjoin = read_subdata_from_json("bot\\system_config.json", "config", "Welcome")
        if memberjoin == "True":
            await AutoSystems.welcome.welcome(member)
        autorole = read_subdata_from_json("bot\\system_config.json", "config", "AutoRole")
        if autorole == "True":
            AutoSystems.AutoRole.autorole(member)
    except:
        pass


# Event Actions

#Bot Events ---------------------











# TaskLoops Actions

# TaskLoops Actions

#TaskLoops ---------------------










#On Bot Ready --------------------------
@bot.event
async def on_connect():
    await bot.wait_until_ready()

os.system("cls")
print(Fore.MAGENTA + "=" * 40)

while True:
    try:
        bot.run(f'{ilist[0]}', reconnect=True)
    except KeyboardInterrupt:
        print(Fore.RED + f"[{time.strftime('%H:%M:%S')}] Bot process terminated by user.")
        break
    except discord.LoginFailure:
        print(Fore.RED + f"[{time.strftime('%H:%M:%S')}] Invalid token. Please provide a valid bot token.")
        bottoken = input("Your bot's token: ")
        update_text_file("bot\\botconfig.json", "bottoken", f"{bottoken}")
    except Exception as e:
        os.system("cls")
        os.system("TASKKILL /F /PID %s" % os.getpid())

#On Bot Ready --------------------------


