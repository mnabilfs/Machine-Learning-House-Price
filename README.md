# ML House Price Prediction

## Cara Menjalankan

### 1. Install dependency
pip install -r requirements.txt

### 2. Training model
python train.py

### 3. Jalankan API
python app.py

### 4. Test API
POST http://127.0.0.1:5000/predict

Body JSON:
{
  "sqft_living": 2000,
  "bedrooms": 3,
  "bathrooms": 2,
  "floors": 2,
  "condition": 3,
  "yr_built": 2000
}