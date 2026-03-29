import joblib

model = joblib.load("model/model_rumah.pkl")

sqft_living = float(input("Luas rumah (sqft): "))
bedrooms = int(input("Jumlah kamar: "))
bathrooms = float(input("Jumlah kamar mandi: "))
floors = float(input("Jumlah lantai: "))
condition = int(input("Kondisi rumah (1-5): "))
yr_built = int(input("Tahun dibangun: "))

house_age = 2024 - yr_built

result = model.predict([[
    sqft_living,
    bedrooms,
    bathrooms,
    floors,
    condition,
    house_age
]])

print(f"💰 Prediksi harga: {result[0]:,.0f}")