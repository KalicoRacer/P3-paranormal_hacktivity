# import necessary libraries
import cv2
import tensorflow as tf
import os
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow import keras
from keras.models import load_model
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

# create function to parse the image and predict
def prepare(filepath):
    IMG_SIZE = 100
    x = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    x = cv2.resize(x, (IMG_SIZE,IMG_SIZE))
    x = x.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    x = tf.cast(x, tf.float32)
    return x
    
    
def predict(filepath):    
    CATEGORIES = ['Dog','Cat']
    model = load_model("catsdogs.model")
    predictions = model.predict([prepare(filepath)])
    return CATEGORIES[int(predictions[0][0])]


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/filelink/<file_name>")
def filelink(file_name):
    result = predict(file_name)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
