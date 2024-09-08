import streamlit as st
import speech_recognision
import transcription
import translation
import text_to_speech
from multiprocessing.pool import ThreadPool
import time

def start_translation():


    pool = ThreadPool(processes=4)

    pool.apply_async(speech_recognision.main)
    pool.apply_async(transcription.main)
    pool.apply_async(translation.translate)
    pool.apply_async(text_to_speech.say)

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        st.write("Exiting...")
        pool.terminate()

def main():
    st.title("Real-Time Translator")

    st.write("Press the button below to start the real-time translation process.")

    if st.button('Start Translation'):
        start_translation()
        st.write("Translation process started. Check the console for updates.")

if __name__ == "__main__":
    main()
