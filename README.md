# Real-Time Language Translator

## Overview

The Real-Time Language Translator is a Python-based application designed to provide real-time translation services. It uses a combination of speech recognition, transcription, translation, and text-to-speech technologies. The application runs a Streamlit web interface that allows users to start and stop the translation process with the click of a button.

## Features

- Real-time speech recognition
- Live transcription of recognized speech
- Translation of transcribed text
- Text-to-speech synthesis of translated text
- Streamlit interface for easy interaction

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/VijayarajParamasivam/RTLT.git
    cd RTLT
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:
    
      ```bash
      venv\Scripts\activate
      ```


4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

## Usage

- Open the Streamlit app in your browser.
- Click the "Start Translation" button to begin the translation process.
- Click the "Stop Translation" button to halt the process.

## Project Structure

- `app.py`: Main Streamlit application file.
- `speech_recognision.py`: Handles speech recognition functionality.
- `transcription.py`: Manages the transcription of recognized speech.
- `translation.py`: Provides translation services.
- `text_to_speech.py`: Handles text-to-speech synthesis.
- `requirements.txt`: Lists the required Python packages.

## Requirements

- Python 3.11
- Streamlit
- SpeechRecognition
- Other dependencies listed in `requirements.txt`

## Troubleshooting

- Ensure that all dependencies are properly installed.
- Verify that the virtual environment is activated.
- Check the console for any error messages.

## Contribution

Thanks to all my teammates for their efforts and contributions in this project.

## Challenges we faced

- Implementation of large language models for translation voice cloning.
- Collecting parallel corpus data (Colloquial Tamil to English) for fine tuning Helsinki-nlp/opus model.

## Future development ideas

- Using fine tuned LLM for translation.
- Implementing Voice cloning.
- Developing the product as a dialer extension.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [vijayarj.p@gmail.com](mailto:vijayarj.p@gmail.com).

