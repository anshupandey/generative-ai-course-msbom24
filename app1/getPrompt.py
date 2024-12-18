"""
This script has all the prompts for different stages in the docuemntaiton app.
"""
def get_documentation_prompt(code):
    """
    This function returns the final prompt after embedding it with
    the code provided by user.
    Arguments:
    code: content of .py script; str
    returns
    prompt:Str
    """
    output_format=""" {
    "code_file":"abc.py",
    "class":[
    {"sample_class1":{
    "name":"sample_class1",
    "methods":["func1","func2"],
    }},
    ],
    "functions":[{"funcion1":"used to add two numbers"},{"funcion2":"used to multiply two numbers"}, ]
    }"""
    prompt = f"""
    You are an expert programmer with expertise in Python code writing, reading code and
    drafting detailed, specific, clear description for the provide code.

    Write clear documentation for the functions, class defined in the code separated by triple backticks.

    <context>
    This py file is part of a complex enterprise application, some of the functions, class and their methods
    are used by other files.
    </context>

    Code:
    ```{code}```

    Perform step by step tawsks:
    1. Identify all functions, class and their corresponding methods in the script.
    2. Analyze the content of the function, class and methods to generate one line description for each.
    Include the description of input and output arguments.

    Provide output in JSON format with following structure.
    {output_format}
    """
    return prompt


def get_file_prompt(file_name,json_response):
    prompt = f""" You are an expert python programmer, who works with 
    python packages for generating word files.
    
    Write python code to export a code description to a MS word file.

    THe provided JSON in triple backticks is a documentaiton for a python file
    {file_name}. It has description for all functions, class and its methods
    in the python script.
    your python code should use standard design considerations such as heading, 
    bold text etc. while writing python code.
    Export the description of functions, class and class method to a table in word file.
    The name for output word file should be {file_name}.docx; it should be exported to 
    "C:-->Users-->Admin-->Desktop"
    code description: 
    ```{json_response}```
    ONly provide code which can be directly executed, no other information.
    Provide the response on JSON format with key "code"
    """
    return prompt