import whisper
from os.path import isfile
from datetime import datetime, timedelta
from moviepy.editor import *

class Transcribe:
    def __init__(self, audio_file='', device='cpu', whisper_model='small', base_time=datetime.now()):
        self.audio_file         = audio_file
        self.device             = device
        self.whisper_model      = whisper_model
        self.conversation       = ""
        self.base_time          = base_time
        self.datetime_format    = "%Y-%m-%d %H:%M:%S"

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

            sec_start   = int(segment['start'])
            sec_end     = int(segment['end']) 

            start_time  = str(0) + str(timedelta(seconds=sec_start))
            end_time    = str(0) + str(timedelta(seconds=sec_end))
            text        = segment['text']
            id          = segment['id'] + 1

            start_timestamp = self.base_time + timedelta(seconds=sec_start)
            end_timestamp   = self.base_time + timedelta(seconds=sec_end)

            self.content.append({
                'id': id,
                'text': text,
                'start_time': start_time,
                'end_time': end_time,
                'segment_start': segment_start,
                'segment_end': segment_end,
                'start_timestamp': start_timestamp.strftime(self.datetime_format),
                'end_timestamp': end_timestamp.strftime(self.datetime_format)
            })

            #print(f"Segment {id}: {segment_start}:{segment_end}...")

            output = f"id: {id}\n{start_time} - {end_time}\n{text}\n\n"
            self.conversation += output

        self.ave_speech_len = self.ave_speech_len / len(self.segments)
