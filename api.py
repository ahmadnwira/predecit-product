import pandas as pd
import xgboost as xgb
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)


logger = logging.getLogger(__name__)


# Load trained model
loaded_model = xgb.Booster()
loaded_model.load_model('trained_model.json')

class PredictionService:
    @staticmethod
    def get_predictions(input_data):
        try:
            # Convert input data to DataFrame
            input_df = pd.DataFrame(input_data, index=[0])

            # One-hot encode categorical columns
            input_df = pd.get_dummies(input_df)

            # Convert input data to DMatrix
            dmatrix = xgb.DMatrix(input_df)

            # Use loaded model to make predictions
            predictions = loaded_model.predict(dmatrix)

            return predictions.tolist()
        except Exception as e:
            # Handle any exceptions that occur
            logger.error(f"An error occurred while getting predictions: {e}")
            return []

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input
    input_data = request.get_json()

    # Use PredictionService to get predictions
    predictions = PredictionService.get_predictions(input_data)

    # Return predictions as JSON
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(debug=True, port=5001)