from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config

BUTTONS = [[
    InlineKeyboardButton("♨ Powered By", url="https://t.me/bots137"),
    InlineKeyboardButton("♻ Help", callback_data="help")
    ],[
    InlineKeyboardButton("🏡 Home", callback_data="home"),
    InlineKeyboardButton("🔐 Close", callback_data="close")
]]

ABOUT_TEXT = """
<b>Cʜᴀɴɴᴇʟ : <a href='https://t.me/Bots137'>Bots137</a></b>

<b>Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3.10.2</a></b>

<b>Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢᴀᴍ 1.3.6</a></b>

__If issues persists contact my Master.__

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Since you are one of the admins, you can check /admin to view the admin commands."
)


@ScreenShotBot.on_message(filters.private & filters.command("about"))
async def about_(c, m):
    await m.reply_text(
        text=ABOUT_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("about"))
)
async def about_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=ABOUT_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS)
    )
