import streamlit as st
import pandas as pd
import pickle

def load_model():
    model = pickle.load(open("diabetes.pkl",'rb'))
    return model

model = load_model()

st.title("Diabetes Prediction App")
st.subheader("This app predicts whether a person has diabetes or not")

pregnancies = st.sidebar.number_input("Pregnancies",min_value=0,max_value=20)
glucose = st.sidebar.number_input("Glucose",min_value=0,max_value=200)
blood_pressure = st.sidebar.number_input("Blood Pressure",min_value=0,max_value=200)
skinthickness = st.sidebar.number_input("Skin Thickness",min_value=0,max_value=100)
insulin = st.sidebar.number_input("Insulin",min_value=0,max_value=1000)
bmi = st.sidebar.number_input("BMI",min_value=0.0,max_value=100.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function",min_value=0.0,max_value=10.0)
age = st.sidebar.number_input("Age",min_value=0,max_value=100)

if st.button("Predict"):
    input = [[pregnancies,glucose,blood_pressure,skinthickness,insulin,bmi,dpf,age]]
    output = model.predict(input)

    if output == 0:
        st.subheader("You don't have diabetes")
    else:
        st.subheader("You have diabetes")