
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_passport_2_3 = InlineKeyboardButton('Бухгалтерия', callback_data='bookkeeping')
inline_btn_passport_5 = InlineKeyboardButton('Открыть чат коллектива', url='https://t.me/deadlainerihackaton')
inline_btn_med_book = InlineKeyboardButton('FAQ', callback_data='faq')
inline_btn_work_book = InlineKeyboardButton('Задать вопрос', callback_data='question')
inline_btn_politic = InlineKeyboardButton('Политика конфиденциальности', url='https://case-in.ru/article/3/')
inline_full_document = InlineKeyboardMarkup(row_width=2).add(inline_btn_passport_2_3,inline_btn_passport_5,inline_btn_med_book,inline_btn_work_book,inline_btn_politic)


inline_btn_money = InlineKeyboardButton('Моя зарплата', callback_data='money')
inline_btn_prem = InlineKeyboardButton('Премия', callback_data='prem')
inline_bookkeeping = InlineKeyboardMarkup(row_width=2).add(inline_btn_money,inline_btn_prem)

inline_btn_start_down = InlineKeyboardButton('Вернуться в бухгалтерию', callback_data='bookkeeping')
inline_btn_bookkeeping_down = InlineKeyboardButton('Вернуться в главное меню', callback_data='start')
inline_bookkeeping_down = InlineKeyboardMarkup(row_width=1).add(inline_btn_bookkeeping_down,inline_btn_start_down)

inline_faq_down = InlineKeyboardMarkup(row_width=1).add(inline_btn_bookkeeping_down)