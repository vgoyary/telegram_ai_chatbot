from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGODB_HOST")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["telegram_bot"]
users_collection = db["users"]
chat_history_collection = db["chat_history"]

def save_user_data(chat_id, first_name, username, phone_number=None):
    """Save user data into MongoDB"""
    if users_collection.find_one({"chat_id": chat_id}) is None:
        users_collection.insert_one({
            "chat_id": chat_id,
            "first_name": first_name,
            "username": username,
            "phone_number": phone_number
        })

def save_chat_history(chat_id, user_input, bot_response, timestamp):
    """Save chat history into MongoDB"""
    chat_history_collection.insert_one({
        "user_input": user_input,
        "bot_response": bot_response,
        "chat_id": chat_id,
        "timestamp": timestamp
    })
