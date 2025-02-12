from dotenv import load_dotenv, find_dotenv
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv(find_dotenv())


while True:
    repo_id = "deepseek-ai/DeepSeek-R1"
    task = "text-generation"

    llm = HuggingFaceEndpoint(repo_id=repo_id, task=task, temperature=0.5, model_kwargs={"max_length": 200})
    inp = input("Enter a prompt: ")

    response = llm.invoke(inp)
    print(f"\n\n\n\n{response}")
