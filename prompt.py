from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
prompt_format = prompt.format(product="colorful socks")

print("Prompt format: ")
print(prompt_format)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chat_prompt_message = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

print("Chat prompt: ")
print(chat_prompt_message)
print(chat_prompt_message[0])

print(chat_prompt_message[1])