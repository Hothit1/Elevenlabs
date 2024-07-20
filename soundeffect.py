import os
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


def generate_sound_effect(text: str):
    # Tạo tên tệp đầu ra từ văn bản mô tả
    output_path = f"{text.replace(' ', '_').lower()}.mp3"
    print(f"Generating sound effect for '{text}'...")

    result = elevenlabs.text_to_sound_effects.convert(
        text=text,
        duration_seconds=10,
        prompt_influence=0.3,
    )

    with open(output_path, "wb") as f:
        for chunk in result:
            f.write(chunk)

    print(f"Audio saved to {output_path}")


if __name__ == "__main__":
    generate_sound_effect("train nunning through city")
