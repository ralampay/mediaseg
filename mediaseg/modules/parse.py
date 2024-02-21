import os
import uuid
from librosa.core import audio
import moviepy.editor as mp
from ..app_helper import print_error, is_avi_file
import librosa

from .transcribe import Transcribe

class Parse:
    def __init__(self, file : str ="", threshold : int =5, will_segment=False):
        self.file           = file
        self.threshold      = threshold
        self.will_segment   = will_segment

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
        self.transcriber = Transcribe(audio_file=audio_file)
        self.transcriber.execute()

        print(f"Average Speech Length: {self.transcriber.ave_speech_len}")

        if self.will_segment:
            segments = self.transcriber.segments
            current_start_segment = segments[0]['start']
            for i, segment in enumerate(segments):
                segment_start   = segment['start']
                segment_end     = segment['end']

                # Check if there's a next segment
                if i == len(segments) - 1:
                    sub_clip = video_clip.subclip(current_start_segment, segment_end)
                    sub_clip.write_videofile(f"tmp/{i}.mp4", codec="libx264")
                    sub_clip.close()

                elif i + 1 < len(segments):
                    next_segment = segments[i+1]
                    next_start_time = next_segment['start']
                    time_diff = next_start_time - segment_end

                    # Check if the time difference exceeds the threshold
                    if time_diff > self.threshold:
                        sub_clip = video_clip.subclip(current_start_segment, segment_end)
                        sub_clip.write_videofile(f"tmp/{i}.mp4", codec="libx264")
                        sub_clip.close()

                        current_start_segment = next_start_time

        video_clip.close()
