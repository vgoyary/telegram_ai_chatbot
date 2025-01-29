import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load Gemini API key from environment variable
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API key
palm.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt):
    """Get response from Gemini API"""
    response = palm.generate_text(prompt=prompt)
    return response.result

def analyze_image(image_path):
    """Analyze image using Gemini (basic placeholder for image analysis)"""
    description = palm.generate_text(prompt=f"Describe the content of this image: {image_path}")  # Modify this for actual image analysis
    return description.result
