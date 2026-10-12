
# CodeAlpha Python Task 4
# Basic Chatbot

def chatbot():
    print("Welcome to the Basic Chatbot!")
    print("Type 'hello', 'how are you', or 'bye'.")
    print("You can also type 'help' to see commands.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "help":
            print("Bot: Try 'hello', 'how are you', or 'bye'.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

    print("Chat ended. Thank you!")

if __name__ == "__main__":
    chatbot()
