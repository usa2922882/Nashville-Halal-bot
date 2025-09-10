from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = "8210249353:AAFvDJZgX2O-aSVLaxKjbp9Sg0J3pT770uo"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Bot ishga tushdi ✅")

if __name__ == '__main__':
    print("Bot ishga tushyapti...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
