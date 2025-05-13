from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

app = FastAPI()
llm = OpenAI(temperature = 0)