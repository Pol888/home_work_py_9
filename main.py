from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler
import t  # токен
import record_log
import bot_function


if __name__ == '__main__':
    record_log.l()
    application = ApplicationBuilder().token(t.tk).build()

    start_handler = CommandHandler('start', bot_function.start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), bot_function.echo)
    caps_handler = CommandHandler('caps', bot_function.caps)
    inline_caps_handler = InlineQueryHandler(bot_function.inline_caps)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)

    # ==========================================================================
    Agata_handler = CommandHandler('hello', bot_function.Agata)
    Agata_multiplication = CommandHandler('go', bot_function.multiplication)
    Agata_interpreter = CommandHandler('a', bot_function.interpreter)

    application.add_handler(Agata_handler)
    application.add_handler(Agata_multiplication)
    application.add_handler(Agata_interpreter)

    application.run_polling()
