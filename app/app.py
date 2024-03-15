# import pickle
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Hot Dog or Not Dog?")
st.subheader("Classifies your image as a hot dog or not.")

# Load model from pickle
# with open('../models/austen-poe-detector.pkl', 'rb') as f:
#     model = pickle.load(f)


# Upload image from file for analysis
uploaded_file = st.file_uploader("Upload your image", type=['jpg', 'jpeg', 'png'])

# Or follow a link to an image on the internet
url_placeholder = st.empty()
image_url = st.text_input("Or enter a URL to the image:")

# Or allow user to upload from their webcam   
# pic_from_camera = st.camera_input("Or take a photo with your camera", disabled=True)
image = None

if image_url or uploaded_file:
    if uploaded_file:
        st.empty()
        
        image = Image.open(uploaded_file)
        image_url = None
    else:
        # st.empty()
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))       
        except:
            st.error('Invalid link, unable to load image.')
            image = None

if image:
    st.image(image, width=300)

# if pic_from_camera:
#     st.image(pic_from_camera)

# TODO disallow multiple photos
    
# TODO change this to feed into model    
pred = 'Hot Dog' # model.predict([text])[0]

if st.button("Predict!"):
    st.subheader(f"That's a {pred}!")

# just checking the git branch functionality