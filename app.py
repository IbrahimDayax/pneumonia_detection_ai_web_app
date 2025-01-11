from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'

# Load your saved model
model = load_model('./pneumonia_detection_cnn_model.h5')

# Allowed extensions for upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(filepath):
    img = image.load_img(filepath, target_size=(150, 150), color_mode='grayscale')
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Expand for batch shape (1, 150, 150, 1)
    prediction = model.predict(img_array)
    # class_name = 'Pneumonia' if prediction[0][0] > 0.5 else 'Normal'
    class_name = 'Normal' if prediction[0][0] > 0.5 else 'Pneumonia'
    return class_name

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            result = predict_image(filepath)
            return render_template('index.html', result=result, image_path=filepath)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
