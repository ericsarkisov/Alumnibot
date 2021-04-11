from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token ='1630616274:AAHr_eFfIxxQCGv-8Q1Em4xFiwmk3yAkQ5E')
dp = Dispatcher(bot)

class commands:

	@dp.message_handler(commands=['start'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Привет, я Helper')
	    	await bot.send_message(message.chat.id, ''' 
	    		Вот что я могу:
	    		1. /write_to_administrator - Написать администратору
	    		2. /back - Вернутся к выбору чата
	    		3. /contacts - Контакты
	    		4. /regulations - Правила
	    		4. /Add_resume - Загрузить резюме
	    		5. /Add_vacancy -  Загрузить вакансию
	    		6. /View_vacancies - Посмотреть вакансии
	    		7. /View_resume - Посмотреть резюме
	    		''')

	@dp.message_handler(commands=['add_resume'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Перейдите в личные сообщения к боту(это сделано для защиты вашего резюме от посторонних).Вот ссылка на бота @dhfvsdgsdhlgfbot ')
	@dp.message_handler(commands=['view_vacancies'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Перейдите в личные сообщения к боту(это сделано для защиты вакансии от посторонних).Вот ссылка на бота @dhfvsdgsdhlgfbot ')
	@dp.message_handler(commands=['view_resume'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Перейдите в личные сообщения к боту(это сделано для защиты резюме от посторонних).Вот ссылка на бота @dhfvsdgsdhlgfbot ')
	@dp.message_handler(commands=['add_vacancy'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Перейдите в личные сообщения к боту(это сделано для защиты вашей вакансии от посторонних).Вот ссылка на бота @dhfvsdgsdhlgfbot ')
	@dp.message_handler(commands=['write_to_administrator'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Вот админ: @ERIC_SARKISOV')

	@dp.message_handler(commands=['back'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Вот ссылка https://t.me/joinchat/IVO-EOWcruyJb3ED')
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

	@dp.message_handler(commands=['contacts'])
	async def start_messages(message):
	    	await bot.send_message(message.chat.id, 'Контактов нет')

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)

	
