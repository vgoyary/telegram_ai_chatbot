import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from db import save_user_data
from handlers import start, handle_contact, chat_with_gemini, handle_image

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGO_URI = os.getenv("MONGODB_HOST")

# Setup logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["telegram_bot"]
users_collection = db["users"]

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id

    # Check if user already exists
    if users_collection.find_one({"chat_id": chat_id}):
        await update.message.reply_text("You're already registered! 🎉")
        return

    # Save user data in MongoDB
    user_data = {
        "chat_id": chat_id,
        "first_name": user.first_name,
        "username": user.username
    }
    users_collection.insert_one(user_data)

    # Ask for phone number
    keyboard = [[KeyboardButton("📞 Share Phone Number", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text(f"Hi {user.first_name}! Please share your phone number to complete registration.",
                                    reply_markup=reply_markup)


# Handle phone number
async def handle_contact(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    phone_number = update.message.contact.phone_number

    # Update user in MongoDB
    users_collection.update_one({"chat_id": chat_id}, {"$set": {"phone_number": phone_number}})

    await update.message.reply_text("✅ Registration complete! You can now start chatting.")


if __name__ == "__main__":
    # Start the bot
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gemini))
    app.add_handler(MessageHandler(filters.PHOTO | filters.DOCUMENT, handle_image))

    logging.info("Bot started...")
    app.run_polling()
