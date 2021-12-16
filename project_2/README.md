# Disaster Response Pipeline Project

https://www.codegrepper.com/code-examples/typescript/cannot+be+loaded+because+running+scripts+is+disabled+on+this+system.+For+more+information%2C+see+about_Execution_Policies+at+https%3A%2Fgo.microsoft.com%2Ffwlink%2F%3FLinkID%3D135170.+At+line%3A1+char%3A1

## Table of Contents
 * [Project Motivation](#project-motivation)
 * [File Descriptions](#file-descriptions)
 * [Components](#components)
 * [Instructions of How to Interact With Project](#instructions-of-how-to-interact-with-project)
 * [Licensing, Authors, Acknowledgements, etc.](#licensing-authors-acknowledgements-etc)

### Project Motivation
After spent sometimes learning data engineering skills with this project I applied data engineering skills that I learned to build an ETL Pipeline and a model that classifies disaster messages using data from [Figure Eight](https://appen.com/).
I have created a ML model to categorize which one is the fake message from messages that were sent during disaster events.
The project included with a web app where the emergency workers can input a new message and get result either the message is fake or not. The app also shows some infographic, showing data that related to the disaster events.  

### File Descriptions
app    

| - template    
| |- master.html # main page of web app    
| |- go.html # classification result page of web app    
|- run.py # Flask file that runs app    


data    

|- disaster_categories.csv # dataset    
|- disaster_messages.csv # dataset    
|- process_data.py # pipeline to clean data    
|- messages.db # saved database filename     


models   

|- train_classifier.py # machine learning pipeline     
|- classifier.pkl # saved model     


README.md    

### Components
There are three main components within this project to do ETL process, to build model and to display the result.
Points below are more detail explanation on each step.

#### 1. ETL Pipeline
`process_data.py`, the purpose of the script is to clean the data, handle duplicated data and renaming columns:
Below is the step by step that are done by developer.

 - Loads the messages and categories datasets
 - Merges the two datasets
 - Cleans the data
   - Split categories column into multiple column
   - Rename column with value of categories that has been split into two parts, and take the last part.
   - Drop duplicated rows
 - Stores it in a SQLite database as messages.db

Besides process_data.py, you can refer to `ETL Pipeline Preparation.ipynb` to follow step by step on doing ETL process.

#### 2. ML Pipeline
`train_classifier.py`, the purpose of the script is to build a Machine Learning model that able to classify whether a message considered as fake or real.
Below is the step by step that are done by developer to build Machine Learning model.

 - Load data from the SQLite database
 - Text processing: tokenize, lemmatize and remove stopwords
 - Split dataset into training and test set
 - Trains and tunes a model using Pipeline and GridSearchCV
 - Evaluate performance of the model
 - Explore other algorithm to check is there any possibility to get better result
 - Exports the final model as a .pkl file

Besides process_data.py, you can refer to `ML Pipeline Preparation.ipynb` to follow step by step on doing ETL process.

#### 3. Flask Web App
The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. The outputs are shown below:
![app3](https://user-images.githubusercontent.com/54407746/98725077-9826b800-238c-11eb-828f-864dce8cbd9b.JPG)


![app1](https://user-images.githubusercontent.com/54407746/98724735-159df880-238c-11eb-8338-bc4b4e0b1c39.JPG)


![app2](https://user-images.githubusercontent.com/54407746/98724932-5bf35780-238c-11eb-8a93-ebb09ab2d510.JPG)


### Instructions of How to Interact With Project:
1. Run the following commands in the project's directory to set up your database and model.
If you clone this Github repo, then you need to change directory into project_2

    - To install dependencies of this project please run
        `pip install -r requirements.txt`

    - To run the project first you need to run ETL Pipeline and ML Pipeline
    - To run ETL pipeline
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/messages.db`
    - To run ML pipeline
        `python models/train_classifier.py data/messages.db models/classifier.pkl`
    * `data/messages.db` or `models/classifier` after `pytho models/train_classifier.py` is parameter that can be read by system and there's a line of code that has function to obtain the value e.g. `messages_filepath, categories_filepath, database_filepath = sys.argv[1:]`


2. Run the web app.
    `python app/run.py`

3. Go to http://0.0.0.0:3001/

### Licensing, Authors, Acknowledgements, etc.
Licensing: Initial Script by Udacity(https://udacity.com)
Authors: Krian Bayu as the Data Scientist that finish the code (https://github.com/krianbayuadhinata/udacity_data_science_nanodegree)

Acknowledgements:
Thank you Udacity for the guidance and the initial scripts it makes me understand better about the flow of ML process.
