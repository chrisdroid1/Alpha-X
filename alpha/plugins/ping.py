import time

from alpha import alpha, Ownerfilter
from pyrogram import filters
from pyrogram.types import Message


@alpha.on_message(Ownerfilter & filters.command("ping"))
async def ping(_, msg: Message):
    text = "**Pong!**"
    st = time.time()
    message = await alpha.edit_message_text(
        msg.chat.id,
        msg.message_id,
        text
    )
    et = time.time()
    text += f"\n`{et - st} ms`"

    await message.edit(text)
