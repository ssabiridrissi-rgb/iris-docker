from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import redis

app = FastAPI()

# Charger le modèle Iris
model = joblib.load("/model/iris_model.pkl")

# Connexion à Redis
redis_client = redis.Redis(
    host="base",
    port=6379,
    decode_responses=True
)


# Caractéristiques d'une fleur
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def accueil():
    return {"message": "Bienvenue dans l'API Iris"}


@app.post("/predict")
def predict(data: IrisInput):

    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(features)

    # Augmenter le compteur Redis
    redis_client.incr("prediction_count")

    return {"prediction": int(prediction[0])}


@app.get("/stats")
def stats():

    count = redis_client.get("prediction_count")

    return {"total_predictions": int(count or 0)}