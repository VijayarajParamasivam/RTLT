from translate import Translator
from queueing import speechtotext_queue,texttospeech_queue

def translate():
    print("Translation started")
    while True:
        if speechtotext_queue:
            translator = Translator(to_lang="en",from_lang='ta')
            text=speechtotext_queue.popleft()
            translated=translator.translate(text)
            texttospeech_queue.append(translated)