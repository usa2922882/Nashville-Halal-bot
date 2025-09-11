
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import BOT_TOKEN
from handlers import start, handle_menu, handle_location, handle_contact, handle_feedback

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))
    app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    app.add_handler(CallbackQueryHandler(handle_feedback, pattern="^feedback_"))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
