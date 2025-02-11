# import google.generativeai as genai

# # Set up API Key
# API_KEY = "AIzaSyAYB6WrfTXENxT8DLROJP-jgsHxfM7-pCU"
# genai.configure(api_key=API_KEY)

# # Initialize model
# model = genai.GenerativeModel("gemini-pro")

# def chat_with_gemini(prompt):
#     response = model.generate_content(prompt)
#     return response.text

# # User input
# prompt = input("Enter your prompt: ")
# response = chat_with_gemini(prompt)
# print("Gemini AI:", response)
import google.generativeai as genai
import os

# Set up API Key (Use environment variable for security)
API_KEY = "AIzaSyAYB6WrfTXENxT8DLROJP-jgsHxfM7-pCU"  # Replace with your actual API key or set it in env
genai.configure(api_key=API_KEY)

# Initialize model
model = genai.GenerativeModel("gemini-pro")

def chat_with_gemini(prompt, max_words=50):
    """Generate a response as a comforting friend during dull or tough times."""
    try:
        system_instruction = (
            "You are a caring and understanding companion. "
            "Dont respond to out of context quetions and respond with i'm a chatbot only to assist with ur mood."
            "Your role is to provide comfort, positivity, and friendly support to the user. "
            "Respond in an empathetic and warm tone, like a good friend who listens and uplifts. "
            "Do not provide technical, factual, or impersonal responses. "
            f"Keep your response within {max_words} words."
        )
        full_prompt = f"{system_instruction}\n\nUser: {prompt}\nCompanion:"
        
        response = model.generate_content(full_prompt)
        return response.text if response.text else "I'm here for you. You're not alone. 💙"
    
    except Exception as e:
        return f"Error: {str(e)}"

# User input
prompt = input("Tell me what's on your mind: ")
response = chat_with_gemini(prompt, max_words=50)  # Adjust word limit as needed
print("Companion:", response)
