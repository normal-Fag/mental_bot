import asyncio
import random

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, PollAnswer
from aiogram.dispatcher.filters import Text
from data.test.test_data import check_brother_user, BrotherTestUser, get_brother_user
from bot_init import bot
from inline_keyboard import bool_test_markup


async def send_question(user_id: int):
    user: BrotherTestUser = get_brother_user(user_id)
    user.create_question()
    current_question = user.current_question

    poll = await bot.send_poll(
        chat_id=user_id,
        question='Найди брата',
        options=user.question['options'],
        correct_option_id=user.question['answer'],
        open_period=user.time_to_answer,
        type='quiz',
        is_anonymous=False,
    )
    user.poll_id = poll.poll.id

    await asyncio.sleep(user.time_to_answer)
    if user.poll_id == poll.poll.id and current_question < 5:
        user.current_question += 1
        await send_question(user_id)
    elif user.poll_id == poll.poll.id and current_question == 5:
        await bot.send_message(chat_id=user_id, text=f'Game over\n{user.correct_answers}')


async def start_bool_test(callback: CallbackQuery):
    u_id = callback.message.chat.id

    user: BrotherTestUser = check_brother_user(u_id)
    user.create_question()

    poll = await callback.message.answer_poll(
        question='Найди брата',
        options=user.question['options'],
        correct_option_id=user.question['answer'],
        type='quiz',
        is_anonymous=False,
        open_period=user.time_to_answer
    )
    user.poll_id = poll.poll.id
    await asyncio.sleep(user.time_to_answer)

    if user.poll_id == poll.poll.id:
        user.current_question += 1
        await send_question(u_id)


async def handle_bool_test_answer(poll_answer: PollAnswer):
    user_id = poll_answer.user.id
    user_answer = poll_answer.option_ids[0]
    user: BrotherTestUser = get_brother_user(user_id)

    if user_answer == user.question['answer']:
        user.correct_answers += 1

    if user.current_question == 5:
        user.poll_id = -1
        lvl = user.level
        user.level = lvl + 1 if user.correct_answers == 5 and lvl < 3 else lvl
        if lvl == 3:
            level_info_text = 'Вы уже достигли максимального уровня в данном тесте 🥳\n' \
                              'Но вы все равно можете продолжить оттачивать ваши навыки в _Ментальной арифметике_.\n'
        else:
            level_info_text = f'Ваш уровень остался прежним - _{lvl}_\n' if lvl == user.level \
                else f'Вы достигли нового уровня!\nТеперь ваш уровень – _{lvl + 1}_'
        await bot.send_message(
            chat_id=user_id,
            text=f'Тест окончен 🥳\nКоличество правильных ответов: _{user.correct_answers} / 5_\n{level_info_text}'
                 f'Хотите начать тест заново ?',
            parse_mode='Markdown',
            reply_markup=bool_test_markup
        )
    else:
        user.current_question += 1
        await send_question(user_id)


def register_bool_test_handler(dp: Dispatcher):
    dp.register_callback_query_handler(start_bool_test, Text('booltest_start'))
    dp.register_poll_answer_handler(handle_bool_test_answer)
