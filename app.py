import streamlit as st
import numpy as np
import pandas as pd
import pickle

rfr__=pickle.load(open('rfr.pkl','rb'))
x_train =pd.read_csv('x_train.csv')

def pred(g,a,h,w,d,hr,bt):
    features=np.array([[g,a,h,w,d,hr,bt]])
    prediction=rfr__.predict(features).reshape(1,-1)
    return prediction

st.title("calories burnt app")

gender=st.selectbox('Gender',x_train['Gender'])
age=st.selectbox('Age',x_train['Age'])
height=st.selectbox('Height',x_train['Height'])
weight=st.selectbox('weight',x_train['Weight'])
duration=st.selectbox('Duration',x_train['Duration'])
heart_rate=st.selectbox('Heart_rate',x_train['Heart_Rate'])
body_temp=st.selectbox('Body Temperature',x_train['Body_Temp'])

res=pred(gender,age,height,weight,duration,heart_rate,body_temp)

if st.button('predict'):
    if res:
        st.write("You have consumed this calories:",res)