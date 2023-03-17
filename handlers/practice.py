import random
import time

from aiogram.types import Message, CallbackQuery
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from inline_keyboard import start_practice_markup, repeat_practice_markup
from commands import COMMAND_PRACTICE
from base_messages import PRACTICE_MESSAGE, IDLE_MESSAGE


class Answer(StatesGroup):
    answer = State()
    cache = State()


async def welcome_practice(message: Message):
    await message.answer(text=PRACTICE_MESSAGE, reply_markup=start_practice_markup, parse_mode='Markdown')
    await message.delete()


async def start_practice(callback: CallbackQuery, state: FSMContext):
    if callback.data.split('_')[1] == 'start':
        count = random.randint(3, 10)
        cache = 0

        for i in range(0, 3):
            await callback.message.edit_text(text=f'Начало через {3 - i}...')
            time.sleep(1)

        for n in range(0, count):
            rand_number = random.randint(-5, 5)
            cache += rand_number
            await callback.message.edit_text(text=f'{n}: {str(rand_number)}')
            time.sleep(0.5)

        async with state.proxy() as data:
            data['cache'] = str(cache)

        await Answer.answer.set()
        await callback.message.edit_text(text='Отправьте ответ, который у Вас получился: ')

    elif callback.data.split('_')[1] == 'end':
        await callback.message.edit_text(text=IDLE_MESSAGE)


async def get_answer(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text
        if data['cache'] == data['answer']:
            await message.answer(text='Правильно! 🥳', reply_markup=repeat_practice_markup)
        else:
            await message.answer(text=f'Неправильно!\nПравильный ответ: {data["cache"]}', reply_markup=repeat_practice_markup)

    await state.finish()
    await message.delete()


def register_practice_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome_practice, commands=COMMAND_PRACTICE)
    dp.register_callback_query_handler(start_practice, Text(startswith='practice'))
    dp.register_message_handler(get_answer, state=Answer.answer)


