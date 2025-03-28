# from google.cloud import texttospeech
# import uuid
# import os

# # Ensure the static/audio directory exists
# os.makedirs("static/audio", exist_ok=True)

# # Initialize the Text-to-Speech client
# client = texttospeech.TextToSpeechClient()

# def generate_speech(text):
#     print('reached generate speech')
#     # Set up the input text for synthesis
#     synthesis_input = texttospeech.SynthesisInput(text=text)
    
#     # Configure the voice parameters
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US",
#         ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#     )
    
#     # Specify the audio configuration
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )
    
#     # Perform text-to-speech synthesis
#     response = client.synthesize_speech(
#         input=synthesis_input,
#         voice=voice,
#         audio_config=audio_config
#     )
    
#     # Generate a unique filename for the output audio file
#     filename = f"{uuid.uuid4()}.mp3"
#     file_path = os.path.join("static/audio", filename)
    
#     # Write the synthesized audio to the file
#     with open(file_path, "wb") as out:
#         out.write(response.audio_content)
    
#     return filename


import openai
import uuid
import os

# Ensure the static/audio directory exists
os.makedirs("static/audio", exist_ok=True)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_speech(text):
    print('Reached generate_speech')
    
    # Perform text-to-speech synthesis
    response = openai.audio.speech.create(
        model="tts-1",  # Use the appropriate TTS model
        input=text,
        voice="alloy"  # Choose a voice from available options
    )
    
    # Generate a unique filename for the output audio file
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join("static/audio", filename)
    
    # Write the synthesized audio to the file
    with open(file_path, "wb") as audio_file:
        audio_file.write(response.content)
    
    return filename


