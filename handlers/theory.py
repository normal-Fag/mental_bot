from commands import COMMAND_THEORY
from inline_keyboard import send_theory_page
from telegram_bot_pagination import InlineKeyboardPaginator
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class TheoryBook(StatesGroup):
    page_number = State()


async def start_theory(message: types.Message, state: FSMContext):
    # Достаем страницу на которой остановился пользователь
    data = await state.get_data()
    current_page = data.get('page_number')

    try:
        text = open(f'data/theory_text/{current_page - 1}.txt').read()
    except:
        text = open('data/theory_text/0.txt').read()
        current_page = 0

    start_theory_paginator = InlineKeyboardPaginator(
        20,
        current_page=current_page,
        data_pattern='theory_{page}'
    )

    await message.answer_photo(
        photo=open('data/theory_image/Logo_2.png', 'rb'),
        caption=text,
        reply_markup=start_theory_paginator.markup,
        parse_mode='HTML'
    )


async def update_theory(callback: types.CallbackQuery, state: FSMContext):
    page = int(callback.data.split('_')[1])

    # Записываем текущую страницу в state
    async with state.proxy() as data:
        data['page_number'] = page

    await send_theory_page(callback.message, page)
    await callback.answer()


def register_theory_handlers(dp: Dispatcher):
    dp.register_message_handler(start_theory, commands=COMMAND_THEORY)
    dp.register_callback_query_handler(update_theory, Text(startswith='theory'))