# CO₂ Emission Forecasting using Machine Learning

## 🌍 Overview
This project was completed as part of the **Skills4Future Virtual Internship Program** organized by **AICTE**, **Shell India Markets Pvt. Ltd.**, and **Edunet Foundation**. The goal was to apply AI and Data Analytics to environmental sustainability problems.

### 🎯 Objective
To build a machine learning model that predicts **CO₂ emissions per capita** based on environmental and economic indicators. This can support policy makers and organizations in identifying trends and planning climate action.

---

## 🔍 Problem Statement
Accurately forecasting CO₂ emissions helps countries evaluate the impact of energy consumption, population growth, and economic development on the environment. Using historic data, this model forecasts future per capita emissions for various countries.

---

## 🧠 Technologies Used
- Python 3
- Pandas, NumPy
- Scikit-learn
- Random Forest Regressor
- RFECV for feature selection
- RandomizedSearchCV for hyperparameter tuning
- Streamlit (for interactive demo app)

---

## 📊 Features Used
The model uses the following features:
- `urb_pop_growth_perc`
- `gni_per_cap`
- `cereal_yield`
- `pop_growth_perc`
- `en_per_cap`
- `pop_urb_aggl_perc`
- `prot_area_perc`

---

## 🏗️ Project Structure
```
.
├── app.py                 # Streamlit app for live prediction
├── rf_model.pkl          # Trained Random Forest model (exported)
├── data_cleaned.csv      # Cleaned dataset with features and target
├── Week3_assignement.ipynb  # Original training notebook
└── README.md             # Project overview and documentation
```

---

## 🚀 How to Run the Project
### 🔧 Requirements
```bash
pip install -r requirements.txt
```

### 🧪 Launch the Streamlit App
```bash
streamlit run app.py
```

---

## 📈 Results
- R² Score: >0.85 on test data
- Selected features using RFECV improved generalization
- Hyperparameter tuning increased accuracy

---

## 📽️ Demo
A video demo of the project is available [here](https://drive.google.com/file/d/1PmHeiabwh8auCHdXCZs5M9seOULa7ZZT/view?usp=drive_link) *(Link to project video)*.

---

## 📜 Certificate
A certificate of completion was awarded by the organizing bodies and is included in the repository.

---

## 🤝 Acknowledgements
Thanks to **AICTE**, **Shell India**, and **Edunet Foundation** for this opportunity to work on a real-world environmental AI challenge.

---

## 📬 Contact
For questions or collaboration, feel free to connect:
- LinkedIn: [here](https://www.linkedin.com/in/vishnu-sharma72/)
- Email: kirshansharma3546@gmail.com

---

## 🏷️ Tags
`#ArtificialIntelligence` `#MachineLearning` `#CO2Forecasting` `#GreenSkills` `#Skills4Future` `#Streamlit` `#EnvironmentalAI`



####### Model Uploaded on the Google drive :- https://drive.google.com/file/d/1LCQ6Sj2yNq0kR9okyVP3QDsSjXC4KZsP/view?usp=drive_link
