from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import data_base as db
import keyboards as kb
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, '''
      Привет, я чат-бот, который поможет тебе освоиться в нашем коллективе ''',
                           )
    await bot.send_message(message.chat.id, "Я могу сделать следущее. \n(нажми на интересующую "
                                            "кнопку ниже)", reply_markup=kb.inline_full_document)


@dp.callback_query_handler(lambda c: c.data == 'bookkeeping')
async def some_callback_bookkeeping(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что именно ты хочешь узнать в бухгалтерии?',
                           reply_markup=kb.inline_bookkeeping)


@dp.callback_query_handler(lambda c: c.data == 'start')
async def some_callback_start(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Я могу сделать следущее. \n(нажми на интересующую "
                                                        "кнопку ниже)", reply_markup=kb.inline_full_document)


@dp.callback_query_handler(lambda c: c.data == 'money')
async def some_callback_money(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваша заработная плата за этот месяц \n** ***.** рублей',
                           reply_markup=kb.inline_bookkeeping_down)


@dp.callback_query_handler(lambda c: c.data == 'prem')
async def some_callback_prem(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'К сожалению, в этом месяце ты не попал в ТОП-10 сотрудников \nВ следущем месяце пострайся попасть в него',
                           reply_markup=kb.inline_bookkeeping_down)


@dp.callback_query_handler(lambda c: c.data == 'faq')
async def some_callback_faq(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Q:Что может этот бот? \nA:В данном боте Вы можете узнать свою зарплату, премию, перейти в чат сотрудников или же почитать нашу политику конфиденциальности ',
                           reply_markup=kb.inline_faq_down)


@dp.callback_query_handler(lambda c: c.data == 'question')
async def some_callback_question(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'В разработке',
                           )

if __name__ == '__main__':
    executor.start_polling(dp)



