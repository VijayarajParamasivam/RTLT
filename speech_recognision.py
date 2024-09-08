import pyaudio
import io
import wave
import numpy as np
import time
from queueing import recognised_audio

# Configuration
SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16
CHUNK = 1024  
SILENCE_THRESHOLD = 500
PAUSE_DURATION = 1.5  

def is_silent(data_chunk):
    audio_data = np.frombuffer(data_chunk, dtype=np.int16)
    amplitude = np.abs(audio_data).mean()
    return amplitude < SILENCE_THRESHOLD

def record_audio(stream, audio):

    print("Recording audio...")
    frames = []
    start_time = time.time()
    last_sound_time = start_time
    
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        
        if not is_silent(data):
            last_sound_time = time.time() 

        if time.time() - last_sound_time > PAUSE_DURATION:
            break
    
    print("Recording stopped due to pause.")
    
 
    audio_file = io.BytesIO()
    with wave.open(audio_file, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(b''.join(frames))
    
    audio_file.seek(0) 
    return audio_file

def main():

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, input=True, frames_per_buffer=CHUNK)
    
    print("Speech recognition started")
    try:
        while True:

            audio_file = record_audio(stream, audio)
            recognised_audio.append(audio_file)
            

            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:

        stream.stop_stream()
        stream.close()
        audio.terminate()

if __name__ == "__main__":
    main()
