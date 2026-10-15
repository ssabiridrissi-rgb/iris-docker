from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Charger le dataset Iris
iris = load_iris()

X = iris.data
y = iris.target

# Séparer les données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Créer le modèle
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Entraîner le modèle
model.fit(X_train, y_train)

# Évaluer le modèle
accuracy = model.score(X_test, y_test)

print(f"Accuracy : {accuracy:.2f}")

# Créer le dossier de sortie
os.makedirs("/model", exist_ok=True)

# Sauvegarder le modèle
joblib.dump(model, "/model/iris_model.pkl")

print("Modèle sauvegardé dans /model/iris_model.pkl")