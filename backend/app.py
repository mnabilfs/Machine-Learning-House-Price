from flask import Flask, jsonify, render_template, request
import joblib
import pandas as pd
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("model/model_rumah.pkl")

@app.route("/")
def home():
    return "API ML Ready 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Ambil tahun sekarang otomatis
    current_year = datetime.now().year

    # Validasi input
    yr_built = int(data["yr_built"])

    if yr_built > current_year:
        return render_template("index.html", result="❌ Tahun tidak valid")

    if yr_built < 1800:
        return render_template("index.html", result="❌ Tahun terlalu lama")

    # Hitung house_age
    house_age = current_year - yr_built

    input_data = pd.DataFrame([{
        "sqft_living": float(data["sqft_living"]),
        "bedrooms": int(data["bedrooms"]),
        "bathrooms": float(data["bathrooms"]),
        "floors": float(data["floors"]),
        "condition": int(data["condition"]),
        "house_age": house_age
    }])

    prediction = max(0, model.predict(input_data)[0])

    return jsonify({
        "predicted_price": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)