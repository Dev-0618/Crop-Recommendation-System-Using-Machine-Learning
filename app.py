from flask import Flask, request, render_template
import numpy as np
import pandas
import sklearn
import pickle

# importing model
# Ensure 'model.pkl', 'standscaler.pkl', and 'minmaxscaler.pkl' are in the same directory as app.py
try:
    model = pickle.load(open('model.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))
    ms = pickle.load(open('minmaxscaler.pkl', 'rb'))
except FileNotFoundError:
    print("Error: Model or scaler files not found. Please ensure 'model.pkl', 'standscaler.pkl', and 'minmaxscaler.pkl' are in the same directory.")
    # Exit or handle the error appropriately, e.g., by using dummy models for development
    model = None
    sc = None
    ms = None

# Define crop dictionary for prediction results and dropdown
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Define ideal conditions for each crop (example data)
# This dictionary is used for the "Get Crop Information" feature
crop_ideal_conditions = {
    "Rice": {"N": "75-100", "P": "30-60", "K": "30-60", "Temp": "25-35°C", "Humidity": "70-80%", "pH": "5.5-6.5", "Rainfall": "1500-2500mm"},
    "Maize": {"N": "80-120", "P": "40-70", "K": "40-80", "Temp": "20-30°C", "Humidity": "60-70%", "pH": "6.0-7.0", "Rainfall": "600-1100mm"},
    "Jute": {"N": "60-80", "P": "20-40", "K": "30-50", "Temp": "24-37°C", "Humidity": "80-90%", "pH": "6.0-7.0", "Rainfall": "1200-1500mm"},
    "Cotton": {"N": "60-90", "P": "30-50", "K": "30-60", "Temp": "21-30°C", "Humidity": "50-60%", "pH": "6.0-7.5", "Rainfall": "500-1000mm"},
    "Coconut": {"N": "50-100", "P": "20-40", "K": "100-200", "Temp": "27-32°C", "Humidity": "70-90%", "pH": "5.5-7.0", "Rainfall": "1300-2500mm"},
    "Papaya": {"N": "50-70", "P": "30-50", "K": "60-80", "Temp": "20-35°C", "Humidity": "60-70%", "pH": "6.0-7.0", "Rainfall": "1000-1500mm"},
    "Orange": {"N": "60-90", "P": "30-50", "K": "60-90", "Temp": "20-35°C", "Humidity": "50-70%", "pH": "6.0-7.5", "Rainfall": "900-1200mm"},
    "Apple": {"N": "40-60", "P": "20-40", "K": "50-80", "Temp": "18-24°C", "Humidity": "60-80%", "pH": "6.0-7.0", "Rainfall": "800-1200mm"},
    "Muskmelon": {"N": "60-80", "P": "40-60", "K": "60-80", "Temp": "24-30°C", "Humidity": "60-70%", "pH": "6.0-7.0", "Rainfall": "500-700mm"},
    "Watermelon": {"N": "60-80", "P": "40-60", "K": "60-80", "Temp": "25-30°C", "Humidity": "60-70%", "pH": "6.0-7.0", "Rainfall": "400-600mm"},
    "Grapes": {"N": "40-60", "P": "20-40", "K": "50-70", "Temp": "15-30°C", "Humidity": "60-70%", "pH": "6.0-7.0", "Rainfall": "500-800mm"},
    "Mango": {"N": "50-70", "P": "20-40", "K": "60-90", "Temp": "24-30°C", "Humidity": "60-80%", "pH": "5.5-7.0", "Rainfall": "1000-2000mm"},
    "Banana": {"N": "80-120", "P": "30-50", "K": "100-150", "Temp": "25-30°C", "Humidity": "70-90%", "pH": "6.0-7.5", "Rainfall": "1500-2500mm"},
    "Pomegranate": {"N": "40-60", "P": "20-30", "K": "50-70", "Temp": "20-35°C", "Humidity": "50-60%", "pH": "6.0-7.0", "Rainfall": "500-800mm"},
    "Lentil": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "18-25°C", "Humidity": "50-60%", "pH": "6.0-7.5", "Rainfall": "300-500mm"},
    "Blackgram": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "25-35°C", "Humidity": "60-70%", "pH": "6.0-7.5", "Rainfall": "400-600mm"},
    "Mungbean": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "25-35°C", "Humidity": "60-70%", "pH": "6.0-7.5", "Rainfall": "400-600mm"},
    "Mothbeans": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "25-35°C", "Humidity": "50-60%", "pH": "6.0-7.5", "Rainfall": "200-400mm"},
    "Pigeonpeas": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "25-35°C", "Humidity": "60-70%", "pH": "6.0-7.5", "Rainfall": "600-1000mm"},
    "Kidneybeans": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "20-28°C", "Humidity": "50-60%", "pH": "6.0-7.0", "Rainfall": "500-800mm"},
    "Chickpea": {"N": "20-30", "P": "40-60", "K": "20-40", "Temp": "18-25°C", "Humidity": "50-60%", "pH": "6.0-7.5", "Rainfall": "400-600mm"},
    "Coffee": {"N": "60-90", "P": "30-50", "K": "60-90", "Temp": "18-24°C", "Humidity": "70-80%", "pH": "6.0-6.5", "Rainfall": "1500-2500mm"}
}

# creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Pass crop names to the template for the dropdown
    return render_template("index.html", crop_names=sorted(crop_dict.values()))

@app.route("/predict", methods=['POST'])
def predict():
    if model is None or sc is None or ms is None:
        return render_template('index.html', result="Error: Model not loaded. Please check server logs.", crop_names=sorted(crop_dict.values()))

    try:
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scale the features using the loaded scalers
        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)
        prediction = model.predict(final_features)

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = "{} is the best crop to be cultivated right there".format(crop)
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
        
        return render_template('index.html', result=result, crop_names=sorted(crop_dict.values()))

    except Exception as e:
        return render_template('index.html', result=f"An error occurred during prediction: {e}", crop_names=sorted(crop_dict.values()))


@app.route('/get_crop_info', methods=['POST'])
def get_crop_info():
    """
    Route to get ideal growing conditions for a selected crop.
    """
    selected_crop = request.form.get('selected_crop')
    info = crop_ideal_conditions.get(selected_crop)

    if info:
        result_info = {
            "crop_name": selected_crop,
            "details": info
        }
    else:
        result_info = {
            "crop_name": selected_crop,
            "details": "No detailed information available for this crop."
        }
    
    return render_template('index.html', result_info=result_info, crop_names=sorted(crop_dict.values()))


@app.route('/contact')
def contact():
    """
    Route for the contact page.
    """
    return render_template("contact.html")

@app.route('/about.html')
def about():
    """
    Route for the about page.
    """
    return render_template("about.html")


# python main
if __name__ == "__main__":
    # Ensure debug=True is only used during development
    app.run(debug=True)
