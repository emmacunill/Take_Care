import streamlit as st
import pandas as pd
import random

text_df = pd.read_csv('../data/transformed_df/cleaned_texts.csv')  
songs_df = pd.read_csv('../data/transformed_df/songs.csv')


st.set_page_config(
    page_title="Emotion Recommendations",
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

def main():
    '''252525 BC669F TT Commons Pro'''
    st.title("Emotion Recommender")
    st.subheader("This gives specific recommendations for what you're feeling :)")

if __name__ == "__main__":
    main()


st.markdown("""
<style>
.stTextInput > label {
color:white;
display: none
}


[data-baseweb="input"]{
            width: 300px;
    margin:auto;
}            

.st-ct {
    border-bottom-color: #5DE1FE;
}       
.st-cr {
    border-top-color: #5DE1FE;
}
.st-cr {
    border-right-color: #5DE1FE;
}
.st-cq {
    border-left-color: #5DE1FE;
}            
            
[data-baseweb="base-input"]{
background:#000000;
border: 2px;
border-radius: 3px;
}


input[class]{
font-weight: 400;
font-size:18px;
color: white;
}

input[class]::placeholder {
  color: #979797;
    font-weight: 400;
    font-size: 14px;
    font-family: 'TT Commons Pro', sans-serif;
    
  opacity: 1; /* Firefox */}
            
[data-testid="stDataFrame"]{
    width: 400px;
}

[data-testid="stStyledFullScreenFrame"]{
    background-color: #252525;
    border: white;
    padding: 5px;
    margin:auto;
    display: felx;
    align-content:center;
            
}

</style>
""", unsafe_allow_html=True)


emotion=st.text_input("Emotion", placeholder="Input your emotion here")


def get_songs_for_emotion(emotion):
    filtered_songs = songs_df[songs_df['Emotion'] == emotion]
    return filtered_songs[['Songs', 'Musical']]


def get_random_text_with_title(emotion):
    filtered_texts = text_df[text_df['emotions_names'] == emotion]
    print(filtered_texts)
    if not filtered_texts.empty:
        random_row = random.choice(filtered_texts.index)
        random_text = filtered_texts.loc[random_row, 'text']
        random_title = filtered_texts.loc[random_row, 'title']
        return random_title, random_text
    else: 
        st.warning(f"No text found for {emotion}")

st.header(f"Songs for {emotion}")
songs_table = get_songs_for_emotion(emotion)
if not songs_table.empty:
    st.dataframe(songs_table)
else:
    st.warning(f"No songs found for {emotion}")

random_title, random_text = get_random_text_with_title(emotion)
if random_title and random_text:
    st.header(f"Random Text for {emotion}")
    st.subheader(f"{random_title}")
    st.write(f"{random_text}")
else:
    st.warning(f"No text found for {emotion}")

# Display songs associated with the selected emotion





