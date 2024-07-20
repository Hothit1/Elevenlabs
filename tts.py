import os
import requests
import json
import base64
from dotenv import load_dotenv

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Lấy API key từ biến môi trường
YOUR_XI_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Sử dụng ID giọng nói phù hợp nếu có giọng nói tiếng Việt
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel (thay đổi nếu có giọng nói tiếng Việt khác)
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "Content-Type": "application/json",
    "xi-api-key": YOUR_XI_API_KEY
}

data = {
    "text": (
        "xin chào các bạn "
        
    ),
    "model_id": "eleven_turbo_v2_5",  # Sử dụng mô hình Turbo v2.5
    "language_code": "vi",  # Mã ngôn ngữ cho tiếng Việt
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75,
        "style": 0.5,
        "use_speaker_boost": True
    }
}

response = requests.post(
    url,
    json=data,
    headers=headers,
)

if response.status_code != 200:
    print(f"Error encountered, status: {response.status_code}, "
          f"content: {response.text}")
    quit()

# Kiểm tra loại nội dung của phản hồi
content_type = response.headers.get('Content-Type')

if 'application/json' in content_type:
    # Chuyển đổi phản hồi chứa bytes thành chuỗi JSON từ mã hóa utf-8
    json_string = response.content.decode("utf-8")

    # Phân tích chuỗi JSON và tải dữ liệu dưới dạng từ điển
    response_dict = json.loads(json_string)

    # Mục "audio_base64" trong từ điển chứa âm thanh dưới dạng chuỗi mã hóa base64,
    # chúng ta cần giải mã nó thành bytes để lưu âm thanh dưới dạng tệp
    audio_bytes = base64.b64decode(response_dict["audio_base64"])

    with open('output_vietnamese.mp3', 'wb') as f:
        f.write(audio_bytes)

    # Mục 'alignment' chứa ánh xạ giữa các ký tự đầu vào và dấu thời gian của chúng
    print(response_dict['alignment'])
else:
    # Lưu phản hồi trực tiếp vào tệp nếu không phải là JSON
    with open('output_vietnamese.mp3', 'wb') as f:
        f.write(response.content)

    print("Audio saved to output_vietnamese.mp3")
