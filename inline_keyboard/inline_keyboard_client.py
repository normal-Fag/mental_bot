from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Инлайн для практики
start_practice_markup = InlineKeyboardMarkup(row_width=2)
repeat_practice_markup = InlineKeyboardMarkup(row_width=2)

start_practice = InlineKeyboardButton("Начать практику!", callback_data='practice_start')
end_practice = InlineKeyboardButton("Отмена", callback_data='practice_end')
repeat_practice = InlineKeyboardButton("Повторить практику!", callback_data='practice_start')

start_practice_markup.add(start_practice).add(end_practice)
repeat_practice_markup.add(repeat_practice).add(end_practice)

# Инлайн для Тестов
welcome_test_markup = InlineKeyboardMarkup(row_width=2)  # Главный инлайн (выбор теста)
bool_test_markup = InlineKeyboardMarkup()  # Инлайн для теста "найди брата"
theory_test_markup = InlineKeyboardMarkup()  # Инлайн для теста "теория"

start_theory_test = InlineKeyboardButton('Теоретический тест', callback_data='test_theory')
start_boolean_test = InlineKeyboardButton('Найди брата 👀', callback_data='test_boolean')

end_test = InlineKeyboardButton('Отмена', callback_data='test_end')
test_back = InlineKeyboardButton('Назад', callback_data='test_back')

bool_test_start = InlineKeyboardButton('Начать', callback_data='booltest_start')
theory_test_start = InlineKeyboardButton('Начать', callback_data='ttest_start')

welcome_test_markup.row(start_theory_test, start_boolean_test).add(end_test)
bool_test_markup.add(bool_test_start).add(test_back)
theory_test_markup.add(theory_test_start).add(test_back)
