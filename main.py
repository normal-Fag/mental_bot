from aiogram import executor
from bot_init import dp
from handlers import base, theory, practice, test

base.register_base_handlers(dp)
theory.register_theory_handlers(dp)
practice.register_practice_handlers(dp)
test.register_test_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
