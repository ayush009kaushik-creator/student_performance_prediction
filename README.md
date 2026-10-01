# 🎓 Student Performance Predictor

> A Machine Learning project that predicts a student's final marks using academic and lifestyle-related factors.

---

## 📌 About the Project

The **Student Performance Predictor** is a Machine Learning project developed using Python and Scikit-learn.

The model predicts a student's expected final marks based on different input factors such as:

- 📚 Study Hours
- 📊 Attendance Percentage
- 📝 Previous Marks
- 📋 Assignment Score
- 😴 Sleep Hours

The project uses **Linear Regression** to learn the relationship between these factors and the student's final marks.

---

## 🎯 Objective

The main objective of this project is to demonstrate how Machine Learning can be used to analyze student-related data and predict academic performance.

---

## 🧠 Machine Learning Model

### Linear Regression

The project uses **Linear Regression**, a supervised Machine Learning algorithm.

The model is trained using historical student data and then used to predict the final marks of a new student.

### Workflow

```text
Student Data
     ↓
Data Loading
     ↓
Feature Selection
     ↓
Train/Test Split
     ↓
Linear Regression
     ↓
Model Training
     ↓
Prediction
     ↓
Performance Evaluation
📊 Input Features
Feature
Description
Study Hours
Number of hours the student studies
Attendance
Student attendance percentage
Previous Marks
Marks obtained previously
Assignment Score
Assignment performance
Sleep Hours
Average sleeping hours
🎯 Target
Final Marks
🛠️ Technologies Used
🐍 Python
🐼 Pandas
🤖 Scikit-learn
📈 Matplotlib
📄 CSV Dataset
💻 VS Code
🌐 GitHub
📂 Project Structure
Student-Performance-Predictor/
│
├── student_data.csv
├── student_performance.py
└── README.md
⚙️ Installation
Clone this repository:
git clone YOUR_GITHUB_REPOSITORY_LINK
Move into the project directory:
cd student-performance-predictor
Install the required libraries:
pip install pandas scikit-learn matplotlib
▶️ How to Run
Run the Python program:
python student_performance.py
The program will:
Load the student dataset.
Separate input features and target values.
Split the data into training and testing sets.
Train the Linear Regression model.
Evaluate the model using MAE and MSE.
Predict the final marks for a new student.
🔍 Example Prediction
Example student:
Study Hours       : 7
Attendance        : 88%
Previous Marks    : 70
Assignment Score  : 75
Sleep Hours       : 8
The trained model then predicts the student's expected final marks.
📏 Model Evaluation
The project uses:
MAE — Mean Absolute Error
MAE measures the average absolute difference between actual and predicted marks.
MSE — Mean Squared Error
MSE calculates the average squared difference between actual and predicted marks.
Lower values generally indicate smaller prediction errors on the evaluation data.
🚀 Future Improvements
The project can be further improved by adding:
🌐 Web-based user interface
📊 Interactive performance graphs
📈 More student data
🤖 Different Machine Learning algorithms
💾 Database integration
📱 Mobile-friendly interface
📋 Student performance reports
⚠️ Disclaimer
This project is created for educational and demonstration purposes. Predictions are based on the provided dataset and should not be treated as an official academic assessment.
👨‍💻 Author
Ayush Kaushik
Machine Learning & Python Project
⭐ If you find this project useful, consider giving the repository a star!
