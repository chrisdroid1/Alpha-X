from git import Repo
import os
from telethon.tl.functions.channels import ExportMessageLinkRequest as GetLink

from . import *



@ultroid_cmd(pattern="update$")
async def _(e):
    xx = await eor(e, "`Checking for updates...`")
    m = await updater()
    branch = (Repo.init()).active_branch
    if m:
        x = await asst.send_file(
            int(os.environ.get("LOG_CHANNEL")),
            caption="• **Update Available** •",
            force_document=False,
            buttons=Button.inline("Changelogs", data="changes"),
        )
        if not e.client._bot:
            Link = (await e.client(GetLink(x.chat_id, x.id))).link
        else:
            Link = f"https://t.me/{x.chat.id}/{x.id}"
        await xx.edit(
            f'<strong><a href="{Link}">[ChangeLogs]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )
    else:
        await xx.edit(
            f'<code>Your BOT is </code><strong>up-to-date</strong><code> with </code><strong><a href="https://github.com/TheAlphaX/Alpha-X/tree/{branch}">[{branch}]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )
