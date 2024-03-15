import pickle
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import pandas as pd

st.title("Hot Dog or Not Dog?")
st.subheader("Classifies your image as a hot dog or not.")


def generate_prediction(img):
    img = img.resize((150,150))
    img_array = np.array(img)
    img_array = img_array.reshape(1,150,150,3)
    st.image(img_array)
    pred = m.predict(img_array)
    df = pd.DataFrame(prediction.T)

# Load model from pickle
# with open('modelarchitechture.pkl', 'rb') as f:
#     m = pickle.load(f)
#     m = tf.keras.models.load_model(m)

with open('modelarchitechture.pkl', 'rb') as f:
    architechture = pickle.load(f)
m = tf.keras.models.model_from_json(architechture)
#m.load_weights('model.weights.h5')

#model = keras.models.load_model(os.getcwd() + '\' + 'first_try.h5')
#model = keras.models.load_model('C:\\Users\\binit\\OneDrive\\Documents\\GA_DSB\\project-4\\Project-4---NN-Hackathon\\app\\first_try.h5')

# Upload image from file for analysis
uploaded_file = st.file_uploader("Upload your image", type=['jpg', 'jpeg', 'png'])

# Or follow a link to an image on the internet
url_placeholder = st.empty()
image_url = st.text_input("Or enter a URL to the image:")

# Or allow user to upload from their webcam   
# pic_from_camera = st.camera_input("Or take a photo with your camera", disabled=True)
# image = None

# if image_url or uploaded_file:
if uploaded_file:
    # if uploaded_file:
    #     st.empty()
        
    image = Image.open(uploaded_file)

    if st.button("Predict!", on_click = generate_prediction(image)):
        st.subheader(f"That's a {pred}!")

    #     image_url = None
    # else:
    #     # st.empty()
    #     try:
    #         response = requests.get(image_url)
    #         image = Image.open(BytesIO(response.content))       
    #     except:
    #         st.error('Invalid link, unable to load image.')
    #         image = None

# if image:
    st.image(image, width=300)

# if pic_from_camera:
#     st.image(pic_from_camera)

# TODO disallow multiple photos
    
# TODO change this to feed into model   
#pred = "HOT DOG!"
#pred = m.predict(image)


# just checking the git branch functionality