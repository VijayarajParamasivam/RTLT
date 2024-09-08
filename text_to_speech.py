import pyttsx3
from queueing import texttospeech_queue
def say():

    print("text to speech started")
    engine = pyttsx3.init()

    engine.setProperty('rate', 120)  
    engine.setProperty('volume', 1.0) 
    while True:
        if texttospeech_queue:
            text=texttospeech_queue.popleft()

            engine.say(text)

            engine.runAndWait()
