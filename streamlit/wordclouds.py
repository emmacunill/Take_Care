import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv('../data/transformed_df/emsemotions.csv')

st.set_page_config(
    page_title="Word clouds"
)

st.markdown(
    """
    <style>
        body {
            background-color: #252525;
        }
        .stApp {
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
st.markdown("""
<style>
.stTextInput > label {
color:white;
display: none
}
            
input[class]{
font-weight: 400;
font-size:18px;
color: #000000;
}

input[class]::placeholder {
  color: #000000;
    font-weight: 400;
    font-size: 14px;
    font-family: 'TT Commons Pro', sans-serif;

 </style>
    """,
    unsafe_allow_html=True
)

st.title('Find the most frequent words')

# Function to generate a word cloud for a given emotion
def generate_wordcloud(emotion_df, selected_emotion):
    # Filter the DataFrame for the selected emotion
    emotion_messages = emotion_df[emotion_df['emotions_names'] == selected_emotion]['message'].tolist()
    text = ' '.join(emotion_messages)

    # Tokenize the words
    words = word_tokenize(text)

    stop_words_spanish = set(stopwords.words('spanish'))
    stop_words_catalan = set(stopwords.words('catalan'))

    # Add custom stop words to the existing lists
    custom_stop_words = ['siiii', 'sisiii','siii', 'nose','ok','okay','m','oki','okaaay','guai','okaay','perfecte', 'custom_word2',
                         'deleted','message deleted', 's', 'l', 'h', 't', 'd', 'message','ara', 'serio',
                         'mes', 'mas', 'tears', 'asi', 'voy', 'ahora', 'cosa', 'skin tone', 'dicho',
                         'perque', 'mañana', 're', 'dicho', 'face', 'bien', 'tambe', 'tambien', 'sino', 'dema',
                         'veritat', 'solo', 'joy']  # Add your custom words here
    stop_words_spanish.update(custom_stop_words)
    stop_words_catalan.update(custom_stop_words)
    stop_words = stop_words_spanish.union(stop_words_catalan)

    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Combine the processed words back into a string
    processed_text = ' '.join(words)

    # Generate WordCloud
    wordcloud = WordCloud(width=800, height=400, max_words=20, background_color='white').generate(processed_text)

    # Display the WordCloud using Streamlit
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    # Display the Matplotlib figure using st.pyplot
    st.pyplot(fig)

# Example usage
# Assuming you have a DataFrame called 'df' with 'message' and 'emotions_names' columns
# Get user input for the emotion
selected_emotion = st.text_input("Enter an emotion:")
# For example, for the emotion 'happiness'
if selected_emotion:
    emotion_df = df[df['emotions_names'] == selected_emotion]
    generate_wordcloud(emotion_df, selected_emotion)


