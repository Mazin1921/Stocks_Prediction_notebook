from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained LSTM model
model_path = 'lstm_model.pkl'
with open(model_path, 'rb') as file:
    lstm_model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the last 30 days of closing prices from the form
        closing_prices = [float(request.form[f'day{i}']) for i in range(1, 31)]
        final_features = np.array(closing_prices).reshape(1, -1, 1)  # Reshape for LSTM input format

        # Make prediction using the LSTM model
        prediction = lstm_model.predict(final_features)
        predicted_price = prediction[0][0]  # Assuming the model outputs a single price value

        return render_template(
            'index.html',
            prediction_text=f'Predicted Closing Price for Next Day: {predicted_price:.2f}'
        )
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)