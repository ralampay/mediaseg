import os
import uuid
from librosa.core import audio
import moviepy.editor as mp
from app_helper import print_error, is_avi_file
import librosa

from .transcribe import Transcribe

class Parse:
    def __init__(self, file : str =""):
        self.file = file

    def execute(self):
        if not os.path.exists(self.file):
            print_error(f"{self.file} not found")
            exit(-1)
        if not is_avi_file(self.file):
            print_error(f"{self.file} not an avi file")
            exit(-1)

        print(f"Processing {self.file}")

        video_clip = mp.VideoFileClip(self.file)

        # Extract audio
        print(f"Extracting audio...")
        audio_clip = video_clip.audio

        if audio_clip == None:
            print_error(f"No audio extracted")
            exit(-1)

        audio_dir = f"tmp"
        audio_file = f"{audio_dir}/{str(uuid.uuid4())}.mp3"
        audio_clip.write_audiofile(audio_file)

        print("Transcribing...")
        transcriber = Transcribe(audio_file=audio_file)
        transcriber.execute()
