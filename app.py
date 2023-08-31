import streamlit as st
import pickle
import numpy as np
from tensorflow import keras
import json

# Load data from 'intents.json'
with open('intents.json') as file:
    data = json.load(file)

# Load model, tokenizer, and label encoder
model = keras.models.load_model('chat-model')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)


def get_bot_response(user_input):
    max_len = 20
    result = model.predict(keras.preprocessing.sequence.pad_sequences(
        tokenizer.texts_to_sequences([user_input]), truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])[0]

    for intent in data['intents']:
        if intent['tag'] == tag:
            response = np.random.choice(intent['responses'])
            return response

    return "I'm sorry, I don't understand that."


def main():
    st.sidebar.title("MB Health Bot")
    st.title("Chat with MB Health Bot")

    st.write("Start talking with MB Health Bot, your Personal Therapeutic AI Assistant. (Type quit to stop talking)")
    user_input = st.text_input("You: ")

    if user_input.lower() == 'quit':
        st.write("MB Health Bot: Take care. See you soon.")
    else:
        bot_response = get_bot_response(user_input)
        st.write("MB Health Bot:", bot_response)


if __name__ == "__main__":
    main()