"""
This script carries the main skeleton of the application.
"""
import streamlit as st
from utils_app import get_llm_reponse, get_multimodal_reponse, encode_image
import json
from PIL import Image
from getPrompt import get_graph_prompt

st.title("Graph Generation App")
st.header("Get New Graph from OLD")

# add a commponent for file upload
image= st.file_uploader("Upload an image file",accept_multiple_files=False,type=['png','jpg'])

if image is not None:
    img = Image.open(image)
    st.image(img,width=250)

    if st.button("Get Description"):
        base64_img = encode_image(img)
        response = get_multimodal_reponse(base64_img)
        st.write(response)

        if st.button("Get New Graph"):
            filename = "newimage.png"
            filename = filename[:5]+"_new"
            print(filename)
            prompt = get_graph_prompt(filename, response)
            print(prompt)
            st.write(prompt)
            code = get_llm_reponse(prompt)
            python_code = json.loads(code.strip())
            st.write(python_code['code'].strip())
            exec(python_code['code'].strip()) # executing the python code.
            st.write(f"File exported to C/users/admin/desktop/{filename}.png")
            newimage = Image.open(r'C:\\Users\\Admin\\Desktop\\newim_new.png')
            st.image(newimage)







