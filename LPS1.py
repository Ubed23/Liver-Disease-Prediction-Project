# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:53:42 2024

@author: ubedu
"""

import pickle
import streamlit as st
import pandas as pd
import seaborn as sns

df=pd.read_csv("project-data.csv",delimiter=";")

load=open('model1.pkl','rb')
model=pickle.load(load)

def predict(age,sex,albumin,alkaline_phosphatase,alanine_aminotransferase,aspartase_aminotransferase,bilirubin,cholinesterase,cholesterol,creatinina,gamma_glutamyl_transferase,protein):
    
    user_input=[age,sex,albumin,alkaline_phosphatase,alanine_aminotransferase,aspartase_aminotransferase,bilirubin,cholinesterase,cholesterol,creatinina,gamma_glutamyl_transferase,protein]
    user_input=[float(x) for x in user_input]
    prediction=model.predict([user_input])
    #prediction=model.predict([[age,sex,albumin,alkaline_phosphatase,alanine_aminotransferase,aspartase_aminotransferase,bilirubin,cholinesterase,cholesterol,creatinina,gamma_glutamyl_transferase,protein]])
    return prediction

def main():
    
    
    st.title("**Liver Disease Prediction Model**")
    st.text("A liver disease prediction system uses machine learning algorithms to predict the likelihood of liver disease based on patient data.\n It typically takes inputs like age, gender, liver enzyme levels, and medical history.\n The system processes this data through a trained model to classify whether a patient is at risk of liver conditions like cirrhosis, hepatitis, or fatty liver disease.\n Data preprocessing techniques like normalization and handling missing values are essential for accurate predictions.\n Such systems assist healthcare providers in early diagnosis and treatment decisions.")
    
    html_temp = """
    <div style="background-color:teal;padding:15px">
    <h2 style="color:white;text-align:center;">Streamlit Liver Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.write("\n Enter the Details")
    
    age=st.slider("select age", 0, 100)
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        sex=st.text_input("sex: ")

    with col2:
        albumin=st.text_input("Albumin: ")
    
    with col3:
        alkaline_phosphatase=st.text_input("Alkaline_phosphatase: ")
    
    with col1:
        alanine_aminotransferase=st.text_input("Alanine_aminotransferase: ")
        
    with col2:
        aspartase_aminotransferase=st.text_input("Aspartase_aminotransferase: ")
    
    with col3:
        bilirubin=st.text_input("Bilirubin: ")
    
    with col1:
        cholinesterase=st.text_input("Cholinesterase: ")
    
    with col2:
        cholesterol=st.text_input("Cholesterol: ")

    with col3:
        creatinina=st.text_input("Creatinina: ")
    
    with col1:
        gamma_glutamyl_transferase=st.text_input("Gamma_glutamyl_transferase: ")
    
    with col2:
        protein=st.text_input("Protein: ")
    
    if st.button("Predict"):
        result=predict(age,sex,albumin,alkaline_phosphatase,alanine_aminotransferase,aspartase_aminotransferase,bilirubin,cholinesterase,cholesterol,creatinina,gamma_glutamyl_transferase,protein)
        if result==0:
            st.success("The person has Cirrhosis")
            
        elif result==1:
            st.success("The person has Hepatitis")
            
        elif result==2:
            st.success("The person has Fibrosis")
            
        else:
            st.success("The person has no disease")
            
    st.dataframe(df)
    
    tab1, tab2 = st.tabs(["tab1","tab2"])
    with tab1:
        st.bar_chart(y='category', data=df,color= "#3FC6F0")
    with tab2:
        st.scatter_chart(y="age",data=df,color="#7FDD05")
    with tab1:
        st.bar_chart(y="sex",data=df)
    
            
if __name__=="__main__":
    main()
        