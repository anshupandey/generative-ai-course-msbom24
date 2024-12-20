"""
This script has all the prompts for different stages in the docuemntaiton app.
"""


def get_graph_prompt(file_name,json_response):
    prompt = f""" You are an expert python programmer, who works with 
    python packages for generating visally appealing charts.
    
    Write python code to export a JSON/CSV data to a new graph with complete annotation and information.
    Use only matplotlib, seaborn and plotly. Dont use any other packages.
    Add code to export the grpah at the end to {file_name}.png
    
    THe provided JSON in triple backticks is description for the old graph and statistical data
    your python code should use standard design considerations such as title, colors, legen.
    Choose the appropriate graph type based on data.
    the export path should be "C:-->Users-->Admin-->Desktop". Make sure the path in code to export uses double slashes
    code description: 
    ```{json_response}```
    ONly provide code which can be directly executed, no other information.
    Provide the response on JSON format with key "code"
    """
    return prompt