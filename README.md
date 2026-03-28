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
  "area": 100,
  "bedrooms": 3,
  "bathrooms": 2
}