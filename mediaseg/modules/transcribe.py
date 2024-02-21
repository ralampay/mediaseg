import whisper
from os.path import isfile
from datetime import timedelta
from moviepy.editor import *

class Transcribe:
    def __init__(self, audio_file='', device='cpu', whisper_model='small'):
        self.audio_file     = audio_file
        self.device         = device
        self.whisper_model  = whisper_model
        self.conversation   = ""

    def execute(self):
        self.model = whisper.load_model(self.whisper_model)
        self.model.to(self.device)

        self.transcription  = self.model.transcribe(audio=self.audio_file)
        self.text           = self.transcription['text']
        self.segments       = self.transcription['segments']

        self.content = []

        #print(self.transcription)

        self.ave_speech_len = 0.0

        for segment in self.segments:
            segment_start   = segment['start']
            segment_end     = segment['end']

            self.ave_speech_len += segment_end - segment_start

            start_time  = str(0) + str(timedelta(seconds=int(segment['start'])))
            end_time    = str(0) + str(timedelta(seconds=int(segment['end'])))
            text        = segment['text']
            id          = segment['id'] + 1

            self.content.append({
                'id': id,
                'text': text,
                'start_time': start_time,
                'end_time': end_time,
                'segment_start': segment_start,
                'segment_end': segment_end
            })

            #print(f"Segment {id}: {segment_start}:{segment_end}...")

            output = f"id: {id}\n{start_time} - {end_time}\n{text}\n\n"
            self.conversation += output

        self.ave_speech_len = self.ave_speech_len / len(self.segments)
