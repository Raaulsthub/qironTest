import numpy as np
import pandas as pd
import boto3
from audio_recorder import AudioRecorder


DEBUG = 1


class LexSession:
    def __init__(self, bot_id, alias_id, locale_id, session_id):
        self.client = boto3.client('lexv2-runtime')
        self.bot_id = bot_id
        self.alias_id = alias_id
        self.locale_id = locale_id
        self.session_id = session_id

    
    def make_request():
        recorder = AudioRecorder()
        a = recorder.record_n_save()
        if a and DEBUG:
            print("audio recorded...")

    def kill_session(self):
        response = self.client.delete_session( botId=self.bot_id, botAliasId=self.alias_id,
                                            localeId=self.locale_id, sessionId=self.session_id)


class TranscribeSession:
    def __init__(self):
        self.client = boto3.client('transcribe')
    
    def transcribe(self, file_uri, job_name, lenguage_code, media_format):
        response = self.client.start_transcription_job()


class S3Session:
    def __init__(self):
        self.client = boto3.client('s3')

    def send_audio(self):
        pass
    
        


def main():
    # session id depends on the client aplication only, so it can be anything
    current_session = LexSession('to_be_created', 'to_be_created', 'en_US', '001')



if __name__ == "__init__":
    main()



'''main idea:
    1. record audio
    2. send audio to be stored to s3 bucket
    3. send stored audio to be transcribed in aws transcribe
    4. get transcription and publish on lex
    5. get response
    6. text to speech the response with aws polly
    7. play response
    8. all ver again'''

'''secondary idea:
    1. record audio
    2. transcribe it with another api (maybe google's)
    3. get transcription and publish on lex
    4. get response
    5. text to speech with polly
    6. play response
    7. all over again'''