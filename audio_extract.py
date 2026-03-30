#!./venv/bin/python3
from moviepy import VideoFileClip

video = VideoFileClip("video-2-text.mp4")
audio_path = "video-2-text.wav"
video.audio.write_audiofile(audio_path, codec='pcm_s16le')
