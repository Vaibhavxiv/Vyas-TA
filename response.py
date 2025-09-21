import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
from openai import OpenAI

client = OpenAI(api_key="API-KEY")  


def create_embedding(text_list):
    response = client.embeddings.create(
        model="text-embedding-3-small",  
        input=text_list
    )
    return [item.embedding for item in response.data]


def inference(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # fast + cheap; 
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


df = joblib.load("embeddings.joblib")


def answer_query(incoming_query,top_results=5):

    question_embedding = create_embedding([incoming_query])[0]

    # Find similarities
    similarities = cosine_similarity(np.vstack(df["embedding"]), [question_embedding]).flatten()
    max_indx = similarities.argsort()[::-1][0:top_results]
    new_df = df.loc[max_indx]

    
    prompt = f"""
    You are a helpful teaching assistant for my Sigma Web Development course.

    I will give you several video subtitle chunks. Each chunk has:
    - "title": the video title
    - "number": the video number
    - "start" and "end": timestamps in seconds
    - "text": transcript of what is taught in that segment

    Here are the relevant chunks:
    {new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}

    User question:
    "{incoming_query}"

    Your task:
    1. If the question is related to the course, answer it in a clear, human-like explanation.
    2. Tell the user **which video(s)** cover this topic, and give the **timestamps** where it is taught.
    3. Summarize briefly what is explained in that section of the video.
    4. If the question is unrelated to the course, politely say you can only answer questions about this course.

    Do not mention JSON or the format above in your answer — that is just background for you.
    Speak directly to the student as if you are guiding them personally.
    """



    answer = inference(prompt)
    return answer,new_df



