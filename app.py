import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

st.title("Chest X-ray Pneumonia Detection")

model = load_model("pneumonia_classifier.keras")

uploaded_file = st.file_uploader(
    "Upload Chest X-ray Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=300)

    img = img.resize((128,128))
    img = img.convert("RGB")

    img_array = image.img_to_array(img)
    img_array = img_array/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    if prediction[0][0] > 0.5:
        st.error("Prediction : Pneumonia")
    else:
        st.success("Prediction : Normal")