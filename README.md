Pneumonia Detection AI Web App

This is a Flask-based web application for detecting pneumonia from chest X-ray images using a pre-trained Convolutional Neural Network (CNN). The application allows users to upload an X-ray image and receive a classification result: either "Pneumonia" or "Normal".

Features

User-Friendly Interface: Built with Bootstrap 5 for a responsive and visually appealing design.

AI-Powered Classification: Utilizes a trained CNN model to classify chest X-rays.

Real-Time Results: Provides instant feedback on the uploaded image.

Image Preview: Displays the uploaded image alongside the prediction result.

Project Structure

📂 pneumonia_detection_ai_web_app
├── 📁 static
│   └── 📁 uploads
├── 📁 templates
│   └── index.html
├── app.py
├── pneumonia_detection_cnn_model.h5
└── Pneumonia_Detection_using_CNN.ipynb

app.py: The main Flask application file.

index.html: The HTML template for the web interface.

static/uploads: Directory to store uploaded images.

pneumonia_detection_cnn_model.h5: The pre-trained CNN model for image classification.

Pneumonia_Detection_using_CNN.ipynb: Jupyter notebook used for training the CNN model.

Requirements

Python 3.7+

TensorFlow

Flask

Werkzeug

Bootstrap 5 (via CDN)

Setup

Clone the Repository:

git clone https://github.com/IbrahimDayax/pneumonia_detection_ai_web_app.git
cd pneumonia_detection_ai_web_app

Install Dependencies:

pip install -r requirements.txt

Run the Application:

python app.py

Access the Web App:
Open your browser and navigate to http://127.0.0.1:5000/.

Usage

Upload a chest X-ray image in PNG, JPG, or JPEG format.

Wait for the model to process the image.

View the classification result and the uploaded image.

Model Information

The CNN model was trained on a dataset of chest X-ray images to classify images into two categories:

Pneumonia: Indicates that the patient might have pneumonia.

Normal: Indicates that the patient does not have pneumonia.

Screenshots



Future Enhancements

Add support for multiple image uploads.

Implement additional diagnostic insights, such as probability scores.

Optimize the model for faster predictions.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Dataset: Chest X-ray Images

Frameworks: TensorFlow, Flask, Bootstrap

Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bug reports.

For any questions, please contact Ibrahim Dayax.

