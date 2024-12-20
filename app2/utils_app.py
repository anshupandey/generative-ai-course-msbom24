from openai import OpenAI
import os, io, base64
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_multimodal_reponse(base64_image,model='gpt-4o-mini'):
    messages=[{"role": "system", "content": [{ "type": "text",
          "text": "You are an AI assistant that helps people find information."}]},
        {
            "role": "user",
            "content": [
                {   "type": "text",
                    "text": """extract the statistics, and description from the image 
                    and provide as CSV table. Make sure to provide output in JSON format
                    with keys description, statistics.""",},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ]
    response = client.chat.completions.create(messages=messages,
        model = model, temperature=0,
        response_format={"type":"json_object"} )
    return response.choices[0].message.content


def get_llm_reponse(prompt,model='gpt-4o'):
    response = client.chat.completions.create(
        messages=[{"role":"user","content":prompt}],
        model = model,
        temperature=0,
        response_format={"type":"json_object"}
    )
    return response.choices[0].message.content

def encode_image(img):
    img_bytes = io.BytesIO()
    img.save(img_bytes, format=img.format)
    img_bytes = img_bytes.getvalue()
    b644 = base64.b64encode(img_bytes).decode("utf-8")
    return b644