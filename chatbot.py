import ollama

messages = [
	{"role": "system", "content": "You are a helpful assistant. Be concise."}
]

print("Chatbot ready. Type 'quit' to exit.\n")
while True:
	user_input = input("You: ")
	if user_input.lower() == "quit":
		break

	messages.append({"role": "user", "content": user_input})

	reply = ""
	print("Bot: ", end="", flush=True)
	for chuck in ollama.chat(model="llama3.2", messages=messages, stream=True):
		text = chuck["message"]["content"]
		print(text, end="", flush=True)
		reply += text
	print("\n")

	messages.append({"role": "assistant", "content": reply})