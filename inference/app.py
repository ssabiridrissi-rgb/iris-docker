import joblib

# Charger le modèle entraîné
model = joblib.load("/model/iris_model.pkl")

# Exemple d'une fleur Iris
sample = [[5.1, 3.5, 1.4, 0.2]]

# Faire la prédiction
prediction = model.predict(sample)

print("Caractéristiques de la fleur :", sample)
print("Classe prédite :", prediction[0])