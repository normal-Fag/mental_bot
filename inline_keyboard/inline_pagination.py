from telegram_bot_pagination import InlineKeyboardPaginator
from bot_init import bot
from aiogram.types import InputMedia


async def send_theory_page(message, page=1):
    paginator = InlineKeyboardPaginator(
        20,
        current_page=page,
        data_pattern='theory_{page}'
    )
    text = open(f'data/theory_text/{str(page - 1)}.txt', 'r').read()

    try:
        image = open(f'data/theory_image/{str(page - 1)}.jpg', 'rb')
    except:
        image = open('data/theory_image/Logo_2.png', 'rb')

    try:
        await bot.edit_message_media(
            media=InputMedia(
                type='photo',
                media=image,
                caption=text,
                parse_mode='HTML'
            ),
            chat_id=message.chat.id,
            message_id=message.message_id,
            reply_markup=paginator.markup,
        )
    except:
        print("Same page as before")
