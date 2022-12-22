from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler
import math
from translate import Translator  # переводчик
import record_log


# функции бота ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):  # ответ на /start
    record_log.l_msg(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello Кожаный!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):  # эхо - отвечает тем же.
    record_log.l_msg(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):  # /caps text - text с большой буквы
    record_log.l_msg(update, context)
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):  # inline запрос
    record_log.l_msg(update, context)
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
async def Agata(update: Update, context: ContextTypes.DEFAULT_TYPE):
    record_log.l_msg(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет Агатa!!!")


async def multiplication(update: Update, context: ContextTypes.DEFAULT_TYPE):  # умножение - /go цифра цифра цифра
    record_log.l_msg(update, context)
    magic = math.prod(map(int, context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Привет Агатa! ответ = {magic}!!!")


async def interpreter(update: Update, context: ContextTypes.DEFAULT_TYPE):  # переводчик /a text
    record_log.l_msg(update, context)
    tr = Translator(from_lang='en', to_lang='ru')
    end_text = tr.translate(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=end_text)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++