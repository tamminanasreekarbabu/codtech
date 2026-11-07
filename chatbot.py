
print("Chatbot: Hello! Welcome to my chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. How can I help you?")

    elif user == "your name":
        print("Bot: I am Python Chatbot.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
