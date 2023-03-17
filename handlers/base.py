from aiogram import types, Dispatcher
from keyboard import kb_client
from commands import COMMAND_START, COMMAND_HELP
from base_messages import START_MESSAGE, HELP_MESSAGE
from bot_init import add_message_id, get_message_id, bot


async def start_bot(message: types.Message):
    first_msg = await message.answer(START_MESSAGE, reply_markup=kb_client, parse_mode='Markdown')
    add_message_id(first_msg.chat.id, first_msg.message_id)


async def show_help(message: types.Message):
    await message.answer(HELP_MESSAGE, reply_markup=kb_client, parse_mode='Markdown')


async def chmonya(message: types.Message):
    with open('data/chmonya.jpeg', 'rb') as photo:
        await message.reply_photo(photo=photo, caption='Chmonya 😽')


def register_base_handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=COMMAND_START)
    dp.register_message_handler(show_help, commands=COMMAND_HELP)
    dp.register_message_handler(chmonya, regexp='(^chmonya[s]?$|chmonya)')

