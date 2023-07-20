import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords  # for removing stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('model/vectorizer.pkl', 'rb'))
model = pickle.load(open('model/model.pkl', 'rb'))

st.title("SMS Spam Classifier")

input_data = st.text_input("Enter the message to check! ")

if st.button('Predict'):
    # preprocessing
    transform_data = transform_text(input_data)

    # vectorize
    vector_data = tfidf.transform([transform_data])

    # predict
    result = model.predict(vector_data)

    # display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

