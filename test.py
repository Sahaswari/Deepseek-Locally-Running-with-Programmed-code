import ollama # type: ignore

client = ollama.Client()

model = "deepseek-r1:1.5b"
question = 'Hello'

response = client.generate(model=model,prompt=question)
print(response)