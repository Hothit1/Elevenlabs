# ElevenLabs  Project

Dự án này sử dụng API của ElevenLabs để thực hiện các tác vụ liên quan đến xử lý âm thanh và giọng nói.

## Cài đặt

### Yêu cầu
- Python 3.6+

### Các gói cần thiết
Cài đặt các gói sau bằng pip:

```
pip install requests python-dotenv
```

### Tạo file .env
1. Tạo một file có tên `.env` trong thư mục gốc của dự án.
2. Thêm API key của ElevenLabs vào file `.env` như sau:

```
ELEVENLABS_API_KEY=your_api_key_here
```

Thay `your_api_key_here` bằng API key thực của bạn từ ElevenLabs.

## Cách sử dụng

1. Đảm bảo bạn đã cài đặt tất cả các gói cần thiết và tạo file `.env` với API key hợp lệ.

2. Import các module cần thiết trong mã Python của bạn:

```python
import os
import requests
import json
import base64
from dotenv import load_dotenv
```

3. Tải các biến môi trường từ file `.env`:

```python
load_dotenv()
```

4. Lấy API key từ biến môi trường:

```python
YOUR_XI_API_KEY = os.getenv("ELEVENLABS_API_KEY")
```

5. Bây giờ bạn có thể sử dụng `YOUR_XI_API_KEY` để thực hiện các yêu cầu API đến ElevenLabs.

## Lưu ý bảo mật

- Không bao giờ commit file `.env` vào kho lưu trữ git của bạn.
- Thêm `.env` vào file `.gitignore` để tránh vô tình commit.

## Hỗ trợ

Nếu bạn gặp bất kỳ vấn đề nào hoặc có câu hỏi, vui lòng mở một issue trong kho lưu trữ này.
