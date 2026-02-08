# 🤖 Milestone 3: Model Development & Fine-Tuning

## Objective
Develop, train, and optimize machine learning models for visa status prediction and processing time estimation.

## Models Implemented

### 1. Status Prediction Models

#### Random Forest Classifier
- **Purpose**: Baseline multi-class classification
- **Hyperparameters**: 
  - `n_estimators`: 200
  - `max_depth`: 15
  - `min_samples_split`: 5
- **Performance**:
  - Accuracy: 78.3%
  - F1-Score (Macro): 0.72

#### XGBoost Classifier
- **Purpose**: High-performance gradient boosting
- **Hyperparameters**:
  - `learning_rate`: 0.1
  - `max_depth`: 8
  - `n_estimators`: 300
  - `subsample`: 0.8
- **Performance**:
  - Accuracy: 82.1%
  - F1-Score (Macro): 0.78

#### LightGBM Classifier
- **Purpose**: Fast training for large datasets
- **Performance**:
  - Accuracy: 81.5%
  - F1-Score (Macro): 0.77

### 2. Processing Time Models

#### Survival Analysis (Cox Proportional Hazards)
- **Purpose**: Estimate time-to-decision with censoring
- **C-Index**: 0.74

#### Gradient Boosting Regressor
- **Purpose**: Direct processing days prediction
- **MAE**: 12.3 days
- **RMSE**: 18.7 days

### 3. Transformer-Based Model (Fine-Tuned)

#### Hugging Face BERT Variant
- **Base Model**: `distilbert-base-uncased`
- **Fine-Tuning Dataset**: 50,000 visa case descriptions
- **Training Configuration**:
  - Epochs: 5
  - Batch Size: 16
  - Learning Rate: 2e-5
- **Performance**:
  - Accuracy: 84.2%
  - F1-Score: 0.81

## Hyperparameter Tuning

### Methods Used
1. **Grid Search**: For Random Forest
2. **Optuna**: For XGBoost/LightGBM
3. **Learning Rate Finder**: For Transformer

### Best Configuration (XGBoost)
```python
{
    'learning_rate': 0.08,
    'max_depth': 10,
    'n_estimators': 350,
    'subsample': 0.85,
    'colsample_bytree': 0.9,
    'reg_alpha': 0.1,
    'reg_lambda': 1.0
}
```

## Model Explainability

### SHAP Integration
- Feature importance rankings
- Individual prediction explanations
- Waterfall plots for case analysis

### Top Predictive Features
1. Wage ratio (offered/prevailing)
2. Prior employer approval rate
3. Education level
4. Nationality risk score
5. Premium processing flag

## Model Selection
**Production Model**: XGBoost (best balance of performance and speed)
**Fallback**: Mock predictions for demo/testing

## Deliverables
- [x] Trained model artifacts (.pkl files)
- [x] Hyperparameter tuning reports
- [x] Model comparison analysis
- [x] SHAP explainability integration
