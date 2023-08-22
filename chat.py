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


with open('intents.json') as file:
    data = json.load(file)


def chat():
    # load trained model
    model = keras.models.load_model('chat-model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    while True:
        print(Fore.LIGHTBLUE_EX + 'User: ' + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == 'quit':
            print(Fore.GREEN + 'MB Health Bot:' + Style.RESET_ALL,
                  "Take care. See you soon.")
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(
            tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + 'MB Health Bot :' + Style.RESET_ALL,
                      np.random.choice(i['responses']))


print(Fore.YELLOW + 'Start talking with MB Health Bot, your Personal Therapeutic AI Assistant. (Type quit to stop talking)' + Style.RESET_ALL)
chat()


# {"tag": "",
#  "patterns": [""],
#  "responses": [""]
# },
