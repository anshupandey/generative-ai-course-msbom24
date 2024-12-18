"""
This script carries the main skeleton of the application.
"""
import streamlit as st
from getPrompt import get_documentation_prompt
from utils_app import get_llm_reponse
from getPrompt import get_file_prompt
import json

st.title("Codoc App")
st.header("Codoc Application")

# add a commponent for file upload
file= st.file_uploader("Upload a .py file",accept_multiple_files=False,)
if file:
    content = file.getvalue().decode('utf-8')
    file_name = file.name
    file_name.replace(".","_")

if st.button("Read File"):
    with st.spinner("Reading Content.."):
        # read content from file
        st.write(content)

#########################################



prompt = get_documentation_prompt(content)
response = get_llm_reponse(prompt=prompt)
if st.button("Get Doc"):
    st.write(response)


if st.button("Export as File"):
    with st.spinner("Perform doc generation .. "):
        prompt = get_file_prompt(file_name[:-3], response)
        python_code = get_llm_reponse(prompt)
        python_code = json.loads(python_code.strip())
        st.write(python_code['code'].strip())
        exec(python_code['code'].strip()) # executing the python code.
        st.write(f"File exported to C/users/admin/desktop/{file_name}.docx")



