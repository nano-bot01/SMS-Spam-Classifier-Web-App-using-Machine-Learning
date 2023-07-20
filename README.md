# SMS-Spam-Classifier-Web-App-using-Machine-Learning
SMS Spam Classifier Web Application which is used to classify spam and ham in text messages we receive in phones


## How it works
- The app uses a machine learning model to classify SMS messages. The model is trained on a dataset of SMS messages that have been labeled as spam or ham. The model works by extracting features from the SMS messages, such as the length of the message, the number of exclamation points, and the presence of certain keywords. The features are then used to train a classifier, which predicts whether a new SMS message is spam or ham.

- The machine learning model is trained using a technique called supervised learning. In supervised learning, the model is given a set of labeled data, and it learns to predict the labels for new data. The labeled data for this app is a dataset of SMS messages that have been labeled as spam or ham.

- The classifier used in this app is a support vector machine (SVM). SVMs are a type of machine learning model that are known for their accuracy and robustness. SVMs work by finding a hyperplane that separates the spam messages from the ham messages.

<hr>

## The ipynb file
The ipynb file contains the code for training and evaluating the machine learning model. The file also contains the code for the web app. The code is well-organized and easy to follow. The comments provide helpful explanations of the code.

The ipynb file is divided into three sections:

* Data loading and preprocessing: This section loads the dataset of SMS messages and preprocesses the data. The preprocessing steps include removing punctuation, converting all letters to lowercase, and stemming the words.
* Model training: This section trains the machine learning model. The model is trained using the scikit-learn library.
* Web app: This section creates the web app. The web app is built using the Flask framework.


## Files
- app.py - The main file that runs the app.
- models.py - The file that contains the machine learning model.
- preprocessing.py - The file that contains the preprocessing functions.
- templates/index.html - The HTML template for the web app.

## To-Do
1. Add more features to the web app, such as the ability to train the model on a custom dataset.
2. Improve the accuracy of the machine learning model.
License
This project is licensed under the MIT License.


## Application of spam classifier

Spam classifiers can be used to:

* Identify and block spam messages.
* Reduce the amount of spam that users receive.
* Protect users from phishing attacks.
* Improve the accuracy of spam filters.


## Contributor : [Ankit Nainwal](https://github.com/nano-bot01) 
