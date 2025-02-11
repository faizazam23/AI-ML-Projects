from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("disease_model.pkl")

# Symptoms list (same as used during training)
symptoms = ["Fever", "Cough", "Fatigue", "Headache"]

@app.route("/")
def home():
    return render_template("index.html", symptoms=symptoms)

@app.route("/predict", methods=["POST"])
def predict():
    user_symptoms = request.form.getlist("symptoms")
    
    # Convert input to a NumPy array
    input_data = np.zeros(len(symptoms))
    for symptom in user_symptoms:
        if symptom in symptoms:
            input_data[symptoms.index(symptom)] = 1

    # Predict Disease
    prediction = model.predict([input_data])[0]
    
    return jsonify({"Predicted Disease": prediction})

if __name__ == "__main__":
    app.run(debug=True)
