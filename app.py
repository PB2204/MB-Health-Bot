import streamlit as st
import pickle
import random
from colorama import Fore, Style, Back
import colorama
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
import json
import numpy as np
import warnings

warnings.filterwarnings("ignore")
colorama.init()

# Load 'data' variable at the top level
with open('intents.json') as file:
    data = json.load(file)

# Define functions to load model, tokenizer, and label encoder


@st.cache_resource
def load_model():
    model = keras.models.load_model('chat-model')
    return model


@st.cache_resource
def load_tokenizer():
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer


@st.cache_resource
def load_label_encoder():
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    return lbl_encoder


def main():
    st.sidebar.title("MB Health Bot")
    st.title("Chat with MB Health Bot")

    st.write("Start talking with MB Health Bot, your Personal Therapeutic AI Assistant. (Type quit to stop talking)")
    user_input = st.text_input("You: ")

    if user_input.lower() == 'quit':
        st.write("MB Health Bot: Take care. See you soon.")
    else:
        model = load_model()
        tokenizer = load_tokenizer()
        lbl_encoder = load_label_encoder()
        max_len = 20

        result = model.predict(keras.preprocessing.sequence.pad_sequences(
            tokenizer.texts_to_sequences([user_input]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for intent in data['intents']:
            if intent['tag'] == tag:
                response = np.random.choice(intent['responses'])
                st.write("MB Health Bot:", response)


if __name__ == "__main__":
    main()