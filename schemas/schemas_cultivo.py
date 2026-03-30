from pydantic import BaseModel

class CultivoDat(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


class PredictionOutput(BaseModel):
    model: str
    prediction: str