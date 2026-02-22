import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

from flask import Flask, request, render_template

appplication = Flask(__name__)

app = appplication

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # Initialize empty form_data for GET requests
        form_data = {
            'gender': '',
            'ethnicity': '',
            'parental_level_of_education': '',
            'lunch': '',
            'test_preparation_course': '',
            'writing_score': '',
            'reading_score': ''
        }
        return render_template('home.html', results=None, form_data=form_data)
    else:
        # Capture RAW form data BEFORE processing (for repopulation)
        form_data = {
            'gender': request.form.get('gender', ''),
            'ethnicity': request.form.get('ethnicity', ''),
            'parental_level_of_education': request.form.get('parental_level_of_education', ''),
            'lunch': request.form.get('lunch', ''),
            'test_preparation_course': request.form.get('test_preparation_course', ''),
            'writing_score': request.form.get('writing_score', ''),
            'reading_score': request.form.get('reading_score', '')
        }
        
        # Create CustomData object with CORRECT parameter mapping
        try:
            data = CustomData(
                gender=form_data['gender'],
                race_ethnicity=form_data['ethnicity'],
                parental_level_of_education=form_data['parental_level_of_education'],
                lunch=form_data['lunch'],
                test_preparation_course=form_data['test_preparation_course'],
                reading_score=float(form_data['reading_score']),   # ✅ CORRECT - reading_score from reading_score field
                writing_score=float(form_data['writing_score'])    # ✅ CORRECT - writing_score from writing_score field
            )
            
            pred_df = data.get_data_as_dataframe()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")
            
            # Pass BOTH results AND form data to template
            return render_template(
                'home.html', 
                results=results[0] if results else None,
                form_data=form_data
            )
        except ValueError as e:
            # Handle case where scores are not valid numbers
            error_message = "Please enter valid numeric scores for Reading and Writing."
            return render_template(
                'home.html', 
                results=None,
                form_data=form_data,
                error=error_message
            )
        except Exception as e:
            # Handle any other errors
            error_message = f"An error occurred: {str(e)}"
            return render_template(
                'home.html', 
                results=None,
                form_data=form_data,
                error=error_message
            )

# if __name__ == "__main__":
#     # app.run(host="0.0.0.0")    
#     app.run(debug=True, port=8000)  # port: optional, for other  
#     # app.run(debug=False, use_reloader=False, port=8000)

# if __name__ == "__main__":
#     url = "http://127.0.0.1:8000/"
#     print(f"\nYour Flask app is running! Click or Ctrl+Click to open:\n{url}\n")
    
#     app.run(debug=True, use_reloader=False, port=8000)

import os

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        url = "http://127.0.0.1:8000/"
        print(f"\n✅ Your Flask app is running! \n Ctrl + Click to open: {url}\n")
    
    app.run(debug=True, port=8000)