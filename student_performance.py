import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Dataset load
data = pd.read_csv("student_data.csv")

# Input features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_score",
        "sleep_hours"
    ]
]

# Target
y = data["final_marks"]

# Training aur testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model create
model = LinearRegression()

# Model train
model.fit(X_train, y_train)

# Test predictions
predictions = model.predict(X_test)

# Model error
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print("Model trained successfully!")
print("MAE:", mae)
print("MSE:", mse)

# New student prediction
new_student = [[7, 88, 70, 75, 8]]

predicted_marks = model.predict(new_student)

print("Predicted Final Marks:", predicted_marks[0])