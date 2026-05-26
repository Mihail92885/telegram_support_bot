import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8984601449:AAG6ba4Jp8XHPIzuY6CeLY7vP6iSQNf60KQ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот техподдержки. Задай вопрос.")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Напиши свой вопрос, я помогу.")

@dp.message()
async def answer(message: types.Message):
    text = message.text.lower()
    if "принтер" in text:
        await message.answer("Проверь бумагу, питание, перезагрузи принтер.")
    elif "интернет" in text:
        await message.answer("Проверь кабель, перезагрузи роутер, ipconfig.")
    elif "ккм" in text:
        await message.answer("Проверь питание ККМ, связь с драйвером.")
    else:
        await message.answer("Опиши проблему подробнее — я помогу.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
