import os
import json
import pandas as pd
import joblib
from openai import OpenAI


client = OpenAI(api_key="API-KEY")

def create_embedding(text_list):
    
    response = client.embeddings.create(
        model="text-embedding-3-small",   
        input=text_list
    )
    return [item.embedding for item in response.data]

jsons = os.listdir("jsons")
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}", encoding="utf-8") as f:
        content = json.load(f)

    print(f"Creating embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)

# Save DataFrame with embeddings
joblib.dump(df, 'embeddings.joblib')
print("✅ Embeddings saved to embeddings.joblib")
