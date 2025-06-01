Crop Recommendation System

This project is a web-based Crop Recommendation System built using Flask, designed to assist farmers and agricultural enthusiasts in making informed decisions about crop cultivation. It recommends the most suitable crops based on specific environmental and soil conditions and provides detailed information about ideal growing conditions for various crops.

Table of Contents

Features

Project Structure

Setup and Installation

Usage

Technologies Used

Team Members

License

Features

Crop Prediction: Users can input soil nutrient levels (Nitrogen, Phosphorus, Potassium), temperature, humidity, pH value, and rainfall to get a recommendation for the best crop to cultivate.

Crop Information Lookup: Users can select a specific crop from a dropdown menu to view its ideal growing conditions (N, P, K, Temperature, Humidity, pH, Rainfall ranges).

Intuitive User Interface: A clean and responsive design built with Bootstrap 5 and Font Awesome for a user-friendly experience.

Navigation: Dedicated pages for Home, Contact, and About sections.

Team Contact Information: A contact page listing team members with their USN and email.

Project Gallery: A visual gallery showcasing aspects of the project's work on the contact page.

Project Structure

your_project_folder/
├── app.py                  # Flask application backend
├── templates/
│   ├── index.html          # Home page with crop prediction and info lookup
│   ├── contact.html        # Contact page with team details and image gallery
│   └── about.html          # About page with project description
├── static/                 # Directory for static files (images, CSS, JS)
│   ├── girl1.jpeg          # Team member image
│   ├── girl2.jpeg          # Team member image
│   ├── girl3.jpeg          # Team member image
│   ├── girl4.jpeg          # Team member image
│   ├── pic1.jpeg           # Project/team image
│   ├── pic2.jpeg           # Project/team image
│   ├── pic3.jpeg           # Project/team image
│   ├── pic4.jpeg           # Project/team image
│   ├── pic5.jpeg           # Project/team image
│   ├── pic6.jpeg           # Project/team image
│   └── img.jpg             # Placeholder image for prediction result card
├── model.pkl               # Trained machine learning model (pickle file)
├── standscaler.pkl         # Standard Scaler for feature scaling (pickle file)
└── minmaxscaler.pkl        # Min-Max Scaler for feature scaling (pickle file)


Setup and Installation

To run this project locally, follow these steps:

Clone the repository:

git clone <your-repository-url>
cd crop-recommendation-system


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install Flask numpy pandas scikit-learn


Note: Ensure you have model.pkl, standscaler.pkl, and minmaxscaler.pkl files in your project's root directory. These are your trained model and scalers.

Place HTML templates:
Make sure index.html, contact.html, and about.html are inside a folder named templates in your project root.

Place static files:
Ensure all image files (girl*.jpeg, pic*.jpeg, img.jpg) are placed inside a folder named static in your project root.

Run the Flask application:

python app.py


Usage

Once the Flask application is running, open your web browser and navigate to http://127.0.0.1:5000/.

Home Page:

Enter the required environmental and soil parameters (Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall) and click "Get Recommendation" to see the suggested crop.

Use the "Explore Crop Ideal Conditions" section to select a crop from the dropdown and view its optimal growing parameters.

Contact Page:

Find contact details for the team members involved in the project.

View a gallery of images related to the project's work.

About Page:

Learn more about the purpose, functionality, and mission of the Crop Recommendation System.

Technologies Used

Backend: Python, Flask

Machine Learning: NumPy, Pandas, Scikit-learn (for model and scalers)

Frontend: HTML5, CSS3, Bootstrap 5, Font Awesome

Templating: Jinja2 (integrated with Flask)

Team Members

Sarah Smyrline R

USN: 1AT22IS095

Email: sarahsmyrlinework@gmail.com

Shafiya Noorain

USN: 1AT22IS097

Email: shafiyanoorain@gmail.com

Zoya Harmain

USN: 1AT22IS126

Email: zoyaharmain@gmail.com

Tamirah Sharieff

USN: 1AT22IS113

Email: tamirah@example.com

License

This project is open-source and available under the MIT License.
