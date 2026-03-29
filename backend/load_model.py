import joblib
import pandas as pd

model = joblib.load("model/model_rumah.pkl")

print(model)

print("Koefisien:", model.coef_)
print("Intercept:", model.intercept_)

data = pd.DataFrame([{
    'sqft_living': 2000,
    'bedrooms': 3,
    'bathrooms': 2,
    'floors': 1,
    'condition': 3,
    'yr_built': 2000
}])

result = model.predict(data)
print(result)