import ollama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

# Define the question
question = "who is the current pm of qatar?"



template = ChatPromptTemplate.from_messages([
    ("system", "you are helpful assistant based on the user {question} you  will provide the answer?"),
    ("user"," {question}")
])

formattedPrompt = template.format(question=question)

response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": formattedPrompt}])

print(response)
