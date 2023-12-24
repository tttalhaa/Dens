 from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client: Client, message: Message):
	await message.reply_text(f"Merhaba {message.from_user.mention}, ben [BLACK KED]",
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"kanal", url=""
						)
				],
				[
					InlineKeyboardButton(
						"➕  Botu Bir Gruba Ekle ➕", url="?startgroup=true"
						)
				]
			]
		)
	)
