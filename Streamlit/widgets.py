import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")
age=st.slider("Select Your age:",0,100,25)
st.write(f"Your age is {age}")

options=['Python','Cpp','Java','JS']
choice=st.selectbox("Choose your preferred Language:",options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["Amit", "Sneha", "Raj", "Priya"],
    "Age": [25, 22, 28, 24],
    "City": ["Delhi", "Mumbai", "Bangalore", "Kolkata"]
}

df=pd.DataFrame(data)
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)