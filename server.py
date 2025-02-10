from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/compress', methods=['POST'])
def compress_audio():
    audio_url = request.json.get("url")
    output_file = "compressed.mp3"

    if not audio_url:
        return {"error": "No URL provided"}, 400

    # Descargar el audio
    subprocess.run(["wget", "-O", "input.mp3", audio_url])

    # Comprimir usando FFmpeg
    subprocess.run(["ffmpeg", "-i", "input.mp3", "-b:a", "64k", output_file])

    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
