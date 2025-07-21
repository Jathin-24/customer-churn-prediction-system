from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load models and preprocessors
def load_pickle(filename):
    with open(os.path.join('models', filename), 'rb') as f:
        return pickle.load(f)

logistic_model = load_pickle('logistic_model.pkl')
rf_model = load_pickle('rf_model.pkl')
xgb_model = load_pickle('xgb_model.pkl')
encoder = load_pickle('encoder.pkl')
scaler = load_pickle('scaler.pkl')

@app.route('/')
def index():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_input = request.form.to_dict()
        df = pd.DataFrame([user_input])

        numeric_cols = [
            'Tenure', 'CityTier', 'WarehouseToHome', 'HourSpendOnApp',
            'NumberOfDeviceRegistered', 'SatisfactionScore', 'NumberOfAddress',
            'Complain', 'OrderAmountHikeFromlastYear', 'CouponUsed',
            'OrderCount', 'DaySinceLastOrder', 'CashbackAmount'
        ]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col])

        X = encoder.transform(df)
        X = scaler.transform(X)

        log_pred = logistic_model.predict(X)[0]
        rf_pred = rf_model.predict(X)[0]
        xgb_pred = xgb_model.predict(X)[0]

        return render_template('predict.html',
            log_pred=log_pred,
            rf_pred=rf_pred,
            xgb_pred=xgb_pred,
            input=user_input
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)