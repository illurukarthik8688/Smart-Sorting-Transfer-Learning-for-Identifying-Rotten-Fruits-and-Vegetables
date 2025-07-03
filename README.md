# Smart-Sorting-Transfer-Learning-for-Identifying-Rotten-Fruits-and-Vegetables
# 🍏 Smart Sorting AI — Rotten Fruit Detection Using Transfer Learning

> A deep learning-powered web application to detect whether fruits (specifically apples) are **fresh or rotten** using image classification.

![Smart Sorting Demo](https://img.shields.io/badge/AI-Powered-success?style=flat&logo=python)
![Built with Flask](https://img.shields.io/badge/Flask-WebApp-black?style=flat&logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Model-orange?style=flat&logo=tensorflow)

---

## 🧠 About the Project

**Smart Sorting AI** is a machine learning + web-based solution to automate the detection of spoiled apples.  
It uses **Transfer Learning (MobileNetV2)** to classify images uploaded by users and provides a simple web interface built with **Flask + HTML**.

### 🚀 Use Case Scenarios:
- ✅ **Supermarkets**: Automatically identify spoiled stock on arrival  
- ✅ **Smart Kitchens**: Alert households when fruits go bad  
- ✅ **Food Industry**: Save time and reduce human error in manual sorting

---

## 🎥 Live Demo

> _Click the image to see the working demo_  
<img src="https://user-images.githubusercontent.com/yourusername/demo.gif" width="500" alt="demo" />

---

## 📂 Project Structure

smart-sorting-ai/
├── app.py ← Flask server
├── smart_sorting_model.h5 ← Trained ML model
├── templates/
│ └── index.html ← Frontend UI
├── static/
│ └── uploads/ ← Uploaded test images
├── requirements.txt ← Python dependencies
└── README.md ← This file


---

## 🧪 Model Information

- 🏷️ **Architecture**: MobileNetV2 (Transfer Learning)
- 📊 **Dataset**: 150 training images, 50 testing (Fresh vs Rotten Apples)
- 📈 **Accuracy**: ~90% validation accuracy
- 🔁 **Epochs**: 5
- ⚖️ **Loss Function**: Binary Crossentropy

---

## 🛠️ How to Run the App

### 📦 Step 1: Clone the Repo
```
git clone https://github.com/yourusername/smart-sorting-ai.git
cd smart-sorting-ai

pip install -r requirements.txt

python app.py

```

| Technology          | Role                         |
| ------------------- | ---------------------------- |
| Python + TensorFlow | Model Training (MobileNetV2) |
| Flask               | Backend web framework        |
| HTML + CSS          | Frontend UI                  |
| OpenCV              | Image preprocessing          |


👩‍💻 Author
Illuru Karthik
linkedin: https://www.linkedin.com/in/illuru-karthik-503059269/

---
