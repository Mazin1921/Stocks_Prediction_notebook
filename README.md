# 📈 Stock Price Prediction with Flask Web App

This repository provides a full solution for predicting stock prices using an LSTM model. It includes a Jupyter Notebook for training and a **Flask Web App** for real-time predictions and visualization.  

---

## 📊 Project Overview

The project follows these main steps:

- 📥 **Importing Libraries and Datasets**: Load essential libraries and stock price data.
- 🧮 **Pivoting the Data**: Organize the data into a suitable format for analysis.
- 📈 **Plotting Close Prices**: Visualize the closing stock prices over time.
- 📉 **Moving Averages**: Compute and plot 10-day and 100-day moving averages.
- 🔄 **Normalizing Data**: Scale data using MinMaxScaler for better LSTM training.
- 🧠 **LSTM Model**: Train a Long Short-Term Memory (LSTM) neural network.
- 💾 **Model Saving**: Save the trained model as `lstm.pkl` using `joblib`.
- 🌐 **Deployment**: Build a user-friendly Flask web app to display predictions interactively.

---

## 🔧 Requirements

Install the necessary Python libraries with or simply refer requirements.txt:

```bash
pip install numpy pandas matplotlib scikit-learn tensorflow keras flask joblib
```

---

## 👨‍💻 How to Use This Project

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/stock-price-predictor.git
cd stock-price-predictor
```

---

### ✅ Step 2: Train and Save the Model

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Run the cells to:
   - Load and process stock data
   - Train the LSTM model
   - Save the trained model as `lstm.pkl`

---

### ✅ Step 3: Run the Flask Web App

1. Ensure `lstm.pkl` is present in the same directory as `app.py`.
2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to:  
   👉 `http://localhost:5000`

---

## 🌐 Flask Web App UI

### 🖼️ User Interface Preview of the LSTM Stock Predictor Web App (Last 30-days Close Price)

![image](https://github.com/user-attachments/assets/25e22e92-2412-4d9e-9704-864662056620)
![image](https://github.com/user-attachments/assets/073df060-288d-47ee-835a-9dc0ddf593ab)



---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests for improvements or new features.

---

## 🪪 License

This project is licensed under the **MIT License**.
