import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from db import save_user_data, save_chat_history
from gemini import get_gemini_response, analyze_image

# Handle /start command
async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    chat_id = update.message.chat.id
    first_name = user.first_name
    username = user.username

    # Register user in MongoDB if not already registered
    save_user_data(chat_id, first_name, username)

    # Ask for phone number
    keyboard = [["📞 Share Phone Number"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text(f"Hi {first_name}, please share your phone number to complete registration.",
                                    reply_markup=reply_markup)

# Handle phone number submission
async def handle_contact(update: Update, context: CallbackContext):
    user = update.message.from_user
    chat_id = update.message.chat.id
    phone_number = update.message.contact.phone_number

    # Update phone number in MongoDB
    save_user_data(chat_id, None, None, phone_number)

    await update.message.reply_text("✅ Registration complete! You can now start chatting.")

# Handle chat with Gemini (text input)
async def chat_with_gemini(update: Update, context: CallbackContext):
    user_input = update.message.text
    chat_id = update.message.chat.id

    # Get response from Gemini
    bot_response = get_gemini_response(user_input)

    # Save chat history to MongoDB
    timestamp = datetime.datetime.now()
    save_chat_history(chat_id, user_input, bot_response, timestamp)

    # Send response to user
    await update.message.reply_text(bot_response)

# Handle file analysis (image/file input)
async def handle_image(update: Update, context: CallbackContext):
    file = update.message.photo[-1].get_file()
    file.download("image_to_analyze.jpg")

    # Analyze image with Gemini
    description = analyze_image("image_to_analyze.jpg")

    # Save file metadata to MongoDB
    chat_id = update.message.chat.id
    timestamp = datetime.datetime.now()
    save_chat_history(chat_id, "Image uploaded", description, timestamp)

    # Send analysis description to user
    await update.message.reply_text(f"Image description: {description}")
