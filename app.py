from flask import Flask, request, jsonify, render_template # type: ignore
from flask_cors import CORS # type: ignore
from gtts import gTTS # type: ignore
import os
import tempfile
import base64
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000"]}}, supports_credentials=True)

# Simple response templates
RESPONSES = [
    "I understand what you're saying about {topic}. That's interesting!",
    "Tell me more about {topic}.",
    "That's a fascinating point about {topic}. What made you think of that?",
    "I see what you mean about {topic}. Could you elaborate?",
    "That's an interesting perspective on {topic}. How do you feel about it?",
]

def generate_response(text):
    # Extract key topics from the text (simple version)
    words = text.lower().split()
    topics = [word for word in words if len(word) > 4]  # Simple topic extraction
    if not topics:
        topics = ["that"]
    topic = random.choice(topics)
    response_template = random.choice(RESPONSES)
    return response_template.format(topic=topic)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate_response_route():
    print("Received request for /generate_response")
    try:
        text = request.json.get('text')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        # Generate response using our simple template system
        response = generate_response(text)
        # Convert response to speech
        tts = gTTS(text=response, lang='en')
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
            tts.save(temp_audio.name)
            temp_audio_path = temp_audio.name
        with open(temp_audio_path, 'rb') as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')
        os.unlink(temp_audio_path)
        return jsonify({
            'text': response,
            'audio': f'data:audio/mp3;base64,{audio_base64}'
        })
    except Exception as e:
        import traceback
        error_message = f"Error in /generate_response: {e}\n{traceback.format_exc()}\n"
        print(error_message)
        with open("error.log", "a") as f:
            f.write(error_message)
        return jsonify({'error': str(e)}), 500

@app.route('/generate_response', methods=['OPTIONS'])
def handle_options():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True) 