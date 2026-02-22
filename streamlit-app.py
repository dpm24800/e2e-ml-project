import numpy as np
import pandas as pd
import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="EduPredict AI",
    page_icon="🎓", # Graduation hat restored
    layout="centered"
)

# ===== SESSION STATE FOR RESET =====
if 'reset_key' not in st.session_state:
    st.session_state.reset_key = 0
if 'form_data' not in st.session_state:
    st.session_state.form_data = None

# ===== INJECT CUSTOM CSS =====
st.markdown(f"""
    <style>
    /* Compact Top Margin */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }}

    /* Original Sexy Dark Gradient */
    .main {{
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }}
    
    /* Restored Purple/Indigo Title Gradient */
    h1 {{
        background: -webkit-linear-gradient(#6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-align: center;
        font-size: 3rem !important;
        margin-top: 0px !important;
        padding-top: 0px !important;
    }}
    
    label p {{
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }}

    div[data-testid="stForm"] {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
    }}

    /* PREDICT BUTTON - NOW ELECTRIC BLUE */
    button[kind="primary"] {{
        # background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        border: none !important;
        color: white !important;
        padding: 12px 0px !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        transition: 0.3s !important;
    }}
    
    button[kind="primary"]:hover {{
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.5) !important;
        transform: translateY(-1px);
    }}

    /* CLEAR BUTTON - SLATE WITH BLUE HOVER */
    button[kind="secondary"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        color: #94a3b8 !important;
        border: 1px solid #475569 !important;
        padding: 12px 0px !important;
        border-radius: 12px !important;
        transition: 0.3s !important;
    }}
    
    button[kind="secondary"]:hover {{
        border-color: #3b82f6 !important;
        color: #3b82f6 !important;
        background: rgba(59, 130, 246, 0.05) !important;
    }}

    .result-pass {{
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid #22c55e;
        color: #22c55e;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
    }}

    .result-fail {{
        background: rgba(239, 68, 68, 0.15);
        border: 1px solid #ef4444;
        color: #ef4444;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
    }}
    </style>
    """, unsafe_allow_html=True)

# ===== HEADER =====
st.write("<h1>EduPredict AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; margin-top: -10px;'>Student Performance Indicator</p>", unsafe_allow_html=True)

# ===== INPUT FORM =====
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["", "male", "female"], key=f"gender_{st.session_state.reset_key}")
        ethnicity = st.selectbox("Ethnicity", ["", "group A", "group B", "group C", "group D", "group E"], key=f"eth_{st.session_state.reset_key}")
        parental_edu = st.selectbox("Parental Education", [
            "", "some high school", "high school", "some college", 
            "associate's degree", "bachelor's degree", "master's degree"
        ], key=f"edu_{st.session_state.reset_key}")
    
    with col2:
        lunch = st.selectbox("Lunch Type", ["", "standard", "free/reduced"], key=f"lunch_{st.session_state.reset_key}")
        test_prep = st.selectbox("Test Prep Course", ["", "none", "completed"], key=f"prep_{st.session_state.reset_key}")
        reading_score = st.number_input("Reading Score", 0, 100, step=1, key=f"read_{st.session_state.reset_key}")
        writing_score = st.number_input("Writing Score", 0, 100, step=1, key=f"write_{st.session_state.reset_key}")

    st.markdown("<br>", unsafe_allow_html=True)
    
    btn_left, btn_right = st.columns(2)
    with btn_left:
        submitted = st.form_submit_button("Predict Math Score", type="primary")
    with btn_right:
        clear_clicked = st.form_submit_button("Clear Form", type="secondary")

# ===== LOGIC =====
if clear_clicked:
    st.session_state.reset_key += 1
    st.session_state.form_data = None
    st.rerun()

if submitted:
    if not all([gender, ethnicity, parental_edu, lunch, test_prep]):
        st.error("⚠️ Please fill in all fields.")
    else:
        try:
            st.session_state.form_data = {
                'Gender': gender, 'Ethnicity': ethnicity, 'Education': parental_edu,
                'Lunch': lunch, 'Prep': test_prep, 'Reading': reading_score, 'Writing': writing_score
            }

            data = CustomData(
                gender=gender, race_ethnicity=ethnicity,
                parental_level_of_education=parental_edu,
                lunch=lunch, test_preparation_course=test_prep,
                reading_score=float(reading_score), writing_score=float(writing_score)
            )
            
            results = PredictPipeline().predict(data.get_data_as_dataframe())
            score = results[0]

            st.markdown("<br>", unsafe_allow_html=True)
            if score >= 50:
                if score >= 90: st.balloons()
                st.markdown(f'<div class="result-pass">🎉 Predicted Math Score: {score:.2f}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="result-fail">📉 Predicted Math Score: {score:.2f}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

# ===== SUMMARY =====
if st.session_state.form_data:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📋 View Submitted Input Data"):
        st.json(st.session_state.form_data)

# ===== UPDATED FOOTER =====
st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 0.8rem;'>Developed by Dipak Pulami Magar . 2026</p>", unsafe_allow_html=True)