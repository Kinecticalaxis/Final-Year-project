import os
import openai
import streamlit as stl
from constants import openai_key

os.environ['OPENAI_API_KEY']=openai_key
stl.title("Language search")
input_text=stl.text_input("Enter your query")
from langchain.llms import OpenAI
llm=OpenAI(temperature=0.8)


if input_text :
    stl.write(llm(input_text))
