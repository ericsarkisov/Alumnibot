import aiogram.dispatcher
from aiogram import Bot
from aiogram import types
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token = TOKEN)
dp = aiogram.dispatcher.Dispatcher(bot)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_hi2_1 = KeyboardButton('Принимаю!')
button_hi2_2 = KeyboardButton('Не принимаю!')
button_hi2_3 = KeyboardButton('Вернуться назад!')
greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi2_1, button_hi2_2, button_hi2_3)

button_hi3_1 = KeyboardButton('Вернуться назад!')
greet_kb3 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi3_1)


button_hi1_1 = KeyboardButton('Добавить резюме! 📄')
button_hi1_2 = KeyboardButton('Добавить вакансию! 📰')
button_hi1_3 = KeyboardButton('Посмотреть резюме! 📄')
button_hi1_4 = KeyboardButton('Посмотреть вакансии! 📰')
button_hi1_5 = KeyboardButton('Вернуться назад! 🖕')
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi1_1, button_hi1_2, button_hi1_3, button_hi1_4, button_hi1_5)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply("Привет. Что ты хочешь?", reply_markup=greet_kb1)

@dp.message_handler(content_types=['text'])
async def process_help_command1(message: types.Message):
	if message.text == 'Вернуться назад! 🖕':
	await message.answer('Ну и пошел на *** и без тебя норм было. https://t.me/joinchat/IVO-EOWcruyJb3ED')
	elif message.text == 'Добавить резюме! 📄':
	await message.answer("В случае потери данной информации создатели бота не несут ответственость", reply_markup=greet_kb2)
if message.text == "Принимаю!":
	await message.answer("Напиши своё Фамилию и Имя через пробел пример: Эрнест Эдуардович", reply_markup=greet_kb3)
	A = message.text
	f = A.split('')
	for i in range(len(A)):
	if f[i] == ' ':
	if f[i+1] != ' ' and f[i+1] != '':
	await message.answer("Напишите свой опыт работы в годах, если у вас его нет напишите 0", reply_markup=greet_kb3)
	B = message.text
	f = B.split('')
	for i in range(len(B)):
	if f[i] == '1' or f[i] == '2' or f[i] == '3' or f[i] == '4' or f[i] == '5' or f[i] == '6' or f[i] == '7' or f[i] == '8' or f[i] == '9':
	await message.answer("Напишите в чат своё резюме", reply_markup=greet_kb3)
								C = message.text
							if message.text == "Вернуться назад!":
								process_help_command1()
						else:
							await message.answer("Вы написали не согласно образцу", reply_markup=greet_kb3)
							if message.text == "Вернуться назад!":
								process_help_command1()
					else:
						await message.answer("Вы написали не согласно образцу", reply_markup=greet_kb3)
						if message.text == "Вернуться назад!":
						process_help_command1()
		if message.text == "Вернуться назад!":
			process_help_command1()
		elif message.text == "Не принимаю!":
			await message.answer("Ничем не могу вам помочь", reply_markup=greet_kb3)
			if message.text == "Вернуться назад!":
				process_help_command1()
	elif message.text == 'Добавить вакансию! 📰':
		await message.answer("В случае потери данной информации создатели бота не несут ответственость", reply_markup=greet_kb2)
		if message.text == "Принимаю!":
			await message.answer("Напиши своё Фамилию и Имя через пробел пример: Эрнест Эдуардович", reply_markup=greet_kb3)
			A = message.text
			f = A.split('')
			for i in range(len(A)):
				if f[i] == ' ':
					if f[i+1] != ' ' and f[i+1] != '':
						await message.answer("Напишите свой опыт работы в годах, если у вас его нет напишите 0", reply_markup=greet_kb3)
						B = message.text
						f = B.split('')
						for i in range(len(B)):
							if f[i] == '1' or f[i] == '2' or f[i] == '3' or f[i] == '4' or f[i] == '5' or f[i] == '6' or f[i] == '7' or f[i] == '8' or f[i] == '9':
								await message.answer("Напишите в чат своё резюме", reply_markup=greet_kb3)
								C = message.text
							if message.text == "Вернуться назад!":
								process_help_command1()
							else:
								await message.answer("Вы написали не согласно образцу", reply_markup=greet_kb2)
								if message.text == "Вернуться назад!":
									process_help_command1()
					else:
						await message.answer("Вы написали не согласно образцу", reply_markup=greet_kb2)
						if message.text == "Вернуться назад!":
							process_help_command1()
		else:
			await message.answer("Ничем не могу вам помочь", reply_markup=greet_kb2)
			if message.text == "Вернуться назад!":
				process_help_command1()
	elif message.text == 'Посмотреть резюме! 📄':
		await message.answer('Все что-ли а не много тебе? Из какой гильдии тебе нужно резюме')
	elif message.text == 'Посмотреть вакансии! 📰':
		await message.answer("Все что-ли а не много тебе? Из какой гильдии тебе нужно вакансию")



if __name__ == '__main__':
	executor.start_polling(dp)
