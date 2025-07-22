# 📊 Customer Churn Prediction System

This project was developed as part of the AI/ML Internship Program at Flipkart Pvt Ltd.

## 🎯 Objective

Build an end-to-end machine learning pipeline that predicts customer churn using behavioural and transactional data. The goal is to help businesses to identify customers who are likely to discontinue their service.

---
## 📁 Dataset Description

The dataset contains customer behavioural and transactional data.

| **Feature**                   | **Description**                                 |
| ----------------------------- | ----------------------------------------------- |
| `CustomerID`                  | Unique customer ID                              |
| `Churn`                       | Churn Flag (target variable)                    |
| `Tenure`                      | Tenure of customer in organization              |
| `PreferredLoginDevice`        | Preferred login device of customer              |
| `CityTier`                    | City tier                                       |
| `WarehouseToHome`             | Distance between warehouse and home of customer |
| `PreferredPaymentMode`        | Preferred payment method of customer            |
| `Gender`                      | Gender of customer                              |
| `HourSpendOnApp`              | Hours spent on the mobile app or website        |
| `NumberOfDeviceRegistered`    | Number of devices registered to customer        |
| `PreferedOrderCat`            | Preferred order category in last month          |
| `SatisfactionScore`           | Customer satisfaction score                     |
| `MaritalStatus`               | Marital status of customer                      |
| `NumberOfAddress`             | Number of addresses linked to customer          |
| `Complain`                    | Any complaint raised in the last month          |
| `OrderAmountHikeFromlastYear` | % increase in order amount from last year       |
| `CouponUsed`                  | Total number of coupons used last month         |
| `OrderCount`                  | Total number of orders placed last month        |
| `DaySinceLastOrder`           | Days since the last order                       |
| `CashbackAmount`              | Average cashback received in the last month     |


Target variable:
- `Churn` — Indicates whether the customer churned (1) or stayed (0).

Data Source:
- Got the dataset form [Dataset Link](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)
 
---

## Key Features

- 📌 Data Preprocessing: Handling nulls, encoding, scaling
- 🤖 Model Building: Logistic Regression, Random Forest, XGBoost
- 📊 Model Evaluation: Accuracy, Precision, Recall, F1-Score, AUC
- 🧠 Interpretability: Feature Importance
- 🗂️ Output: Final predictions exported to CSV
- 🌐 Web App: Interactive Flask frontend to make real-time predictions

---

## 🧰 Tech Stack

- Python, Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, XGBoost
- Jupyter Notebook, Visual Studio Code
- Flask (for web app)
- Git & GitHub (version control)

---
## 📊 Feature Importance & Model Performance Summary

Top features influencing churn:
- Tenure
- HourSpendOnApp
- OrderAmountHikeFromlastYear
- CashbackAmount
- SatisfactionScore


Model Accuracy Scores:
| Model              | Accuracy | Precision | Recall | F1-Score | AUC   |
|-------------------|----------|-----------|--------|----------|-------|
| LogisticRegression | 86.2%    | 0.78      | 0.71   | 0.74     | 0.83  |
| RandomForest       | 88.6%    | 0.81      | 0.74   | 0.77     | 0.87  |
| XGBoost            | 89.3%    | 0.84      | 0.76   | 0.80     | 0.89  |

---
## 🔧 Prerequisites
Before you begin, make sure you have the following tools installed on your system.

---

### Step 1: Install Prerequisites

#### 1.1 Install Git

* Download: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* Install Git with default options.
* Confirm:

```bash
git --version
```

#### 1.2 Install Python (3.10+)

* Download: [https://www.python.org/downloads](https://www.python.org/downloads)
* IMPORTANT: Check ✅ **"Add Python to PATH"** during install.
* Confirm:

```bash
python --version
pip --version
```

#### 1.3 Install Visual Studio Code

* Download: [https://code.visualstudio.com](https://code.visualstudio.com)
* Install and open VS Code.

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/Jatin-24/churn-prediction-system.git
cd churn-prediction-system
```

---

### Step 3: Create Python Virtual Environment

#### Using `venv`:

```bash
python -m venv environ
environ\Scripts\activate
```

> You should now see `(environ)` in your terminal prompt.

---

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```
---

### Step 5: Open Project in VS Code

```bash
code .
```

If `code` command doesn't work:

1. Open VS Code manually.
2. Go to `File > Open Folder`.
3. Select the cloned `churn-prediction-system` folder.

---

### Step 6: Install Jupyter Extension in VS Code

1. Go to the **Extensions panel** (Ctrl+Shift+X).
2. Search for **"Jupyter"**.
3. Click **Install**.

Also install:

* **Python extension**

---

### Step 7: Select the Correct Python Kernel

1. Open any notebook (`.ipynb`) like `Logistic_regression_normal.ipynb`.
2. At the top-right, click **Select Kernel**.
3. Choose the interpreter from your virtual environment:

   ```
   Python 3.x (environ)
   ```

---

### Step 8: Run the Notebooks

Click `Run All` or execute cells one by one.

You should see:

* Predictions generated and saved as `.csv` in the `predictions/` folder.
* `.pkl` model files saved in `churn_prediction_frontend/models/`.

---

### Step 9: Launch the Web App

```bash
cd churn_prediction_frontend
python app.py
```

* The terminal will show:

  ```
  * Running on http://127.0.0.1:5000/
  ```
* Open this link in your web browser to access the application.

---

### Step 10: Use the Churn Prediction System

1. 📋 You’ll see a form with input fields for customer details.
2. 🧾 Enter the required values (e.g., gender, age, tenure, etc.).
3. ⚡ Click **"Predict"**.
4. 📊 The predicted churn results will be displayed using:

   * Logistic Regression
   * Random Forest
   * XGBoost

---

## 📝 Final Notes

- ✅ Ensure `models/` and `predictions/` folders are generated after running notebooks.
- 🔒 No personal data used; all input is synthetic or anonymized.

---

## 🧾 License

This project is for educational use only as part of Flipkart's AI/ML Internship Program.

---

## 🙏 Acknowledgments

- Dataset: Kaggle — [E-commerce Customer Churn](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)
- Internship Host: Flipkart Pvt Ltd


