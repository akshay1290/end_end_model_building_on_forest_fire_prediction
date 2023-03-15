import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
model_file = 'model_C=1.0.bin'

from PIL import Image

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,
       wind,rain):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=regressor.predict([[X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain]])
    print(prediction)
    return prediction



def main():
    image = Image.open('images/icone.png')
    image2 = Image.open('images/image.png')
    st.image(image,use_column_width=False)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict FOREST FIRE')
    st.sidebar.image(image2)
    st.title("FOREST FIRE PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">FOREST FIRE PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    X = st.text_input("X","Type Here")
    Y = st.text_input("Y","Type Here")
    month = st.text_input("month","Type Here")
    day = st.text_input("day","Type Here")
    FFMC = st.text_input("FFMC","Type Here")
    DMC = st.text_input("DMC","Type Here")
    DC = st.text_input("DC","Type Here")
    ISI = st.text_input("ISI","Type Here")
    temp = st.text_input("temp","Type Here")
    RH = st.text_input("RH","Type Here")
    wind = st.text_input("wind","Type Here")
    rain = st.text_input("rain","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    