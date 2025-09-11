
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes
from config import ADMIN_ID
from menu_data import MENU_CATEGORIES, PRICES
from pdf_generator import generate_pdf
from utils import calculate_distance_miles

cart = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[category] for category in MENU_CATEGORIES.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📋 MENU dan tanlang:", reply_markup=reply_markup)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in MENU_CATEGORIES:
        buttons = [[item] for item in MENU_CATEGORIES[text]]
        buttons.append(["⬅️ Orqaga"])
        reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        await update.message.reply_text(f"{text}:", reply_markup=reply_markup)
    elif text in PRICES:
        user_id = update.message.from_user.id
        cart.setdefault(user_id, {})
        cart[user_id][text] = PRICES[text]
        await update.message.reply_text(f"✅ {text} savatga qo‘shildi.")
    elif text == "⬅️ Orqaga":
        await start(update, context)

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = (update.message.location.latitude, update.message.location.longitude)
    miles = calculate_distance_miles(user_location)
    await update.message.reply_text(f"📍 Sizdan masofa: {miles} mil
Yetkazib berish narxi: ${miles}")

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone = update.message.contact.phone_number
    await update.message.reply_text(f"📞 Telefon raqamingiz: {phone}")

async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("💬 Fikringiz uchun rahmat!")
