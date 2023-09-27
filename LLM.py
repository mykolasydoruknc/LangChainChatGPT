from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import json

with open('config.json') as config_file:
    config_data = json.load(config_file)

openai_api_key = config_data.get("OPENAI_API_KEY")
# Initialize OpenAI with your API key
llm = OpenAI(openai_api_key=openai_api_key)

# Initialize ChatOpenAI with the OpenAI instance
chat_model = ChatOpenAI(openai_api_key=openai_api_key)
text = "What would be a good company name for a company that makes colorful socks?"
# Use the models
llm_response = llm.predict(text)
chat_model_response = chat_model.predict(text)

# Print the responses
print("OpenAI Response:")
print(llm_response)

print("\nChatOpenAI Response:")
print(chat_model_response)


messages = [HumanMessage(content=text)]

llm_messages = llm.predict_messages(messages)

chat_model_messages = chat_model.predict_messages(messages)

# Print the responses
print("OpenAI Messages:")
print(llm_messages)

print("\nChatOpenAI Messages:")
print(chat_model_messages)