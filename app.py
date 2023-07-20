import streamlit as st
import pickle
import string
import nltk
nltk.download('stopwords')
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

# Add css to make text bigger
st.markdown(
    """
    <style>
    textarea {
        font-size: 1rem !important;
    }
    title {
        font-size: 2rem !important;
    }
    header{
        font-size: 3rem !important;
        font-color : red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center; color: red;'>SMS Spam Classifier</h1>", unsafe_allow_html=True)
st.text("\n\n")


st.markdown("<h5 style=' color: white;'>Enter the message to check! </h1>", unsafe_allow_html=True)
input_data = st.text_area('')

if st.button('Predict'):
    # preprocessing
    transform_data = transform_text(input_data)

    # vectorize
    vector_data = tfidf.transform([transform_data])

    # predict
    result = model.predict(vector_data)

    # display
    if result == 1:
        st.header(":red[Spam Detected]")
    else:
        st.header(":green[Not Spam]")

st.markdown("******")
st.markdown("""
        1. Sample Spam Message :   
                You could be entitled up to E3,16Ø in compensation from mis-sold PPI on a credit card or Loan. Please reply for info or STOP to opt out.
                
        2. Sample Ham Message : 
                Hii how are you!!!""")



st.markdown("******")
st.write(
    "Contributor : [Ankit Nainwal](https://github.com/nano-bot01) \n [LinkedIn](https://www.linkedin.com/in/ankit-nainwal1/) ")

st.write("\n© 2023 [SMS Spam Classifier using Machine Learning](https://github.com/nano-bot01/SMS-Spam-Classifier-Web-App-using-Machine-Learning).")

