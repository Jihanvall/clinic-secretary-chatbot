from chatbot_config import create_chat

chat = create_chat()

print("Clinic Assistant is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)