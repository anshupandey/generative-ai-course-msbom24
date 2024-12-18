from openai import OpenAI
import os
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_llm_reponse(prompt,model='gpt-4o'):
    response = client.chat.completions.create(
        messages=[{"role":"user","content":prompt}],
        model = model,
        temperature=0,
        response_format={"type":"json_object"}
    )
    return response.choices[0].message.content
