import google.generativeai as genai
from sentence_transformers.util import cos_sim
from datetime import datetime
import streamlit as st
import os

import asyncio

from typing import List, Any

api_key = os.environ["API_KEY"] if "API_KEY" in os.environ else st.secrets["API_KEY"]

def create_chunks(text : str):
    """
    Creates overalpped chunks

    text: string
    
    """
    tokens = text.split(' ')
    chunk_size = int(round(0.1 * len(tokens))) if len(tokens) < 3000 else 300
    overlap = int(round(0.1*chunk_size))
    chunks = [' '.join(tokens[i : i + chunk_size]) for i in range(0, len(tokens), chunk_size - overlap)]
    return chunks

def get_embeddings(text : List):

    """
    Creates embeddings for the raw text fecthed by the scraper from web.

    text : List (List of chunks)
    
    """
    genai.configure(api_key=api_key)
    embeddings = genai.embed_content(
    model="models/embedding-001",
    content=text,
    task_type="clustering", output_dimensionality=128)

    return embeddings

def make_context(query : str, context : List, context_percentage : float):

    """
    Prepares the context for the LLM to answer the user query

    query : str
    context : List
    context_percentage : float (Percentage of context to be passed to the LLM)
    
    """


    query_embedding = get_embeddings(query)
    context_embeddings = get_embeddings(context)

    similarities = cos_sim(query_embedding['embedding'], context_embeddings['embedding'])

    output_context = ''
    context_chunksize = round(context_percentage*len(context)) if len(context) < 20 else 10
    for i in reversed(similarities.argsort()[0][-context_chunksize:]):
        output_context = output_context + ' ' + (context[i.item()])

    return output_context

def current_datetime():
    """return current date and time"""
    return datetime.now()


class Model():
    def __init__(self):
        genai.configure(api_key=api_key)
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=1000,
                temperature=1.0)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest', generation_config=generation_config, safety_settings=None)
    
    def answer(self, query, context):

        """
        query : str
        context : str

        """
        
        messages = [
        {'role':'user',
         'parts': [f"""You are the answer engine. Analyze the provided context carefully and answer the following question and give proper rational behind your response wherever it is needed. Use you skills to answer the query in the best way possible.
                       Donot mention that you are referring a context to answer the query.
                
         
                      Question: {query}
                      Context: 
                      {context}
                      """]}
        ]
        response = self.model.generate_content(messages)
    
        return response.text
    
print(api_key)