import speech_recognition as sr
from queueing import recognised_audio,speechtotext_queue

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    try:
        transcription = recognizer.recognize_google(audio_data, language='ta-IN')
        return transcription
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    
def main():
    print("Transcription Started")
    while True:
        if recognised_audio:
            audio_file=recognised_audio.popleft()
            transcription = transcribe_audio(audio_file)
            if not transcription:
                continue
            speechtotext_queue.append(transcription)