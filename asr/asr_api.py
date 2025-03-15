from flask import Flask, request, jsonify
import librosa
import torch
import os
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC


app = Flask(__name__)

# Load the model and processor once when app is started
processor = Wav2Vec2Processor.from_pretrained(
    "facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/asr', methods=['POST'])
def asr():
    file_path = request.form.get('file')
    # Check if file exists
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    # Load and calculate duration of audio
    audio, rate = librosa.load(file_path, sr=16000)
    duration = librosa.get_duration(y=audio, sr=rate)
    # Perform inference
    input_values = processor(audio, return_tensors="pt",
                             padding='longest').input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    # Format the return output
    transcription = processor.batch_decode(predicted_ids)
    output = [{'transcription': transcription[0], 'duration': duration}]
    return jsonify(output)
