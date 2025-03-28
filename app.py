from flask import Flask, render_template, request, jsonify, send_from_directory
from stt import transcribe_audio
from chat import get_chat_response
from tts import generate_speech
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stt", methods=["POST"])
def speech_to_text():
    audio_file = request.files["file"]
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)
    
    text = transcribe_audio(audio_path)
    return jsonify({"text": text})

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json["text"]
    response_text = get_chat_response(user_text)
    
    audio_filename = generate_speech(response_text)
    return jsonify({"response": response_text, "audio_url": f"/static/audio/{audio_filename}"})

@app.route("/static/audio/<path:filename>")
def serve_audio(filename):
    return send_from_directory("static/audio", filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
