import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
TIME = 10
AUDIO_PATH = './audio/output.wav'

class AudioRecorder:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format = FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    def record_n_save(self):
        frames = []
        seconds = TIME

        print("recording")

        for i in range(int(RATE/CHUNK*seconds)):
            data = self.stream.read(CHUNK)
            frames.append(data)

        print('recording stopped')

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(AUDIO_PATH, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        return AUDIO_PATH

