from pathlib import Path
from openai import OpenAI


# Initialize OpenAI client
client = OpenAI()

# Streamlit interface
st.title('Text-to-Speech with OpenAI')
user_input = st.text_input('Enter the text you want to convert to speech:')

if st.button('Convert to Speech'):
    if user_input:
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=user_input
        )
        
        response.stream_to_file(speech_file_path)
        
        if speech_file_path.exists():
            st.success('The response has been saved to speech.mp3.')
        else:
            st.error('Failed to save the response to file.')
    else:
        st.warning('Please enter some text to convert.')