import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load historical data
df = pd.read_csv('data/historical_slots.csv')
df['day'] = df['day'].astype('category').cat.codes
df['time_slot'] = df['time_slot'].astype('category').cat.codes

X = df[['day', 'time_slot']]
y = df['bookings']

# Train Model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok = True)
joblib.dump(model, 'model/slot_predictor.pkl')
print("Model trained and saved to 'model/slot_predictor.pkl'")
