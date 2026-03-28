import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data/data.csv")

# Drop kolom yang tidak dipakai
df = df.drop(columns=[
    'date', 'street', 'city', 'statezip', 'country'
])

# Bersihkan data
df = df.dropna()

# Feature & target
X = df[['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'condition', 'yr_built']]
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Training model
model = LinearRegression()
model.fit(X_train, y_train)

# Simpan model
joblib.dump(model, "model/model_rumah.pkl")

print("✅ Model berhasil ditraining dengan dataset kamu!")