from fastapi import APIRouter
from services.service_cultivo import  predictSVM, predictRF
from schemas.schemas_cultivo import CultivoDat, PredictionOutput

router = APIRouter()


@router.get("/")
def home():
    return {"message": "sin error"}



@router.post("/predict/compare")
def models(data: CultivoDat):

    input_data = [
        data.N, 
        data.P, 
        data.K,
        data.temperature, 
        data.humidity,
        data.ph, 
        data.rainfall
    ]

    RFpred = predictRF(input_data)
    SVMpred = predictSVM(input_data)

    return {
        "RandomForest": RFpred,
        "SVM": SVMpred
    }