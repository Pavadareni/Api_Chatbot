from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# accessing and printing value
key = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)
CORS(app)

# Set up Gemini API key
genai.configure(api_key=key)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)

        reply = response.text if hasattr(response, "text") else "Sorry, I couldn't understand that."
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
