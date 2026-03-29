import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("data/data.csv")

# Drop kolom yang tidak dipakai


# Bersihkan data
df = df.dropna()
df = df[df['price'] > 0]
df = df[df['price'] < 2000000]

# Feature & target
df['house_age'] = 2024 - df['yr_built']
X = df[['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'condition', 'house_age']]
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Training model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)

# Prediksi data test
y_pred = model.predict(X_test)

# Evaluasi
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("📊 MAE:", mae)
print("📈 R2 Score:", r2)

# Simpan model
joblib.dump(model, "model/model_rumah.pkl")

print("✅ Model berhasil ditraining dengan dataset kamu!")