import streamlit as st
import requests

fastapi_url = "http://fastapi:8000" 


st.set_page_config(page_title="Iris Prediction", layout="centered")

st.title("🌸 Iris Flower Prediction")
st.write("Enter flower measurements to predict the Iris species")

sepal_length=st.number_input("sepal length")
sepal_width=st.number_input("sepal width")
petal_length=st.number_input("Petal_length")
petal_width=st.number_input("petal width")

if st.button("Click for Prediction"):
    payload={
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    try:
        response=requests.post(fastapi_url+'/predict',
                      json=payload)
        if response.status_code==200:
            prediction=response.json()['Prediction']
            st.success(f"🌼 Prediction: {prediction}")
        else:
            st.error("❌ Prediction failed")
    except Exception as e:
        st.error(f"Error: {e}")