import aiogram.types
from aiogram.types import ContentType
from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
users_messages = {}


def add_message_id(user_id, msg_id):
    users_messages[user_id] = msg_id
    print(users_messages)


def get_message_id(user_id):
    print(users_messages, user_id)
    return users_messages[user_id]
