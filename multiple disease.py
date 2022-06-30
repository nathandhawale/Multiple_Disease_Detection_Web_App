#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:21:30 2022

@author: nathandhawale
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading the Saved Models

diabetes_model = pickle.load(open('/Users/nathandhawale/Desktop/Multiple Disease Prediction System/Saved Models/Diabetes-Prediction/trained_diabetes_model.sav',
                                  'rb'))
heart_disease_model = pickle.load(open('/Users/nathandhawale/Desktop/Multiple Disease Prediction System/Saved Models/Heart-Disease-Prediction/trained_heart_disease_model.sav',
                                       'rb'))
parkinson_model = pickle.load(open('/Users/nathandhawale/Desktop/Multiple Disease Prediction System/Saved Models/Parkinson-Detection/trained_parkinsons_model.sav',
                                   'rb'))


#sidebar
with st.sidebar:
    select = option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons = ['activity',
                                  'heart',
                                  'bandaid'],
                         default_index=0)
    
    
#Diabetes Prediction Page
if (select == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction Using ML')
    
    #getting input data from user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
        
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input("Age")
        
    
    #getting input data from user
    
    
    #code for Prediction
    diabetes_diagnosis = ''
    
    #creating button for prediction
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,
                                                       Glucose,
                                                       BloodPressure,
                                                       SkinThickness,
                                                       Insulin,
                                                       BMI,
                                                       DiabetesPedigreeFunction,
                                                       Age]])
        
        if (diabetes_prediction[0]==1):
            diabetes_diagnosis = 'The person is Diabetic'
        else:
            diabetes_diagnosis = 'The person is not Diabetic'
    
    st.success(diabetes_diagnosis)
    

#Heart Disease Prediction Page
if (select == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction Using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("CP")
        
    with col1:
        trestbps = st.text_input("TrestBPS")
    with col2:
        chol = st.text_input("Cholesterol")
    with col3:
        fbs = st.text_input("FBS")
        
    with col1:
        restecg = st.text_input("Resting ECG")
    with col2:
        thalach = st.text_input("Thalach")
    with col3:
        exang = st.text_input("Exang")
        
    with col1:
        oldpeak = st.text_input("Old Peak")
    with col2:
        slope = st.text_input("Slope")
    with col3:
        ca = st.text_input("CA")

    with col1:
        thal = st.text_input("Thal")
        
        
        
    heart_disease_diagnosis = ''
        
        #creating button for prediction
    if st.button("Heart Disease Result"):
        heart_disease_prediction = heart_disease_model.predict([[age,
                                                                 sex,
                                                                 cp,
                                                                 trestbps,
                                                                 chol,
                                                                 fbs,
                                                                 restecg,
                                                                 thalach,
                                                                 exang,
                                                                 oldpeak,
                                                                 slope,
                                                                 ca,
                                                                 thal]])
        
        if (heart_disease_prediction[0]==1):
            heart_disease_diagnosis = 'The person has Heart Disease'
        else:
            heart_disease_diagnosis = 'The person does not have Heart Disease'
    
    st.success(heart_disease_diagnosis)
        
        
        
#Parkinsons Prediction Page
if (select == 'Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz) ")
    
    with col1:
        jitter = st.text_input("MDVP:Jitter(%)")
    with col2:
        jitterabs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        rap = st.text_input("MDVP:RAP")
    
    with col1:
        ppq = st.text_input("MDVP:PPQ")
    with col2:
        ddp = st.text_input("Jitter:DDP")
    with col3:
        shimmer = st.text_input("MDVP:Shimmer")
        
    with col1:
        shimmerdb = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        apq3 = st.text_input("Shimmer:APQ3")
    with col3:
        apq5 = st.text_input("Shimmer:APQ5")
        
    with col1:
        apq = st.text_input("MDVP:APQ")
    with col2:
        dda = st.text_input("Shimmer:DDA")
    with col3:
        nhr = st.text_input("NHR")
    
    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rpde = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")
    
    with col1:
        spread1 = st.text_input("Spread1")
    with col2:
        spread2 = st.text_input("Spread2")
    with col3:
        d2 = st.text_input("D2")
    
    with col1:
        ppe = st.text_input("PPE")
    
    
    parkinsons_disease_diagnosis = ''
        
        #creating button for prediction
    if st.button("Parkinsons Disease Result"):
        parkinsons_disease_prediction = parkinson_model.predict([[fo, fhi, flo,
                                                                  jitter, jitterabs, rap,
                                                                  ppq, ddp, shimmer,
                                                                  shimmerdb, apq3, apq5,
                                                                  apq, dda, nhr,
                                                                  hnr, rpde, dfa,
                                                                  spread1, spread2, d2,
                                                                  ppe]])
        
        if (parkinsons_disease_prediction[0]==1):
            parkinsons_disease_diagnosis = 'The person has Heart Disease'
        else:
            parkinsons_disease_diagnosis = 'The person does not have Heart Disease'
    
    st.success(parkinsons_disease_diagnosis)    
    
    
    
    
    
    
    
    
    
