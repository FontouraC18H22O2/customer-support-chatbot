# 🤖 Customer Support Chatbot

An AI-powered customer support chatbot with a web widget interface, built with Python and Google Gemini API.

## Features

- AI responses based on a customizable knowledge base
- Conversation history maintained throughout the session
- Automatic escalation to human agent when needed
- Ready-to-use chat widget embeddable in any website
- Secure API key management with environment variables

## Tech Stack

- Python 3
- Google Gemini API
- Flask
- HTML / CSS / JavaScript

## Installation

1. Clone the repository
   git clone https://github.com/your-username/customer-support-chatbot.git
   cd customer-support-chatbot

2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
   Copy .env.example to .env and add your API key

5. Customize the bot
   Edit the system_prompt in servidor.py with your company info and FAQ

6. Run the server
   python servidor.py

7. Open index.html in your browser

## Project Structure

customer-support-chatbot/
├── servidor.py        # Flask backend server
├── bot.py             # Terminal version of the bot
├── index.html         # Chat widget frontend
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── .gitignore         # Git ignored files

## Customization

To adapt this bot to your business, edit the system_prompt
in servidor.py with:
- Your company name and description
- Products or services you offer
- Return and shipping policies
- Payment methods
- Support hours

## License

MIT
