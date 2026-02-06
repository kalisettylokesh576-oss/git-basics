import openai

openai.api_key = "YOUR_API_KEY_HERE"

def ai_agent(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    reply = ai_agent(user)
    print("AI:", reply)