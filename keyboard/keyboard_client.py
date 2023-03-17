from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from commands import COMMAND_HELP, COMMAND_THEORY, COMMAND_TEST, COMMAND_PRACTICE

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

button_help = KeyboardButton('/' + COMMAND_HELP)
button_theory = KeyboardButton('/' + COMMAND_THEORY)
button_practice = KeyboardButton('/' + COMMAND_PRACTICE)
button_test = KeyboardButton('/' + COMMAND_TEST)

kb_client.row(button_theory, button_test).row(button_practice, button_help)
