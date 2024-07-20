import os
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from dotenv import load_dotenv

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Lấy API key từ biến môi trường
api_key = os.getenv("ELEVENLABS_API_KEY")

# Khởi tạo client ElevenLabs với API key
client = ElevenLabs(api_key=api_key)

def stream_voice(text: str):
    print(f"Streaming voice for text: '{text}'...")

    # Tạo luồng âm thanh từ văn bản
    audio_stream = client.generate(
        text=text,
        stream=True
    )

    # Phát trực tiếp âm thanh
    stream(audio_stream)

if __name__ == "__main__":
    while True:
        text = input("Enter text to stream (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        stream_voice(text)
