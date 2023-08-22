# MB Health Bot - THERAPEUTIC AI ASSISTANT

Classic therapy scenes in Hollywood films show a distraught client reclining on a colorful Victorian sofa and recounting their troubles. The psychotherapist ponders in a leather chair, while the client’s concerns are revealed to be tied to some early experiences. Most therapy in the real world hasn’t looked like this in ages. However, these scenes get one thing right: the therapist in the room is **human**. <br>

Today, as the need for mental health services continues to surpass availability, people in distress can reach out online to mental health “chatbots.” In some instances, the responses are based on artificial intelligence (AI). In others, there’s a human element.

But the question remains: Is it possible to automate the expertise needed to become an effective therapist, using sophisticated algorithms and programming, when humans spend a lifetime trying to master these skills?

# CHATBOTS

Chatbots are systems that can carry on extended conversations with the goal of mimicking the unstructured conversations or ‘chats’ characteristic of informal human-human interaction.

# MB Health Bot

**MB Health Bot** is a conversational agent designed to mimic a psychotherapist in order to provide emotional support to people with anxiety & depression.
At its core, MB Health Bot is a chatbot trained on a text dataset using Deep Learning and Natural Language Processing techniques.

MB Health Bot can provide general advice regarding anxiety and depression, answer questions related to mental health and make daily conversations. MB Health Bot is obviously not a licensed physician, and it does not make diagnoses or write prescriptions. MB Health Bot offers help and support rather than treatment. MB Health Bot is not equipped to deal with real mental health crises either. When it senses someone is in trouble, it suggests they seek help in the real world and provides text and hotline resources. MB Health Bot doesn’t seek to remove the human element in therapy either but is rather a “gateway therapy,” to give people a good first experience, and even help them realise when they need a more intense form of intervention.

# HOW TO RUN THIS REPOSITORY?

First, clone this repository.

Install the necessary libraries using:

```
pip install -r requirements.txt
```

Train the model using:

```
python model.py
```

Now run MB Health Bot using:

```
python chat.py
```

You can modify MB Health Bot by inserting your own text in the `intents.json` file.

# A CONVERSATION WITH MB Health Bot

![sample-chat](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGKQwZ1rMoht6X4a_6ghuuQR9BinxXoipk7dWGd6py5evjaXU8xV-FsUVZ4EcbQmAqBLRWZ8pcyMLBlZHttnsK-MCS-XzCQdgqheJXiBnj7fB34aZ_0vM-1vudsSEt8pUUTJwN1ZMNAeabDkjWEtEVowtfRdDTXjGsvJAEVt4SfiEz6v5tQrkjlWr4plsC/s1600/Demo.png)

# DATASET

https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data

# FUTURE WORK

- [ ] Fine-tune using GPT-3.
