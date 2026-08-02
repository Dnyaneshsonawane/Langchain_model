

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="openai/gpt-4",
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)