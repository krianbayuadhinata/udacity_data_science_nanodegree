import sys
import pandas as pd
import numpy as np
import sqlalchemy
import matplotlib.pyplot as py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.model_selection import GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import pickle

def load_data(database_filepath):
    """
    Load data from database.

    Parameters:
    database_filepath: Filepath to the database

    Returns:
    X: Independent variables or features
    y: Target or dependent variable
    """

    # load data from database
    engine = sqlalchemy.create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table("messages", con=engine)
    X = df['message']
    y = df.iloc[:, 4:]
    category_names = y.columns

    return X, y, category_names


def tokenize(text):
    """
    Tokenize and lemmatize input text.

    Parameters:
    text: input text that needs to pass tokenize and lemmatize process

    Returns:
    cleaned: tokenized and lemmatized text
    """
    tokenized = word_tokenize(text)

    lemmatizer = WordNetLemmatizer()

    cleaned=[]
    for word in tokenized:
        cleaned.append(lemmatizer.lemmatize(word).lower().strip())

    return cleaned

def build_model():
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    parameters = {
        'clf__estimator__n_estimators' : [10, 20]
    }

    cv = GridSearchCV(pipeline, param_grid=parameters, cv = 5, n_jobs = 5)

    return cv

def evaluate_model(model, X_test, y_test, category_names):
    """
    Print model evaluation with classification report.

    Parameters:
    model: classifier
    X_test: independent variables used for testing / features
    Y_test: target variable used for testing

    Output:
    Printed classification report.
    """
    y_pred = model.predict(X_test)
    for message, target in enumerate(y_test):
        print(target)
        print(classification_report(y_test[target], y_pred[:, message]))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    print(sys.argv)

    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/messages.db classifier.pkl')


if __name__ == '__main__':
    main()
