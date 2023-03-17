from commands import COMMAND_TEST
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from inline_keyboard import welcome_test_markup, bool_test_markup, theory_test_markup
from base_messages import IDLE_MESSAGE, TEST_MESSAGE
from aiogram.dispatcher.filters import Text
from handlers.test_brother import register_bool_test_handler
from handlers.test_theory import register_theory_handlers


async def welcome_test(message: Message):
    await message.answer(
        text=TEST_MESSAGE,
        reply_markup=welcome_test_markup,
        parse_mode='Markdown'
    )


async def handle_test(callback: CallbackQuery):
    answer = callback.data.split('_')[1]
    if answer == 'end':
        await callback.message.edit_text(text=IDLE_MESSAGE)
    elif answer == 'back':
        await callback.message.edit_text(
            text=TEST_MESSAGE,
            reply_markup=welcome_test_markup,
            parse_mode='Markdown'
        )
    elif answer == 'boolean':
        await init_bool_test(callback)
    elif answer == 'theory':
        await init_theory_test(callback)


async def init_bool_test(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Суть следующего теста - найти пример, где необходимо применить правило _Брат_.\n'
             'Учти, что среди представленных примеров может и не быть нужного 😉',
        parse_mode='Markdown',
        reply_markup=bool_test_markup
    )


async def init_theory_test(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Данный тест направлен на проверку ваших теоретических значний по пройденноому материалу.',
        parse_mode='Markdown',
        reply_markup=theory_test_markup
    )


def register_test_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome_test, commands=COMMAND_TEST)
    dp.register_callback_query_handler(handle_test, Text(startswith='test'))
    register_bool_test_handler(dp)
    register_theory_handlers(dp)
