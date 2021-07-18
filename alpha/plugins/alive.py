
import time
from userbot import *
from userbot import bot as TheAlphaX
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon import version
from datetime import datetime
from userbot import ALIVE_NAME, StartTime, botversion ,
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


#-------------------------------------------------------------------------------

start = datetime.now()
end = datetime.now()
ms = (end - start).microseconds / 1000
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

ludosudo = Config.SUDO_USERS
if ludosudo:
    sudou = "True"
else:
    sudou = "False"

DEFAULTUSER = ALIVE_NAME or " User"
My_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Legendary Bot"

USERID = bot.uid

furious = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@TheAlphaX.on(admin_cmd(outgoing=True, pattern="about$"))
@TheAlphaX.on(sudo_cmd(pattern="about$", allow_sudo=True))
async def aboutme(about):
    if about.fwd_from:
        return
    reply_to_id = await reply_id(about)

    if My_IMG:
        My_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        
        My_caption += f"      __**»★ABOUT ME★«**__\n"
        My_caption += f"**╭─────☆═━┈┈┈━═☆─────╮**\n"
        My_caption += f"**※ MY OWNER:** ** {furious} **\n"
        My_caption += f"**※ MY NAME : NO ONE KNOWS**\n"
        My_caption += f"**※ MY VERSION : **`{botversion}`\n"
        My_caption += f"**※ MY PING: **`{ms}`\n"
        My_caption += f"**※ MY STATUS : WORKING FINALLY **\n"
        My_caption += f"**※ MY TELETHON VERSION : ** `{version.__version__}`\n"
        My_caption += f"**※ I'M ON TILL : ** `{uptime}`\n"
        My_caption += f"**※ MY SUDO STATUS :** `{sudou}`\n"
        My_caption += f"**※ MY CREATOR :** ** [🇮🇳• Pʀɪɴᴄᴇ •🇮🇳](https://t.me/Nikkuiii)**\n"
        My_caption += f"**╰──────☆═━┈┈┈━═☆─────╯**\n"
    

        await about.client.send_file(
            about.chat_id, My_IMG, caption=My_caption, reply_to=reply_to_id
        )
    else:
        await edit_or_reply(
            about,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"      __**»★ABOUT ME★«**__\n"
            f"**╭──────☆═━┈┈┈━═☆─────╮**\n"
            f"**※ MY OWNER : ** ** {furious} **\n"
            f"**※ MY NAME : NO ONE KNOWS**\n"
            f"**※ MY VERSION : **`{botversion}`\n"
            f"**※ MY PING: **`{ms}`\n"
            f"**※ MY STATUS : WORKING FINALLY **\n"
            f"**※ MY TELETHON VERSION : ** `{version.__version__}`\n"
            f"**※ I`M ON TILL : ** `{uptime}`\n"
            f"**※ MY SUDO STATUS : ** `{sudou}`\n"
            f"**※ MY CREATOR :** ** [🇮🇳• Pʀɪɴᴄᴇ •🇮🇳](https://t.me/Nikkuiii)**\n"
            f"**╰────────☆═━┈┈┈━═☆───────╯**\n"
             )
CmdHelp("alive").add_command(
  'about', None, 'Tell about the bot'
  ).add_info(
  'Kuch batayega kya bro apne baare me?'
).add()
