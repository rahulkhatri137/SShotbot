from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config
from bot.database.forcesub import ForceSub


BUTTONS = [[
        InlineKeyboardButton("♨ Powered By", url="https://t.me/MoviesFlixers_DL"),
        InlineKeyboardButton("♻ Help", callback_data="help")
        ],[
        InlineKeyboardButton("🏡 Home", callback_data="home"),
        InlineKeyboardButton("🔐 Close", callback_data="close")
    ]]

ABOUT_TEXT = """
<b>Mʏ ɴᴀᴍᴇ : <a href='http://t.me/TeleRoudScreenshotBot'>Screen ʙᴏᴛ</a></b>

<b>Cʜᴀɴɴᴇʟ : <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a></b>

<b>Sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/TeleRoid14'>@TeleRoid14</a></b>

<b>Vᴇʀꜱɪᴏɴ : <a href='https://t.me/joinchat/t1ko_FOJxhFiOThl'>2.0 ʙᴇᴛᴀ</a></b>

<b>Sᴏᴜʀᴄᴇ : <a href='https://github.com/PredatorHackerzZ'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>

<b>Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a></b>

<b>Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3.10.2</a></b>

<b>Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢᴀᴍ 1.3.6</a></b>

<b>Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/MoviesFlixers_DL'>Pʀᴇᴅᴀᴛᴏʀ</a></b>

<b>Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/TheTeleRoid'>@TheTeleRoid</a></b>

__If issues persists contact my Master.__

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Since you are one of the admins, you can check /admin to view the admin commands."
)


@ScreenShotBot.on_message(filters.private & filters.command("about"))
async def about_(c, m):
    forcesub = await ForceSub(c, m,)
    if forcesub == 400:
        return
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
