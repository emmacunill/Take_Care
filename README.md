# Take Care : Project Documentation

![Portada del Proyecto](https://github.com/emmacunill/final_project/blob/main/presentation/Slide%2016_9%20-%2016.png?raw=true)

## Overview

In a world where trends evolve rapidly, technologies advance continuously, and self-reflection becomes essential, "Take Care" offers a viable solution for young adults and teens. 

This project revolves around the use of artificial intelligence to address mental health concerns.

## Table of Contents

1. [Libraries & Dependancies](#libraries-&-dependancies)
2. [Workflow](#workflow)
3. [Approaches](#approaches)
4. [Step by Step Process](#step-by-step-process)
5. [Next Steps](#next-steps)


## Libraries & Dependancies

**Python Libraries:**
- **Pandas:** A powerful data manipulation library.
- **Scikit-learn:** A machine learning library providing simple and efficient tools for data analysis.
- **XGBoost:** An optimized distributed gradient boosting library.
- **H2O:** Used for ensemble models and distributed machine learning.
- **Matplotlib:** A comprehensive library for creating static, animated, and interactive visualizations.
- **Streamlit:** Rapid App Prototyping for Data Science

- **Other:** Seaborn / re / os / emoji / langid / Translator / random / numpy / sklearn.metrics / pyplot / pymysql / sys / math / Counter / openai / time / concurrent.futures / GoogleTranslator / WordCloud / stopwords / word_tokenize. Amongst others. 

**Data Visualization and Presentation:**
- **Figma** 
- **Tableau** 

**Database:**
- **SQL** (Structured Query Language) 

## Workflow

The project follows a structured workflow:

- **Data Acquisition:** Obtain and preprocess WhatsApp conversations.
- **Emotion Detection Model Training:** Train an XGBClassifier for emotion detection using vectorization.
- **Emotion Aggregation:** Aggregate emotions on a daily, weekly, and monthly basis.
- **Results Exploration:** Visualize and explore results using Figma, SQL queries, and Tableau.
- **Future Emotional States Prediction:** Use a new dataset to predict emotional states for the upcoming month.
- **Autoregularization:** Implement a self-care time recommender and most frequent words used, including a Streamlit interface.

## Approaches

**For Mental Health Professionals**

Mental health professionals can leverage SQL queries, views, Tableau visualizations and most frequent words used to gain insights into patients emotional patterns.

**For Users or Patients**

Users benefit from the autoregularization feature, receiving personalized self-care time recommendations.

## Step by Step Process

**1. Detecting and Tracking Emotions through AI from WhatsApp Conversations**

- **Exporting Conversations:** Conversations from WhatsApp are exported and transformed into CSV format.

- **Automated Export & Import Function:** A function is provided for automating the export of the zip of Whatsapp conversations, and importing the new CSV into the notebooks, streamlining the process.

- **Data Cleaning:** Emojis are replaced with their corresponding descriptions, and columns such as date, time, name, and message are created for better organization. Irrelevant messages are filtered out, excluding personal messages. Dataframes are concatenated for comprehensive analysis.

- **Translation Attempts:** An attempt is made to translate the messages, considering the multilingual nature of the data. Because of the impossibility of translation, Manual categorization of a representative sample (1000 messages) into 20 emotion categories is performed due to the diversity of languages and the number of categories.

- **Model Selection:** Ten different models, including bootstrapping and H2O ensemble models, are experimented with. The XGBClassifier emerges as the winning model.

- **Application of Trained Model:** The trained XGBClassifier is applied to the entire dataset for emotion detection.

- **Emotion-Weighted Aggregation:** Daily, weekly, and monthly emotional peaks are obtained through weighted aggregation.

- **Results Exploration:** Figma schemas provide visual representations of emotional patterns. SQL queries and views are used for accessing updated data. Tableau visualizations offer insights into patterns and emotional stories for mental health professionals.

![Tableau](https://github.com/emmacunill/final_project/blob/main/videos/Tableau_example.png?raw=true)

**2. Predicting Future Emotional States**

- **Obtaining New Dataset:** The initial dataset is merged with incorporating daily, weekly, and next month monthly max emotions datasets. 

- **Model Training:** A new model is trained to predict future emotional states by finding new patterns.

- **Model Application:** The trained model is applied to the dataset to predict emotional states for the upcoming month (e.g., The maximum emotion for December will be: Happiness.)



**3. Autoregularization**

- **Self-Care Time Recommender:** 
An autoregularization feature recommends personalized self-care time for users based on emotional states.

- **Most frequent words used:** 
It provides via Wordcloud useful information for Mental health professionals to pinpoint the origin of possible patterns.

**Streamlit Implementation:**
Integrate the self-care time recommender and most frequent words used into a Streamlit app for a user-friendly interface and real-time information. 

## Next Steps

- **Implement Neural Networks:** Unsupervised methodology using Neural Networks to improve accuracy.
- **Recommender:** Professionality & Standarize.
- **Analysis:** Deeper understanding of own patterns.
- **Generator:** Generate songs insted of listing.
- **Emotions:** Understanding of more complex combinations as emotions rarely go one by one.

## LINKS

[Canva presentation](https://www.canva.com/design/DAF2HyPDCoE/LOeff3M0OJKUF4Fj6V3_bQ/edit?utm_content=DAF2HyPDCoE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton "Canva Presentation Link")


