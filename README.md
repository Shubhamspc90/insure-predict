# InsurePredict — AI-Powered Insurance Premium Category Prediction System

InsurePredict is an end-to-end **Machine Learning + FastAPI + Streamlit** application that predicts an insurance premium category based on user information and provides prediction confidence along with derived customer features.

The project demonstrates how a trained Machine Learning model can be integrated into a production-style backend API and connected to an interactive frontend.

---

## 📌 Project Overview

The application accepts customer information such as:

* Age
* Weight
* Height
* Annual Income
* Smoking status
* City
* Occupation

From this information, the application automatically derives additional features:

* BMI
* Age Group
* Lifestyle Risk
* City Tier

These features are passed to the trained Machine Learning model, which predicts the customer's **insurance premium category** and returns confidence probabilities for each category.

### Application Flow

```text
User
 │
 ▼
Streamlit Frontend
 │
 │ POST /predict
 ▼
FastAPI Backend
 │
 ▼
Pydantic Validation
 │
 ▼
Feature Engineering
 │
 ├── BMI
 ├── Age Group
 ├── Lifestyle Risk
 └── City Tier
 │
 ▼
Machine Learning Model
 │
 ▼
Prediction + Confidence
 │
 ▼
Streamlit Result
```

---

# ✨ Features

## 1. Machine Learning Prediction

The application uses a trained Machine Learning model to predict one of the insurance premium categories:

```text
Low
Medium
High
```

The model also provides probability/confidence values for each category.

---

## 2. FastAPI Backend

The ML model is exposed through a REST API using FastAPI.

### Available Endpoints

| Method | Endpoint   | Description                           |
| ------ | ---------- | ------------------------------------- |
| GET    | `/`        | API information                       |
| GET    | `/health`  | Health and model status               |
| POST   | `/predict` | Generate insurance premium prediction |

FastAPI also provides automatic interactive API documentation through Swagger UI.

```text
http://localhost:8000/docs
```

---

# 🧮 Feature Engineering

The application automatically generates several features from the user's input.

## BMI

BMI is calculated using:

```text
BMI = Weight / Height²
```

For example:

```text
Weight = 65 kg
Height = 1.70 m

BMI = 65 / (1.70²)
    = 22.49
```

The calculated BMI is rounded to two decimal places.

---

## Age Group

The application categorizes users into age groups:

|     Age | Age Group   |
| ------: | ----------- |
|  `< 25` | young       |
| `25–44` | adult       |
| `45–59` | middle_aged |
| `>= 60` | senior      |

---

## Lifestyle Risk

Lifestyle risk is derived from smoking status and BMI.

```text
Smoker + BMI > 30
        ↓
      High

Smoker OR BMI > 27
        ↓
     Medium

Otherwise
        ↓
       Low
```

---

## City Tier

Cities are categorized into three tiers.

### Tier 1 Cities

Examples:

```text
Mumbai
Delhi
Bangalore
Chennai
Kolkata
Hyderabad
Pune
```

### Tier 2 Cities

The project maintains a predefined list of Tier 2 cities including:

```text
Jaipur
Chandigarh
Indore
Lucknow
Patna
Ranchi
Visakhapatnam
Coimbatore
Bhopal
Nagpur
Vadodara
Surat
Rajkot
...
```

### Tier 3

Any city that is not present in the Tier 1 or Tier 2 lists is treated as:

```text
Tier 3
```

The city input is also normalized before classification.

For example:

```text
"   mumbai   "
```

becomes:

```text
"Mumbai"
```

---

# 🔐 Input Validation

User input is validated using **Pydantic** before reaching the Machine Learning model.

Validation includes:

* Age must be greater than 0 and less than 120
* Weight must be greater than 0
* Height must be greater than 0 and less than 2.5 meters
* Income must be greater than 0
* Smoking status must be boolean
* City is normalized automatically
* Occupation is restricted to predefined values

Supported occupations:

```text
retired
freelancer
student
government_job
business_owner
unemployed
private_job
```

Invalid input results in a FastAPI validation response such as:

```text
422 Unprocessable Entity
```

---

# 📊 Prediction Response

A successful prediction returns:

```json
{
    "success": true,
    "predicted_category": "Medium",
    "confidence": {
        "Low": 10.25,
        "Medium": 75.50,
        "High": 14.25
    },
    "features": {
        "bmi": 22.49,
        "age_group": "adult",
        "lifestyle_risk": "low",
        "city_tier": 1
    }
}
```

The exact prediction and confidence values depend on the trained model.

---

# ❤️ Health Check

The API provides a health-check endpoint:

```text
GET /health
```

Example response:

```json
{
    "status": "ok",
    "version": "1.0.0",
    "model_loaded": true
}
```

This can be used to verify that:

* The API is running
* The model has been loaded
* The current model version is available

---

# 🖥️ Streamlit Frontend

The project includes an interactive Streamlit frontend.

The frontend allows users to enter:

* Age
* Weight
* Height
* Income
* Smoking status
* City
* Occupation

After clicking the prediction button, the frontend sends the information to the FastAPI backend.

The result displays:

* Predicted premium category
* BMI
* City tier
* Age group
* Lifestyle risk
* Confidence for Low, Medium and High categories

### Frontend Flow

```text
Streamlit
    │
    │ HTTP POST
    ▼
FastAPI
    │
    ▼
ML Prediction
    │
    ▼
JSON Response
    │
    ▼
Streamlit Result
```

---

# 🏗️ Project Structure

```text
insure-predict/
│
├── config/
│   ├── __init__.py
│   └── city_tier.py
│
├── model/
│   ├── model.pkl
│   └── predict.py
│
├── schema/
│   ├── response.py
│   └── user_input.py
│
├── frontend/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│
├── .gitignore
├── apps.py
├── README.md
└── requirements.txt
```

---

# 📁 Folder Responsibilities

### `config/`

Contains application configuration and city classification data.

```text
config/city_tier.py
```

stores Tier 1 and Tier 2 city lists.

---

### `model/`

Contains the trained Machine Learning model and prediction logic.

```text
model.pkl
```

stores the trained model.

```text
predict.py
```

handles model loading and prediction.

---

### `schema/`

Contains Pydantic schemas used by FastAPI.

```text
user_input.py
```

handles:

* Input validation
* BMI calculation
* Age group
* Lifestyle risk
* City tier

```text
response.py
```

defines the structure of the API response.

---

### `frontend/`

Contains the Streamlit user interface.

```text
frontend/app.py
```

handles:

* User input
* API communication
* Prediction results
* Error handling
* Result visualization

---

### `tests/`

Reserved for automated tests for the API, validation, feature engineering and prediction functionality.

---

# 🛠️ Technology Stack

| Technology   | Purpose                       |
| ------------ | ----------------------------- |
| Python       | Core programming language     |
| FastAPI      | Backend REST API              |
| Pydantic     | Data validation and schemas   |
| Pandas       | Data processing               |
| Scikit-learn | Machine Learning              |
| Pickle       | Model serialization           |
| Streamlit    | Frontend                      |
| Requests     | Frontend-to-API communication |
| Git          | Version control               |
| GitHub       | Repository and collaboration  |

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/insure-predict.git
```

Move into the project:

```bash
cd insure-predict
```

---

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# ▶️ Running the Application

The project has two components:

```text
FastAPI Backend
        +
Streamlit Frontend
```

Both should be running simultaneously.

---

## Start FastAPI

From the project root:

```powershell
uvicorn apps:app --reload
```

The API will run at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## Start Streamlit

Open another terminal.

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Run:

```powershell
streamlit run frontend/app.py
```

Streamlit will normally open at:

```text
http://localhost:8501
```

If that port is already occupied, Streamlit may automatically use another available port such as `8502`.

---

# 🧪 API Testing

The API can be tested using Swagger UI.

Open:

```text
http://localhost:8000/docs
```

Use the `/predict` endpoint with a request such as:

```json
{
    "age": 30,
    "weight": 65,
    "height": 1.7,
    "income_lpa": 10,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}
```

The application derives:

```text
BMI          → 22.49
Age Group    → adult
Lifestyle    → low
City Tier    → 1
```

The trained model then generates the final prediction.

---

# 🧪 Validation Scenarios Tested

The application has been tested for different scenarios, including:

### Valid Input

Normal customer information should generate a prediction successfully.

### High-Risk Scenario

A customer with:

```text
High BMI
+
Smoker = True
```

should receive:

```text
lifestyle_risk = high
```

### Tier 2 City

A city such as:

```text
Jaipur
```

should be classified as:

```text
city_tier = 2
```

### City Normalization

Input such as:

```text
"   mumbai   "
```

is normalized to:

```text
"Mumbai"
```

### Invalid Age

```text
age = 150
```

should result in:

```text
422 Unprocessable Entity
```

### Invalid Occupation

An unsupported occupation such as:

```text
doctor
```

should fail Pydantic validation.

### Invalid Height

A height outside the accepted range should also result in validation failure.

---

# 🔒 Error Handling

The application handles different types of errors.

### Validation Errors

Handled automatically by FastAPI/Pydantic.

### Prediction Errors

The `/predict` endpoint catches prediction-related exceptions and returns an appropriate error response.

### Frontend Connection Errors

The Streamlit application handles cases where the FastAPI backend is unavailable.

For example:

```text
FastAPI stopped
        ↓
Streamlit request fails
        ↓
Connection error displayed
```

After restarting FastAPI, the frontend can connect again.

---

# 🤖 Model Compatibility

The trained model was created using:

```text
scikit-learn 1.6.1
```

Therefore, the project pins the dependency to:

```text
scikit-learn==1.6.1
```

This is important because serialized Scikit-learn models can encounter compatibility problems when loaded with a significantly different library version.

---

# 📄 Requirements

Current dependencies:

```text
fastapi
uvicorn[standard]
pydantic
pandas
scikit-learn==1.6.1
streamlit
requests
```

---

# 🔄 Development Workflow

This project follows a professional Git/GitHub workflow.

The planned branch structure is:

```text
main
  │
  └── develop
        │
        ├── feature/*
        ├── fix/*
        └── docs/*
```

### `main`

Contains stable, production-ready code.

### `develop`

Integration branch for completed features before they are promoted to `main`.

### Feature Branches

Used for new functionality:

```text
feature/<feature-name>
```

### Fix Branches

Used for bug fixes:

```text
fix/<bug-name>
```

### Documentation Branches

Used for documentation changes:

```text
docs/<change-name>
```

Changes are intended to follow:

```text
Create Branch
      ↓
Develop
      ↓
Test
      ↓
Commit
      ↓
Push
      ↓
Pull Request
      ↓
Code Review
      ↓
Fix Review Comments
      ↓
Merge
      ↓
Delete Branch
      ↓
Sync Local Repository
```

The project will maintain meaningful commits and use Pull Requests rather than directly pushing development work into the stable branch.

---

# 🧹 Git Ignored Files

The repository ignores files that should not be committed, including:

```text
__pycache__/
venv/
.venv/
.env
*.pyc
.pytest_cache/
.vscode/
.idea/
*.log
```

This keeps generated files, local environments and sensitive configuration out of the repository.

---

# 🚀 Current Project Status

| Component                        | Status         |
| -------------------------------- | -------------- |
| ML Model                         | ✅ Completed    |
| Model Prediction Logic           | ✅ Completed    |
| Pydantic Input Validation        | ✅ Completed    |
| Feature Engineering              | ✅ Completed    |
| City Tier Classification         | ✅ Completed    |
| FastAPI Backend                  | ✅ Completed    |
| Health Check                     | ✅ Completed    |
| Swagger Documentation            | ✅ Completed    |
| Streamlit Frontend               | ✅ Completed    |
| API Integration                  | ✅ Completed    |
| Error Handling                   | ✅ Implemented  |
| Git/GitHub Professional Workflow | 🔄 In Progress |
| Automated Tests                  | 🔄 Planned     |
| Production Improvements          | 🔄 Planned     |

---

# 🔮 Future Improvements

Possible future improvements include:

* Automated unit and API testing
* Improved test coverage
* Better logging
* Improved API error handling
* Environment-based configuration
* Authentication and authorization
* API versioning
* Improved frontend UX
* Model monitoring
* Model metadata and version management
* CI/CD integration

---

# ⚠️ Disclaimer

This project is created for **educational and demonstration purposes**.

The predicted insurance premium category is generated by a Machine Learning model and should not be considered an actual insurance quote or financial decision.

BMI and other derived features are used as model inputs and should not be interpreted as medical or financial advice.

---

# 👨‍💻 Project Goal

The primary goal of InsurePredict is to demonstrate an industry-style workflow for taking a Machine Learning model and building a complete application around it:

```text
Machine Learning Model
        ↓
Python Prediction Logic
        ↓
FastAPI REST API
        ↓
Pydantic Validation
        ↓
Streamlit Frontend
        ↓
Git/GitHub Development Workflow
```

The project focuses not only on Machine Learning prediction but also on **API development, validation, frontend integration, project structure, error handling, version control, and professional software-development practices**.
