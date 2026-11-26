import ollama

response = ollama.chat(
	model="llama3.2",
	messages=[{"role": "user", "content": "Explain LLMs in 3 lines."}],
)
print(response["message"]["content"])