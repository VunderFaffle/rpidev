import subprocess

def main():
    # Снять кадр с камеры и сохранить в output.jpg
    subprocess.run([
        "ffmpeg", "-f", "v4l2", "-i", "/dev/video0", "-frames:v", "1", "output.jpg"
    ], check=True)
    
    # Запустить bash-скрипт с этим изображением
    subprocess.run([
        "bash", "i2s.sh", "output.jpg"
    ], check=True)

if __name__ == "__main__":
    main()
