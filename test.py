import ollama # type: ignore

client = ollama.Client()

model = "deepseek-r1:1.5b"
question = 'What is gen-agent?'

response = client.generate(model=model,prompt=question)
print(response.response)