#!./venv/bin/python3
import whisper

model = whisper.load_model("large")  # или "small", "medium", "large"
result = model.transcribe("video-2-text.wav")
print(result["text"])


output_text_path = "transcript.txt"
output_file = open ("video-2-text.wav", "w", encoding="utf-8")
output_file.write(result["text"])
output_file.close()

