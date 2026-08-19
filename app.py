from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import time
import pdfplumber

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=API_KEY)

models = [
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite"
]

@app.route('/')
def serve_index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/extract-pdf', methods=['POST'])
def extract_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/review', methods=['POST'])
@app.route('/review', methods=['POST'])
def review_resume():
    resume_text = request.json.get('resume')
    
    prompt = (
        "You are an expert HR professional and career coach. "
        "Review this resume and provide detailed feedback on: "
        "1. Overall impression "
        "2. Strengths "
        "3. Areas to improve "
        "4. Missing sections "
        "5. Specific suggestions "
        f"Be constructive, specific and helpful.\n\nResume:\n{resume_text}"
    )
    
    for model in models:
        try:
            chat = client.chats.create(model=model)
            print(f"Trying model: {model}")
        except Exception as e:
            print(f"{model} unavailable: {e}")
            time.sleep(1)
            continue

        try:
            response = chat.send_message(prompt)
            print(f"Success with: {model}")
            return jsonify({'feedback': response.text})
        except Exception as e:
            print(f"Error with prompt/message on {model}: {e}")
            return jsonify({'feedback': f'There was an issue processing your resume: {str(e)}'}), 500

    return jsonify({'feedback': 'All models busy, please try again in a moment!'})

if __name__ == '__main__':
   
    app.run(debug=True, port=5001)
