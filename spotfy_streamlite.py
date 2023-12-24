import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
pickle_in=open("C:\\Users\\91885\\PycharmProjects\\spotify.pkl","rb")
model=pickle.load(pickle_in)
def hello():
    return "hello all"

def main():
    img = Image.open('C:/Users/91885/Desktop/spotify.jpg')
    st.image(img)
    html_temp="""
    <div style="background-color:green;padding:10px">   
    <h2 style="color:white;text-align:center;">Song recommendation</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    danceability = st.text_input("Danceability","Type Here")
    energy = st.text_input("Energy","Type Here")
    key = st.text_input("Key","Type Here")
    loudness = st.text_input("Loudness","Type Here")
    mode = st.text_input("Mode", "Type Here")
    speechiness = st.text_input("Speechiness", "Type Here")
    acousticness = st.text_input("Acousticness", "Type Here")
    instrumentalness = st.text_input("Instrumentalness", "Type Here")
    liveness = st.text_input("Liveness", "Type Here")
    valence = st.text_input("Valence", "Type Here")
    tempo = st.text_input("Tempo", "Type Here")
    duration_ms = st.text_input("Duration_ms", "Type Here")
    time_signature = st.text_input("Time_signature", "Type Here")
    result=""
    if st.button("Predict"):
        testdata = np.array([[danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness,
                              liveness, valence, tempo, duration_ms, time_signature]])
        result = model.predict(testdata)
    if result==0:
        st.success("song not recommended")
    elif result==1:
        st.success("song recommended")
    else:
        st.success("NA")
    if st.button("About"):
        st.text("lets learn")
if __name__=='__main__':
    main()
