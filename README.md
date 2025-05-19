# AI ChatBot with Speech Capabilities

This is a full-stack AI chatbot application that allows users to interact with an AI using voice commands. The application features speech-to-text, AI response generation, and text-to-speech capabilities.

## Features

- Voice recording in the browser
- Speech-to-text conversion
- AI response generation using OpenAI
- Text-to-speech conversion
- Modern and responsive UI
- Real-time chat interface

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Modern web browser with microphone access

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Start the Flask backend:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Click the record button to start speaking. The application will:
   - Record your voice
   - Convert it to text
   - Generate an AI response
   - Convert the response to speech
   - Play the response

## Project Structure

- `app.py`: Flask backend with routes for transcription and response generation
- `templates/index.html`: Frontend interface with HTML, CSS, and JavaScript
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (create this file)

## Technologies Used

- Backend:
  - Flask
  - OpenAI API
  - SpeechRecognition
  - gTTS (Google Text-to-Speech)

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (ES6+)
  - Web Audio API

## Security Notes

- Never commit your `.env` file or expose your API keys
- The application requires microphone access in the browser
- All audio processing is done locally before being sent to the server

## License

MIT License 