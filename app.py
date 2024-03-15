# import pickle
import streamlit as st

st.title("Hot Dog or Not Dog?")
st.subheader("Classifies your image as a hot dog or not.")

# Load model from pickle
# with open('../models/austen-poe-detector.pkl', 'rb') as f:
#     model = pickle.load(f)


# Upload image from file for analysis
uploaded_file = st.file_uploader("Upload your image", type=['jpg', 'jpeg', 'png'])
# Or allow user to upload from their webcam   
# pic_from_camera = st.camera_input("Or take a photo with your camera", disabled=True)

if uploaded_file:
    st.image(uploaded_file, caption='x', use_column_width=True)

# if pic_from_camera:
#     st.image(pic_from_camera)

# TODO disallow multiple photos
    
# TODO change this to feed into model    
pred = 'Hot Dog' # model.predict([text])[0]

if st.button("Submit"):
    st.write(f"That's a {pred}!")