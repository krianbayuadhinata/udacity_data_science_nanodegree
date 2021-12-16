# Recommendations with IBM
This project purpose is to produce a recommendations for users using user-user based collaborative filtering

## Steps
 * [Importing Library](#importing-library)
 * [Project Motivation](#project-motivation)
 * [File Descriptions](#file-descriptions)
 * [Licensing, Authors, Acknowledgements, etc.](#licensing-authors-acknowledgements-etc)


## Importing Library
 - NumPy
 - Pandas
 - Matplotlib
 - Collections
 - Pickle

## Project Motivation
This project is really interesting since it allow us to implement skills that we learned previously on how to build a recommendation engine,
We are implementing user-user based collaborative filtering that give articles recommendation to users. We can use this project as a starter and there's still room for improvement such as solving cold start problem. The project are done with several steps listed below:
  I. Exploratory Data Analysis
  II. Rank Based Recommendations
  III. User-User Based Collaborative Filtering
  IV. Matrix Factorization
  V. Extras & Concluding

## File Descriptions

Recommendations_with_IBM.ipynb # the notebook that contain steps to build the recommendation engine
Recommendations_with_IBM.html # the notebook that contain steps to build the recommendation engine saved as html
README.md   
project_test.py # script that provided by Udacity for testing purposes
top_5.p # file that downloaded from Udacity workspace
top_10.p # file that downloaded from Udacity workspace
top_20.p # file that downloaded from Udacity workspace
user_item_matrix.p # file that downloaded from Udacity workspace
data    
|- articles_community.csv # data related to articles that accesed by certain email     
|- user-item-interactions.csv # data related to articles metadata e.g articles body, articles' description, status of articles and name of the articles  


## Licensing, Authors, Acknowledgements, etc.
Licensing: Initial Script by Udacity(https://udacity.com)
Authors: Krian Bayu as the Data Scientist that finish the code (https://github.com/krianbayuadhinata/udacity_data_science_nanodegree)

Acknowledgements:
Thank you Udacity for the guidance and the initial scripts it makes me understand better about the flow of ML process.
