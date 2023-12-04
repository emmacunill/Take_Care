import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/transformed_df/emsemotions.csv') 

st.set_page_config(
    page_title="Emotions distribution",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {
            background-color: #252525;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
            background-color: #252525;
        }
   
        .stMarkdown h1 {
            color: #CF73B0;
            text-align: center;
            font-family: 'TT Commons Pro', monospace;
            font-weight: 400;
        }    
        .stMarkdown h3 {
            color: #D6D278;
            text-align: center;
            font-family: 'TT Commons Pro', monospace;
            font-size: 18px;
            font-weight: 500;
        }
        .stMarkdown p {
            color: #FFFFFF;
            text-align: center;
            font-family: 'TT Commons Pro', sans-serif;
        }
        .stMarkdown h2 {
            color: #FFB547;
            text-align: center;
            font-family: 'TT Commons Pro', sans-serif;
            font-size: 22px;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True
)

df['date'] = pd.to_datetime(df['date'])

# Group by year and count occurrences of each emotion
yearly_emotion_counts = df.groupby([df['date'].dt.year, 'emotions_names']).size().reset_index(name='count')

# Streamlit app
st.title('Yearly Emotion Radar Chart')
selected_year = st.slider('Select Year', min_value=min(df['date'].dt.year), max_value=max(df['date'].dt.year), value=min(df['date'].dt.year))

# Filter data for the selected year
filtered_data = df[df['date'].dt.year == selected_year]

# Adjust counts for "happiness" if the column names are different
happiness_mask = (filtered_data['emotions_names'] == 'happiness')
if 'count' in filtered_data.columns and happiness_mask.any():
    filtered_data.loc[happiness_mask, 'count'] *= 0.5

# Create a radar chart using Plotly Express
fig = px.line_polar(
    yearly_emotion_counts[yearly_emotion_counts['date'] == selected_year],
    r='count',
    theta='emotions_names',
    line_close=True,
    title=f'Emotion Radar Chart for {selected_year}',
)
st.plotly_chart(fig)