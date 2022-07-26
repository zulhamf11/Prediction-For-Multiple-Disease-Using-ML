
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(
    open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(
    open('heart_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:

    selected = option_menu('Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            ],
                           icons=['activity', 'heart'],
                           default_index=0)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction System')

    # getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        BloodPressure = st.text_input('Blood Pressure value')
        SkinThickness = st.text_input('Skin Thickness value')
        Insulin = st.text_input('Insulin Level')

    with col2:
        BMI = st.text_input('BMI value')
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')
        Age = st.text_input('Age of the Person')
        Glucose = st.text_input('Glucose Level')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Analyze'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction System')

    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex')
        cp = st.text_input('Chest Pain types')
        trestbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        exang = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('ST depression induced by exercise')
        slope = st.text_input('Slope of the peak exercise ST segment')
        ca = st.text_input('Major vessels colored by flourosopy')
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Analyze'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
