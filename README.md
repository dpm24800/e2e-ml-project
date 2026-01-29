# Student Performance Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-1.23%2B-FF4B4B?logo=streamlit) ![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask) ![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end machine learning project that predicts students' math scores based on demographic and academic attributes. Built with a production-ready pipeline architecture and deployed via both Flask and Streamlit interfaces.

## Project Overview

This project demonstrates a complete ML workflow:

- self.Exploratory Data Analysis (EDA)
- self.Feature engineering & preprocessing
- self.Model training (CatBoost, XGBoost, Scikit-learn)
- self.Model evaluation & comparison
- self.Serialization & artifact management
- self.Web deployment (Flask + Streamlit)

Predict math scores using 7 key features:

- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type (standard/reduced)
- Test preparation course (completed/none)
- Reading score (0–100)
- Writing score (0–100)

## Project Structure

```
ml-project/
├── artifacts/                # Serialized models & preprocessors
├── catboost_info/            # CatBoost training metadata
├── notebook/                 # Jupyter notebooks for EDA & modeling
├── src/
│   ├── __init__.py
│   ├── components/           # Data ingestion, transformation modules
│   │   ├── data_ingestion.py
│   │   └── data_transformation.py
│   ├── pipeline/             # Training & prediction pipelines
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py          # Custom exception handling
│   └── logger.py             # Logging configuration
├── templates/                # Flask HTML templates
├── flask_app.py              # Flask web application (port 8000)
├── streamlit_app.py          # Streamlit interactive UI
├── requirements.txt          # Project dependencies
├── setup.py                  # Package configuration
└── README.md
```

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/dpm24800/ml-project.git
cd ml-project
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# OR
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Streamlit Interface (Recommended)

```bash
streamlit run streamlit_app.py
```

→ Open http://localhost:8501 in your browser

### Option 2: Flask Application

```bash
python flask_app.py
```

→ Open http://localhost:8000 in your browser

## Model Training

To retrain the model:

1. Explore data and experiment in `notebook/` directory
2. Run training pipeline:

```python
from src.pipeline.train_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.initiate_training()
```

Trained models and preprocessing artifacts will be saved to the `artifacts/` directory.

## Sample Prediction Interface
### Streamlit Preview
![Streamlit UI Preview](trash/streamlit_preview.png)

### Flask Preview
![Flask UI Preview](trash/flask_preview.png)

## Dependencies

Key libraries used:

- `pandas`, `numpy` – Data manipulation
- `scikit-learn` – Preprocessing & baseline models
- `catboost`, `xgboost` – Gradient boosting models
- `dill` – Model serialization
- `flask`, `streamlit` – Web interfaces
- `matplotlib`, `seaborn`, `altair` – Visualization

See [`requirements.txt`](requirements.txt) for full dependency list.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Dipak Pulami Magar – [@dpm24800](https://github.com/dpm24800)  
Project Link: https://github.com/dpm24800/ml-project


