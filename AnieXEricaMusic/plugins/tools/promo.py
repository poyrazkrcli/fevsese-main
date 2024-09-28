from pyrogram import filters, Client
from pyrogram.types import Message
from unidecode import unidecode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnieXEricaMusic import app
import random 
from config import START_IMG_URL

ban_txt = """

➻ ᴛʜɪs ɪs {1},
➻ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴛʜᴀᴛ ᴘʀᴏᴛᴇᴄᴛɪᴠᴇ ᴍᴇᴀꜱᴜʀᴇꜱ ᴀʀᴇ ɪɴ ᴘʟᴀᴄᴇ.
 ➻ ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢ ɪɴ ɢʀᴏᴜᴘ ᴠᴄ.
➻ ᴀᴅᴅᴇᴅ ᴍᴜʟᴛɪ ʟᴀɴɢᴜᴀɢᴇꜱ.
➻ ɴᴏ ʟᴀɢ.
➻ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢ.
➻ ɴᴏ ᴘʀᴏᴍᴏ.
➻ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.

ɴᴏᴛᴇ : ꜱᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.

ʙᴏᴛ ᴜꜱᴇʀɴᴀᴍᴇ : @{4}
"""
button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users"),    
        ],
        [
            InlineKeyboardButton("ꜱᴛᴀʀᴛ ɪɴ ᴘᴍ", url=f"https://t.me/{app.username}?start=help"),    
        ],

])
@app.on_message(filters.command(["promo"], prefixes=["."]))
async def start_command(client, message):
    await message.delete()
    await message.reply_photo(
                photo=START_IMG_URL,
                caption=ban_txt.format(message.from_user.mention, app.mention, message.chat.title, message.from_user.id, app.username),
                reply_markup=button)      
