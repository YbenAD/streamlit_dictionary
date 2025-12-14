import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title = "Streamlit Dictionary",
    page_icon= "🌍",
    layout= "centered",
)

st.title("English Dictionary")

url = "https://api.dictionaryapi.dev/api/v2/entries/en"
st.sidebar.header("Definition of Word")
word = st.sidebar.text_input("", placeholder="Enter a word")
if st.sidebar.button("Search Definition"):
    response = requests.get(url + "/" + word)
    data = response.json()
    for entry in data:
        st.markdown(f"<h2 style='text-align: center;'>definition of : <i>{word}</i></h2>", unsafe_allow_html=True)
        st.divider()
        meaning = entry["meanings"]
        for element in meaning:
            st.markdown(f"<p style='text-align: center;'>part of speach : {element['partOfSpeech']}</p>", unsafe_allow_html=True)
            st.divider()
            definition = element["definitions"]
            for item in definition:
                st.markdown(f"<p> definition:  {item['definition']}</p>", unsafe_allow_html=True)



