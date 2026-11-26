import ollama

def ask(question, temperature=0.7):
	response = ollama.chat(
		model="llama3.2",
		messages=[
			{"role": "system", "content": "You are a friendly Python teacher. Keep answers under 4 lines."},
			{"role": "user", "content": question},
		],
		options={"temperature": temperature},
	)
	return response["message"]["content"]

print("Temp 0:", ask("What is a list in Python?", 0))
print("Temp 1:", ask("What is a list in Python?", 1))