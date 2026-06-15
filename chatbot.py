import json
import os

# Load knowledge base
with open("knowledge_base.json", "r") as file:
    knowledge = json.load(file)

memory = {}

history_file = "conversation_history.txt"

print("=" * 50)
print("AI STUDY ASSISTANT CHATBOT")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! Happy Learning.")
        break

    # Save name in memory
    if "my name is" in user_input.lower():

        name = user_input.lower().replace("my name is", "").strip()

        memory["name"] = name

        response = f"Nice to meet you, {name.title()}!"

    elif "what is my name" in user_input.lower():

        if "name" in memory:
            response = f"Your name is {memory['name'].title()}."
        else:
            response = "I don't know your name yet."

    else:

        response = None

        for key in knowledge:

            if key in user_input.lower():

                response = knowledge[key]
                break

        if response is None:
            response = (
                "Sorry, I don't have information about that yet. "
                "Try asking about Python, Machine Learning, AI, Pandas or NumPy."
            )

    print("Bot:", response)

    # Save chat history
    with open(history_file, "a") as history:
        history.write(f"You: {user_input}\n")
        history.write(f"Bot: {response}\n\n")
