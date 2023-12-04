import streamlit as st
import pandas as pd
import random


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
            color: #D6D278;
            text-align: center;
            font-family: 'TT Commons Pro', sans-serif;
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

.st-co {
    border-bottom-color: #5DE1FE;
}       
.st-cn {
    border-top-color: #5DE1FE;
}
.st-cm {
    border-right-color: #5DE1FE;
}
.st-cl {
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
    
  opacity: 1; /* Firefox */
}
</style>
""", unsafe_allow_html=True)

emotion=st.text_input("Emotion", placeholder="Input your emotion here")

texts = pd.read_csv("../data/transformed_df/texts_emotions_final.csv")

''' Function to if emotion random text of that emotion,
if emotion list songs emotion'''




