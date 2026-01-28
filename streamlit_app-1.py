import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Student Performance Predictor", layout="centered")

# ===== SESSION STATE FOR FORM PERSISTENCE =====
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'gender': '',
        'ethnicity': '',
        'parental_level_of_education': '',
        'lunch': '',
        'test_preparation_course': '',
        'writing_score': '',
        'reading_score': ''
    }
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None
if 'error_message' not in st.session_state:
    st.session_state.error_message = None

# ===== HEADER =====
st.title("🎓 Student Performance Predictor")
st.markdown("Predict math scores based on student attributes")

# ===== INPUT FORM =====
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["", "male", "female"], 
                             index=["", "male", "female"].index(st.session_state.form_data['gender']) if st.session_state.form_data['gender'] else 0)
        ethnicity = st.selectbox("Ethnicity", 
                                ["", "group A", "group B", "group C", "group D", "group E"],
                                index=["", "group A", "group B", "group C", "group D", "group E"].index(st.session_state.form_data['ethnicity']) if st.session_state.form_data['ethnicity'] else 0)
        parental_edu = st.selectbox("Parental Education Level",
                                   ["", "some high school", "high school", "some college", 
                                    "associate's degree", "bachelor's degree", "master's degree"],
                                   index=["", "some high school", "high school", "some college", 
                                          "associate's degree", "bachelor's degree", "master's degree"].index(st.session_state.form_data['parental_level_of_education']) 
                                          if st.session_state.form_data['parental_level_of_education'] else 0)
    
    with col2:
        lunch = st.selectbox("Lunch Type", ["", "standard", "free/reduced"],
                            index=["", "standard", "free/reduced"].index(st.session_state.form_data['lunch']) if st.session_state.form_data['lunch'] else 0)
        test_prep = st.selectbox("Test Prep Course", ["", "none", "completed"],
                                index=["", "none", "completed"].index(st.session_state.form_data['test_preparation_course']) if st.session_state.form_data['test_preparation_course'] else 0)
        reading_score = st.text_input("Reading Score", value=st.session_state.form_data['reading_score'])
        writing_score = st.text_input("Writing Score", value=st.session_state.form_data['writing_score'])
    
    submitted = st.form_submit_button("🔮 Predict Math Score")

# ===== PREDICTION LOGIC =====
if submitted:
    # Save form data to session state for repopulation
    st.session_state.form_data = {
        'gender': gender,
        'ethnicity': ethnicity,
        'parental_level_of_education': parental_edu,
        'lunch': lunch,
        'test_preparation_course': test_prep,
        'writing_score': writing_score,
        'reading_score': reading_score
    }
    
    # Validation
    if not all([gender, ethnicity, parental_edu, lunch, test_prep, reading_score, writing_score]):
        st.session_state.error_message = "⚠️ Please fill in all fields"
        st.session_state.prediction_result = None
    else:
        try:
            # Convert scores to float
            reading = float(reading_score)
            writing = float(writing_score)
            
            # Create prediction data
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_edu,
                lunch=lunch,
                test_preparation_course=test_prep,
                reading_score=reading,
                writing_score=writing
            )
            
            pred_df = data.get_data_as_data_frame()
            st.write("Input data:", pred_df)  # Optional debug
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            st.session_state.prediction_result = results[0]
            st.session_state.error_message = None
            
        except ValueError:
            st.session_state.error_message = "⚠️ Reading/Writing scores must be valid numbers"
            st.session_state.prediction_result = None
        except Exception as e:
            st.session_state.error_message = f"⚠️ Prediction error: {str(e)}"
            st.session_state.prediction_result = None

# ===== DISPLAY RESULTS =====
if st.session_state.error_message:
    st.error(st.session_state.error_message)

if st.session_state.prediction_result is not None:
    st.success(f"✅ Predicted Math Score: **{st.session_state.prediction_result:.2f}**")
    
    # Optional: Show input summary
    with st.expander("📋 Input Summary"):
        st.json(st.session_state.form_data)

# ===== FOOTER =====
st.markdown("---")
st.caption("Powered by Streamlit • Prediction model trained on student performance dataset")