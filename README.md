# 🌾 Crop Recommendation System

A **web-based application** built with **Flask**, designed to help **farmers** and **agriculture enthusiasts** make informed decisions about crop cultivation. It predicts the most suitable crop based on soil and environmental conditions and provides detailed information on ideal growing parameters for various crops.

---

## 📑 Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Setup and Installation](#setup-and-installation)
* [Usage](#usage)
* [Technologies Used](#technologies-used)
* [Team Members](#team-members)
* [License](#license)

---

## ✅ Features

* **🌱 Crop Prediction:**
  Input soil nutrients (Nitrogen, Phosphorus, Potassium), temperature, humidity, pH, and rainfall to get the best crop recommendation.

* **📊 Crop Information Lookup:**
  Select a crop to view its ideal growing conditions including NPK levels, temperature, humidity, pH, and rainfall range.

* **🖥️ Intuitive User Interface:**
  Clean, responsive design using **Bootstrap 5** and **Font Awesome** for a smooth and user-friendly experience.

* **📌 Navigation:**
  Dedicated pages for **Home**, **Contact**, and **About** sections.

* **📞 Team Contact Information:**
  Contact page displays team members' USN and emails.

* **🖼️ Project Gallery:**
  A visual showcase of the project’s progress and team efforts on the contact page.

---

## 📁 Project Structure

```
your_project_folder/
├── app.py                   # Flask backend application
├── templates/               # HTML templates
│   ├── index.html           # Home page with prediction & info lookup
│   ├── contact.html         # Contact page with team info & gallery
│   └── about.html           # About project page
├── static/                  # Static assets (images, CSS, JS)
│   ├── girl1.jpeg           # Team member image
│   ├── girl2.jpeg
│   ├── girl3.jpeg
│   ├── girl4.jpeg
│   ├── pic1.jpeg            # Project images
│   ├── pic2.jpeg
│   ├── pic3.jpeg
│   ├── pic4.jpeg
│   ├── pic5.jpeg
│   ├── pic6.jpeg
│   └── img.jpg              # Prediction result placeholder image
├── model.pkl                # Trained ML model
├── standscaler.pkl          # Standard Scaler for input features
└── minmaxscaler.pkl         # Min-Max Scaler for input features
```

---

## ⚙️ Setup and Installation

Follow the steps below to set up and run the project locally:

### 1. Clone the Repository:

```bash
git clone https://github.com/Dev-0618/Crop-Recommendation-System-Using-Machine-Learning
cd Crop-Recommendation-System-Using-Machine-Learning
```

### 2. Create and Activate a Virtual Environment (Recommended):

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies:

```bash
pip install Flask numpy pandas scikit-learn
```

> ⚠️ **Note:** Ensure `model.pkl`, `standscaler.pkl`, and `minmaxscaler.pkl` are in the project root directory.

### 4. Place Templates and Static Files:

* Move all `.html` files (`index.html`, `contact.html`, `about.html`) into a folder named `templates/`.
* Place all images (`girl*.jpeg`, `pic*.jpeg`, `img.jpg`) into a folder named `static/`.

### 5. Run the Flask App:

```bash
python app.py
```

---

## 🌐 Usage

Once the app is running, open your browser and go to:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### 🏠 Home Page

* Enter environmental and soil parameters:

  * Nitrogen (N), Phosphorus (P), Potassium (K)
  * Temperature, Humidity, pH, Rainfall
* Click **"Get Recommendation"** to see the predicted crop.
* Use the **"Explore Crop Ideal Conditions"** dropdown to check specific crop requirements.

### 📇 Contact Page

* View the contact information (USN and email) of each team member.
* Browse the image gallery showcasing the project development.

### ℹ️ About Page

* Read about the goal, importance, and background of the Crop Recommendation System.

---

## 🛠️ Technologies Used

| Category             | Tools/Libraries                        |
| -------------------- | -------------------------------------- |
| **Backend**          | Python, Flask                          |
| **Machine Learning** | NumPy, Pandas, Scikit-learn            |
| **Frontend**         | HTML5, CSS3, Bootstrap 5, Font Awesome |
| **Templating**       | Jinja2 (integrated with Flask)         |

---

## 👥 Team Members

| Name             | USN        | Email                                                             |
| ---------------- | ---------- | ----------------------------------------------------------------- |
| Sarah Smyrline R | 1AT22IS095 | [sarahsmyrlinework@gmail.com](mailto:sarahsmyrlinework@gmail.com) |
| Shafiya Noorain  | 1AT22IS097 | [shafiyanoorain@gmail.com](mailto:shafiyanoorain@gmail.com)       |
| Zoya Harmain     | 1AT22IS126 | [zoyaharmain@gmail.com](mailto:zoyaharmain@gmail.com)             |
| Tamirah Sharieff | 1AT22IS113 | [tamirah@example.com](mailto:tamirah@example.com)                 |

---

## 📄 License

This project is **open-source** and licensed under the **MIT License**.
