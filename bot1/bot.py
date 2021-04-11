from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot(token="1696303269:AAEWHC_3UxNZacJRDa_HjbhzLgWxU7ltNNg")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!")
    await message.answer('''Вот что я могу:
    	/where_can_i_go - варианты гильдий
    	/who_are_your_creators - теги создателей
    	/regulations - правила
    	''')


@dp.message_handler(commands=['Where_can_i_go'])
async def process_start_command(message: types.Message):
    await message.answer('''
    Вот куды ты можешь попасть :
    1. Гильдия психологов и педагогов https://t.me/joinchat/H-fDzt-QLJN_EemK
    2. Гильдия архитекторов, дизайнеров https://t.me/joinchat/IrIXVyTFoDjuHSJf
    3. Гильдия инженеров и IT специалистов https://t.me/joinchat/IvMQBQgBeqFMZ6ZG
    4. Гильдия специалистов естественно-научного направления https://t.me/joinchat/U-nyx-3FXoV3XR1G
    5. Гильдия гуманитариев https://t.me/joinchat/GWRQ6WI8_LB2Fm5x
    6. Гильдия экономистов, управленцев и социологов https://t.me/joinchat/H_lDEVJHIxo_03hu
    Выбирайте! 
    ''')



@dp.message_handler(commands=['Who_are_your_creators'])
async def process_start_command(message: types.Message):
	await message.answer('''
	Создатели:
    @WertopHop
    @Helper_Mistake
    ''')

@dp.message_handler(commands=['regulations'])
async def process_start_command(message: types.Message):
	await message.answer('''
	Правила чатов Цифровых гильдий выпускников Южного федерального университета:
    ВСЕГДА – “да” режиму 24х7 на отправку сообщений;
    ОБО ВСЕМ – “да” любым темам для обсуждения, кроме религиозных и политических;
    БЕЗ ХЛАМА – “нет” использованию стикеров;
    БЕЗ ФЛУДА – “нет” массовым ответам на поздравления вида "присоединяюсь к поздравлениям!" (хотите поздравить именинника? напишите ему личное сообщение!);
    БЕЗ ПОНТОВ – “нет” снобизму и личным оскорблениям – каждый имеет право на мнение, но мнение о других людях в чате лучше держать при себе.
    ''')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
