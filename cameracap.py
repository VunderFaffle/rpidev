import subprocess
from openai import OpenAI
import os

subprocess.run(["ffmpeg", "-f", "v4l2", "-i", "/dev/video0", "-frames:v", "1", "output.jpg"], check=True)
subprocess.run(["bash", "i2s.sh", "output.jpg"], check=True)

cwd = os.path.dirname(os.path.abspath(__file__))

def encode_image(path: str) -> str:
    import base64
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    if path.lower().endswith(".png"):
        mime = "image/png"
    elif path.lower().endswith((".jpg", ".jpeg")):
        mime = "image/jpeg"
    else:
        mime = "application/octet-stream"
    return f"data:{mime};base64,{data}"


client = OpenAI(
    api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNlNDdhMmNmLTNjY2EtNGMwNy1hNzg0LTRlNTQ0NWI4OTEyNCIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3NTA0MDk4MjAsImV4cCI6MjA2NTk4NTgyMH0._UYefX0QtUEByZne0q2Rf2y2wZDvaqnBOC4wh3X2uBg',
    base_url='https://bothub.chat/api/v2/openai/v1'
)

def ask(image_path: str):
    img_data_url = encode_image(f"{cwd}/{image_path}")
    content = [
    {
        "type": "text",
        "text": "Что на этом изображении?"
    },
    {
        "type": "image_url",
        "image_url": {"url": img_data_url}
    }]
    chat_completion = client.chat.completions.create(
        model="gpt-4.1",  
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return chat_completion.choices[0].message.content

print(ask("output.jpg"))