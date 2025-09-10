from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from generate_pdf import generate_pdf

BOT_TOKEN = "8210249353:AAFvDJZgX2O-aSVLaxKjbp9Sg0J3pT770uo"

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Bot ishga tushdi ✅")

# /check komandasi - PDF chek yuboradi
async def send_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_data = {
        "items": [
            {"name": "🍕 Pizza", "qty": 2, "price": 10},
            {"name": "🥤 Cola", "qty": 1, "price": 2}
        ],
        "total": 22,
        "customer_name": "Sancho Sari",
        "phone": "+16151234567",
    }

    pdf_file_path = generate_pdf(order_data)

    with open(pdf_file_path, 'rb') as pdf:
        await update.message.reply_document(document=pdf, filename="check.pdf")

if __name__ == '__main__':
    print("Bot ishga tushyapti...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("check", send_check))  # Yangi komandani qo‘shdik
    application.run_polling()
