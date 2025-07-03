from flask import Flask, render_template, request
import tensorflow as tf
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
model = tf.keras.models.load_model('smart_sorting_model.h5')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    filename = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)

            img = Image.open(filename).convert('RGB').resize((224, 224))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            pred = model.predict(img_array)[0][0]

            if pred >= 0.5:
                result = f"🍏 Rotten Apple ({pred:.2f})"
            else:
                result = f"🍎 Fresh Apple ({1 - pred:.2f})"

    return render_template('index.html', result=result, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

