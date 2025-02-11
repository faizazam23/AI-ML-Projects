import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy dataset (You can replace this with a real dataset)
data = {
    "Fever": [1, 0, 1, 0, 1, 0],
    "Cough": [1, 1, 0, 0, 1, 0],
    "Fatigue": [0, 1, 1, 1, 0, 1],
    "Headache": [0, 1, 0, 1, 1, 0],
    "Disease": ["Flu", "COVID-19", "Migraine", "Cold", "Flu", "COVID-19"]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df.drop(columns=["Disease"])
y = df["Disease"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the Model
joblib.dump(model, "disease_model.pkl")
print("✅ Model trained and saved successfully!")
