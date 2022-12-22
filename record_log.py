import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler


# модуль логов ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def l():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def l_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('log.txt', 'a', encoding='utf-8') as file_file:
        file_file.write(str(update) + '\n')

