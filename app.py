from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model/model_rumah.pkl")

@app.route("/")
def home():
    return "API ML Ready 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = [[
        data["sqft_living"],
        data["bedrooms"],
        data["bathrooms"],
        data["floors"],
        data["condition"],
        data["yr_built"]
    ]]

    prediction = model.predict(features)

    return jsonify({
        "predicted_price": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)