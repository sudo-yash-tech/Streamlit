import streamlit as st
import pandas as pd 

##Adding Input Feild in Streamlit
name = st.text_input('Enter Your Good Name')
if name:
    st.write('Hello', name)

##Adding Slider in Streamlit
age = st.slider('How old are you?', 0, 130, 25)
st.write(f"I'm {name}", age, 'years old')

##Adding Selectbox in Streamlit
options = ["Python", "Java", "C++", "Ruby", "Go"]
language = st.selectbox('Which programming language do you like?', options)
st.write(f'{name} selected:', language)

##Adding Dataframe in Streamlit and save it in a csv file
data = {'name': ['John', 'Anna', 'Peter', 'Linda'],
        'age': [25, 26, 25, 23],
        'city': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
df.to_csv('data.csv')
st.write(df)

##Adding File Uploader in Streamlit
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("File Uploaded Successfully",data)
