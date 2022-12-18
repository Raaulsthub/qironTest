#!pip3 install boto3
#!pip3 install audioplayer

import boto3
from audio_recorder import AudioRecorder
from time import sleep
from audioplayer import AudioPlayer
from scipy.io import wavfile



DEBUG = 1


class LexSession:
    def __init__(self, bot_id, alias_id, locale_id, session_id):
        self.client = boto3.client('lexv2-runtime')
        self.bot_id = bot_id
        self.alias_id = alias_id
        self.locale_id = locale_id
        self.session_id = session_id

    
    def make_text_request(self, request_text):
        # working text request
        return self.client.recognize_text(botId=self.bot_id, botAliasId=self.alias_id,
                                                localeId=self.locale_id, sessionId=self.session_id, text=request_text)


    
    def make_audio_request(self, audio_path):
        # future audio conversation implementation
        pass


    def text_conversation(self, bot_name):
        print('STARTING LEX AUDIO CONVERSATION WITH ' + bot_name, end='\n\n')
        sleep(1)
        while(True):
            message = str(input('Type your message to the bot: '))
            bot_response = self.make_text_request(message)
            print("Intent:",bot_response['sessionState']['intent']['name'])
            print("Next Action:",bot_response['sessionState']['dialogAction']['type'])
            try:
                print("Next Slot:",bot_response['sessionState']['dialogAction']['slotToElicit'])
            except:
                pass
            try:
                print("Prompt or Msg:",bot_response['messages'][0]['content'])
            except:
                print("Intent has been fulfilled")
                return True
            print()
        

    def audio_conversation(self, bot_name):
        print('STARTING LEX AUDIO CONVERSATION WITH ' + bot_name, end='\n\n')
        
        while(True):
            # recording audio
            print("You can talk to the bot, you've got 10 seconds to say your message: ")
            recorder = AudioRecorder()
            audio_path = recorder.record_n_save()
            if audio_path and DEBUG:
                print("Audio has been succefully recorded")
            else:
                print("Failed recording audio")


            samplerate, data = wavfile.read('./user_audio/output.wav')

            # request
            response = self.make_audio_request(self.bot_id, self.alias_id, self.locale_id, self.session_id, 'audio/l16', 'audio/mpeg', data)

            # playing it
            response["audioStream"] # this is where the audio file is located, still have to find a way to save it
            #AudioPlayer("./lex_audio/audio.EXTENSAO").play(block=True) # playing the audio file


            # still to find out a way to know when the intent is fulfilled
         

    def kill_session(self):
        response = self.client.delete_session( botId=self.bot_id, botAliasId=self.alias_id,
                                            localeId=self.locale_id, sessionId=self.session_id)

        print('SESSION HAS BEEN TERMINATED')

        


def main():
    # session id depends on the client aplication only, so it can be anything
    current_session = LexSession('ONJHYN234B', '2THUJUQ1TQ', 'pt_BR', '001')
    #if current_session.text_conversation('qiron test bot'):
         #print("CONVERSATION CAME TO AN END")
    current_session.audio_conversation('qiron_test')
    current_session.kill_session()



if __name__ == "__main__":
    main()



'''main idea:
    1. record audio
    2. request utterance
    3. get response
    4. text to speech the response with aws polly
    5. play response
    6. all over again'''

'''secondary idea:
    1. record audio
    2. send it to s3 bucket
    3. transcribe it with aws transcribe
    4. get transcription and publish text on lex
    5. get response
    6. text to speech with polly
    7. play response
    8. all over again'''