from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import routes_cultivo

app = FastAPI(
    title="Crop Recommendation API",
    description="API cultivos con RandomForest y SVM"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://trabajoml.onrender.com"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routes_cultivo.router) 