# -*- coding: utf-8 -*-
"""SPCHATBOT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a5_gdvJxYETc-9p6937NjVoPRozVc5ZL
"""


import nltk
import streamlit as st
import speech_recognition as sr


# Load and preprocess chatbot data
def load_chatbot_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    pairs = [line.strip().split('::') for line in data if '::' in line]
    return {q.lower(): a for q, a in pairs}

chatbot_data = load_chatbot_data('/content/chatdata.txt')

chatbot_data = load_chatbot_data('chatdata.txt')

def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening for your input...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that. Could you please repeat?"
        except sr.RequestError:
            return "There was an issue connecting to the speech recognition service."

def chatbot_response(user_input):
    user_input = user_input.lower()
    response = chatbot_data.get(user_input, "I'm sorry, I don't understand that.")
    return response

# Streamlit app
st.title("Speech-Enabled Chatbot")

st.write("You can interact with the chatbot via text or speech input.")

# Input Options
input_mode = st.radio("Choose your input mode:", ('Text', 'Speech'))

if input_mode == 'Text':
    user_input = st.text_input("Type your message:")
    if user_input:
        response = chatbot_response(user_input)
        st.write("Chatbot:", response)

elif input_mode == 'Speech':
    if st.button("Speak"):
        user_speech = transcribe_speech()
        st.write("You said:", user_speech)
        response = chatbot_response(user_speech)
        st.write("Chatbot:", response)



