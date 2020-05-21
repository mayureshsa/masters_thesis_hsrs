# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:20:47 2020

@author: ai_ods_lab
"""

# Importing packages

# from tensorflow.keras.applications import ResNet50
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy
# from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io
import json

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)

@app.route("/predict", methods = ["POST"])
def predict():
     # initialize the data dictionary that will be returned from the view
    data = {"success": False}
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))
 
            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(224, 224))
            
            # classify the input image and then return the results
            result = saved_model.predict_classes(image)
            model_predictions = result[0]
	    
            data["predictions"]=map_characters[model_predictions]	

            # data["predictions"]=int(model_predictions)
            
            # indicate that the request was a success
            data["success"] = True
    
    # return the data dictionary as a JSON response
    return flask.jsonify(data)

def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image, axis = 0)
    
    # return the processed image
    return image


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("*** Loading Keras model and Flask starting server... ***"
        "...please wait until server has fully started..."))
    global saved_model 
    
    # change saved_model to the model to be used for prediction
    saved_model = load_model('D:\\Mayuresh\\hsrsnao\\Models\\HSRS_ThesisDataset_6Mar_1030\\History_HSRS_ThesisDataset_6Mar_1030.h5')
    
    global map_characters
    map_characters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'K', 10: 'L', 11: 'M', 12: 'N', 13: 'O', 14: 'P', 15: 'Q', 16: 'R', 17: 'S', 18: 'T', 19: 'U', 20: 'V', 21: 'W', 22: 'X', 23: 'Y'}
    app.run(host= '0.0.0.0')