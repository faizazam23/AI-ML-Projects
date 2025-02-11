# AI-ML-Projects
# AI-Based Disease Prediction System

## 📌 Overview
This project is an AI-based disease prediction system that uses Machine Learning (ML) to predict possible diseases based on user-provided symptoms. The system is built using Python, trained with medical datasets, and deployed using Flask as a web API.

## 🛠️ Technologies Used
- **Python 3.x**
- **Flask** (for API deployment)
- **Pandas** (for data processing)
- **Scikit-learn** (for ML model training)
- **NLTK** (for text processing, if needed)
- **Pickle** (to save and load the trained model)

## 📂 Project Structure
```
AI-Disease-Prediction/
│── dataset.csv             # Medical dataset with symptoms & diseases
│── train_model.py          # ML model training script
│── disease_model.pkl       # Trained ML model (saved)
│── app.py                  # Flask API for prediction
│── requirements.txt        # List of required libraries
│── README.md               # Project documentation
```

## 🔧 Installation Steps
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/faizazam23/AI-Disease-Prediction.git
cd AI-Disease-Prediction
```

2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Train the Model**
Run the following command to train and save the ML model:
```bash
python train_model.py
```
🔹 This will generate `disease_model.pkl`, which stores the trained model.

4️⃣ **Run the Flask API**
```bash
python app.py
```
🔹 The API will be accessible at:
```
http://127.0.0.1:5000/predict
```

## 🚀 How to Use (Testing the API)
### **Option 1: Using Postman**
1. Open **Postman**
2. Select `POST` method
3. Enter URL: `http://127.0.0.1:5000/predict`
4. Go to **Body** → **Raw** → **JSON**
5. Enter test data:
```json
{
    "symptoms": ["Fever", "Cough"]
}
```
6. Click **Send** 🚀

### **Option 2: Using cURL (Command Line)**
Run this command:
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d "{\"symptoms\": [\"Fever\", \"Cough\"]}"
```
Expected Response:
```json
{
    "Predicted Disease": "Flu"
}
```

## 📌 Future Enhancements
- Improve the model accuracy with a larger dataset
- Create a GUI-based application for better user experience
- Deploy it on a cloud platform (AWS, Heroku, etc.)

## 📩 Contact
👤 **Faiz Azam**  
🔗 GitHub: [faizazam23](https://github.com/faizazam23)  
📧 Email: your-email@example.com
