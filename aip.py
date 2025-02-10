import google.generativeai as genai

# Set up API Key
API_KEY = "AIzaSyAYB6WrfTXENxT8DLROJP-jgsHxfM7-pCU"
genai.configure(api_key=API_KEY)

# Initialize model
model = genai.GenerativeModel("gemini-pro")

def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# User input
prompt = input("Enter your prompt: ")
response = chat_with_gemini(prompt)
print("Gemini AI:", response)
