import asyncio

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from data.test.test_data import check_theory_user, get_theory_user
from data.test.test_questions import theory_questions
from data.test.theory_test_user import TheoryTestUser
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from inline_keyboard import theory_test_markup

test_count = 8


async def send_test(user_id: int, callback: CallbackQuery):
    user: TheoryTestUser = get_theory_user(user_id)
    question = theory_questions[user.current_test]
    question_markup = InlineKeyboardMarkup()

    for option, index in zip(question['options'], range(len(question['options']))):
        question_markup.add(InlineKeyboardButton(option, callback_data=f't_answer_{index}'))

    await callback.message.edit_text(
        text=question['question'],
        reply_markup=question_markup,
        parse_mode='Markdown'
    )


async def start_theory_test(callback: CallbackQuery):
    user_id: int = callback.message.chat.id
    user: TheoryTestUser = check_theory_user(user_id)
    await send_test(user_id, callback)


async def handle_theory_answer(callback: CallbackQuery):
    user_answer: int = int(callback.data.split('_')[2])
    user_id: int = callback.message.chat.id
    user: TheoryTestUser = get_theory_user(user_id)

    if user_answer == theory_questions[user.current_test]['answer']:
        await callback.message.edit_text(
            text='Все верно !\nДвижемся дальше )'
        )
        user.correct_answers += 1
        await asyncio.sleep(2)
    else:
        await callback.message.edit_text(
            text='Неверно !\nВам стоило бы повторить теорию, но сначала закончим с тестом..'
        )
        await asyncio.sleep(2)

    if user.current_test == test_count - 1:
        await callback.message.edit_text(
            text=f'На этом тест закончен ! 🥳\nПоздравляю !\n'
                 f'Вы ответили правильно на _{user.correct_answers}_ из _{test_count}_ вопросов.\n'
                 f'Хотите повторить тест ?',
            parse_mode='Markdown',
            reply_markup=theory_test_markup
        )
        user.current_test = 0
        user.correct_answers = 0
        return

    user.current_test += 1
    await send_test(user_id, callback)


def register_theory_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_theory_test, Text('ttest_start'))
    dp.register_callback_query_handler(handle_theory_answer, Text(startswith='t_answer'))
