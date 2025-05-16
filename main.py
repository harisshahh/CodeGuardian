from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

app = FastAPI()
llm = OpenAI(temperature = 0.3)

class CodeRequest(BaseModel):
    code:str
    goal:str

@app.post("/analyze")
def analyze: req(CodeRequest):
    template = PromptTemplate.from_template(
        "You are an expert software engineer/code analyzer. Please {goal} the following code:\n\n{code}"
    )
    prompt = template.format(goal = req.goal, code = req.code)
    response = llm(prompt)
    return {"result": response}
