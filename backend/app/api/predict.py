"""
AI Prediction API Endpoints
"""

from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import random

from app.models.schemas import (
    PredictRequest,
    PredictionResult,
    StatusProbabilities,
    PredictionExplanation,
    ExplanationFactor,
)
from app.ml.predictor import get_predictor

router = APIRouter()

# Get global predictor
predictor = get_predictor()


@router.post("/status", response_model=PredictionResult)
def predict_status(request: PredictRequest):
    """
    Predict visa status probabilities.
    
    Uses XGBoost/LightGBM models to predict the probability
    of Approved, RFE, or Denied outcomes.

    NOTE: This is intentionally synchronous (def) instead of async (async def)
    to offload the CPU-bound ML inference to a thread pool, preventing
    blocking of the main asyncio event loop.
    """
    # Generate prediction using ML model
    prediction = predictor.predict_status(request.case_id, request.case_data)
    return prediction


@router.post("/processing-time", response_model=PredictionResult)
def predict_processing_time(request: PredictRequest):
    """
    Estimate visa processing time.
    
    Uses survival analysis models to estimate remaining
    days until decision with confidence intervals.

    NOTE: This is intentionally synchronous (def) instead of async (async def)
    to offload the CPU-bound ML inference to a thread pool.
    """
    prediction = predictor.predict_processing_time(request.case_id, request.case_data)
    return prediction


@router.get("/explain/{case_id}")
def get_prediction_explanation(case_id: str):
    """
    Get SHAP-based explanation for a prediction.
    
    Returns feature importance and top factors
    influencing the prediction.

    NOTE: This is intentionally synchronous (def) instead of async (async def)
    to offload the CPU-bound ML inference to a thread pool.
    """
    explanation = predictor.get_explanation(case_id)
    return explanation
