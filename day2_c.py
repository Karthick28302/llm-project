import ollama, json

response = ollama.chat(
	model="llama3.2",
	messages=[{"role": "user", "content":
		"Extract name, skill and city from: 'Karthick from Bengaluru knows Python and SAP.' "
		"Reply only in JSON with keys name, skill, city."}],
	format="json",
)
data = json.loads(response["message"]["content"])
print(data["name"], data["city"])