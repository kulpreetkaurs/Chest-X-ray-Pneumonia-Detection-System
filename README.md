Project Overview

The Chest X-ray Pneumonia Detection System is a deep learning-based image classification project developed using Python, TensorFlow, Keras, and Streamlit. It is designed to classify chest X-ray images into two categories: Pneumonia and Normal.

The project involves collecting and organizing chest X-ray images, preparing the dataset for model development, training a classification model, and building an interactive web application that allows users to upload an X-ray image and receive a predicted result.

Objectives

Develop a deep learning-based system for classifying chest X-ray images.

Prepare and organize image data for model development and evaluation.

Apply image preprocessing techniques to make images suitable for model prediction.

Build an interactive web application using Streamlit.

Demonstrate the practical application of deep learning in medical image classification.

Technologies Used

Python — Core programming language

TensorFlow and Keras — Deep learning model loading and prediction

NumPy — Numerical operations and image array processing

Pillow (PIL) — Image loading and manipulation

Streamlit — Interactive web application development

Project Workflow

Data Collection: Collected and organized chest X-ray images for the classification task.

Dataset Preparation: Organized the images into training, validation, and testing folders.

Model Development: Developed a deep learning classification model using the prepared image dataset.

Image Preprocessing: Resized uploaded images to 128 × 128 pixels, converted them to RGB format, and normalized pixel values to the range 0–1.

Model Integration: Loaded the trained Keras model from the pneumonia_classifier.keras file.

Application Development: Created a Streamlit interface that accepts uploaded chest X-ray images and displays the predicted classification.

Features

Upload chest X-ray images in JPG, JPEG, and PNG formats.

Preview the uploaded image.

Automatically preprocess images before prediction.

Classify images as Pneumonia or Normal.

Display prediction results through an interactive web interface.

Provide a simple interface for demonstrating image classification.

Project Structure

chest-xray-pneumonia-detection/
│
├── app.py
├── pneumonia_classifier.keras
├── requirements.txt
├── README.md
│
└── dataset/
    ├── train/
    ├── val/
    └── test/

The dataset folder is optional for running the deployed application if the trained model is already available. The application uses the saved model to make predictions on uploaded images.

Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

Replace YOUR_USERNAME and YOUR_REPOSITORY with your GitHub username and repository name.

2. Navigate to the project directory

cd YOUR_REPOSITORY

3. Create a virtual environment (optional)

python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1

4. Install dependencies

python -m pip install -r requirements.txt

5. Run the application

python -m streamlit run app.py

The application will open in your browser, usually at:

http://localhost:8501

How to Use the Application

Launch the application.

Upload a chest X-ray image in JPG, JPEG, or PNG format.

View the uploaded image in the application.

Wait for the model to process the image.

View the predicted classification: Pneumonia or Normal.

Skills Demonstrated

Python programming

Deep learning and image classification

Image data collection and preprocessing

Dataset organization and splitting

TensorFlow and Keras model integration

Streamlit application development

Model inference and deployment preparation

Future Enhancements

Display prediction confidence scores.

Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.

Improve model generalization using data augmentation and additional validation.

Add clearer error handling for invalid or unsupported images.

Explore deployment and monitoring improvements.

Disclaimer

This project is intended for educational and demonstration purposes only. It is not a clinically validated diagnostic system and must not be used to diagnose pneumonia or make medical decisions. Any medical concerns should be evaluated by a qualified healthcare professional.