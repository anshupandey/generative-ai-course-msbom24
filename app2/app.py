"""
This script carries the main skeleton of the application.
"""
import streamlit as st
from utils_app import get_llm_reponse, get_multimodal_reponse
import json, base64, io
from PIL import Image

st.title("Graph Generation App")
st.header("Get New Graph from OLD")

# add a commponent for file upload
image= st.file_uploader("Upload an image file",accept_multiple_files=False,type=['png','jpg'])

if image is not None:
    img = Image.open(image)
    st.image(img,width=250)

    if st.button("Get Description"):
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=img.format)
        img_bytes = img_bytes.getvalue()
        b644 = base64.b64encode(img_bytes).decode("utf-8")
        response = get_multimodal_reponse(b644)
        st.write(response)

