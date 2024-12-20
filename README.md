# Spam SMS Detection

This project aims to classify SMS messages as either "spam" or "ham" (non-spam) using machine learning techniques. The model leverages natural language processing (NLP) to analyze the content of SMS messages and determine their classification.The project is seccesfully deployed on streamlit cloud.
Live dashboard : https://spam-sms-detection-home.streamlit.app/

## Table of Contents
1. [Introduction](#introduction)  
2. [Dataset Overview](#dataset-overview)  
3. [Data Preprocessing](#data-preprocessing)  
4. [Model Building](#model-building)  
5. [Results and Evaluation](#results-and-evaluation)  
6. [Visualizations](#visualizations)  
7. [Dependencies](#dependencies)  
8. [Contributor](#contributor)  

## Introduction  
Spam SMS detection is a critical application of machine learning and NLP that helps filter unwanted messages. This project uses a dataset of labeled SMS messages to train a model that accurately classifies new messages.

## Dataset Overview  
- **Dataset:** The dataset used is the Spam SMS dataset, which contains 5,572 entries with two main columns:
  - `is_spam`: Indicates whether the message is spam (1) or ham (0).
  - `sms`: The actual text of the SMS message.
 
  - link of the dataset : https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Data Preprocessing  
The following preprocessing steps are performed on the dataset:
1. **Loading Data**: The dataset is loaded using pandas.
2. **Data Cleaning**: Unwanted columns are dropped, and column names are renamed for clarity.
3. **Text Normalization**: Messages are converted to lowercase, and stopwords and punctuation are removed.
4. **Feature Engineering**: Additional features such as word count, sentence count, and number count are calculated for each message.

## Model Building  
The model is built using the following steps:
1. **TF-IDF Vectorization**: Text data is transformed into numerical vectors using the TF-IDF method.
2. **Model Training**: A Multinomial Naive Bayes classifier is trained on the processed features.

## Results and Evaluation  
The performance of the model is evaluated using metrics such as:
- **Accuracy**: The proportion of correctly classified messages.
- **Classification Report**: Includes precision, recall, and F1-score for both spam and ham classes.

## Visualizations  
Various visualizations are created to analyze the data:
- Bar charts showing the distribution of spam vs ham messages.
- Pie charts representing the percentage of spam messages in the dataset.
- Word clouds for visualizing common words in spam and ham messages.

## Dependencies  
To run this project, ensure you have the following libraries installed:
- Python 3.x
- pandas
- numpy
- nltk
- sklearn
- matplotlib
- seaborn

## Contributor
- **Tejas Sinroja**: Project development, model design, and implementation.
- Feel free to contribute by suggesting improvements or reporting issues via GitHub!
