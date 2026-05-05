import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

# Show first rows of data (to understand structure)
print(data.head())

# Features (input variables)
x = data[['time', 'feedback', 'attendance']]

# Target variable (what we want to predict)
y = data["performance"]

from sklearn.model_selection import train_test_split

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestRegressor

# Create Random Forest Regression model
model = RandomForestRegressor()

# Train the model on training data
model.fit(x_train, y_train)

# Make predictions on test data
predictions = model.predict(x_test)

# Print predictions
print("Predictions:", predictions)

# Convert numeric predictions into performance labels
for p in predictions:
    if p >= 0.7:
        print(f"{p:.2f} → EXCELLENT ⭐")
    elif p >= 0.4:
        print(f"{p:.2f} → AVERAGE ⚠️")
    else:
        print(f"{p:.2f} → STRUGGLING ❌")

import joblib

# Save trained model to file for deployment
joblib.dump(model, "model.pkl")