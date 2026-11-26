import ollama

stream = ollama.chat(
	model="llama3.2",
	messages=[{"role": "user", "content": "Explain APIs in 5 lines."}],
	stream=True,
)
for chuck in stream:
	print(chuck["message"]["content"], end="", flush=True)
print()