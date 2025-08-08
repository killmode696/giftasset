import hashlib
import logging
import asyncio
import re
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.handlers import InlineQueryHandler
from aiogram import Bot, Dispatcher, Router
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

import myutils
import config

logging.basicConfig(level=logging.DEBUG)
router = Router()
bot = Bot(token=config.BOT_API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
dp = Dispatcher()
dp.include_router(router)

@router.inline_query()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or 'Введите @username для оценки стоимости профиля'
    input_content = InputTextMessageContent(message_text=text)
    item = None
    # Проверяем, что username соответствует действительности
    if re.search(r'^@?[a-zA-Z0-9_]{4,32}$', text):
        text = text[1:] if text.startswith('@') else text

        gifts_user_data, floor_user_data, avg_user_data = myutils.get_user_gifts_by_username(text)
        formated_output = myutils.get_formated_output(text, floor_user_data, avg_user_data, gifts_user_data)
    
        input_content = InputTextMessageContent(message_text=formated_output)
        result_id: str = hashlib.md5(text.encode()).hexdigest()
        item = InlineQueryResultArticle(
            id=result_id,
            title=f"@{text} имеет {str(len(gifts_user_data))} подарков(а) стоимостью {str(floor_user_data)} TON",
            input_message_content=input_content,
        )
    else:   
        text = 'У данного пользователя нет открытых подарков'
        result_id: str = hashlib.md5(text.encode()).hexdigest()
        item = InlineQueryResultArticle(
            id=result_id,
            title=text,
            input_message_content=input_content,
            )

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=300)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())