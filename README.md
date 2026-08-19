AI Resume Reviewer 📄🤖

An AI-powered resume analysis tool that provides instant feedback and improvement suggestions using Google Gemini AI.

Features
📄 Paste your resume for analysis
🤖 AI-powered resume feedback using Google Gemini
📝 Feedback on resume content and structure
💡 Suggestions for improving your resume
🎨 Simple and clean web interface
Tech Stack
Python
Flask
Google Gemini API
HTML
CSS
JavaScript

How to Run
1. Clone the repository
git clone YOUR_REPOSITORY_URL
cd resume-reviewer
2. Install the required packages
pip install flask google-genai python-dotenv
3. Add your Gemini API key

Create a .env file in the project folder and add:

GEMINI_API_KEY=your_api_key_here

Important: Never upload your API key to GitHub. Make sure .env is included in your .gitignore file.

4. Run the application
py -3.13 app.py

Open the local URL shown in your terminal to use the application.
