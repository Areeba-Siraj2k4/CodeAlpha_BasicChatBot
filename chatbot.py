
def chatbot():
    print("===== WELCOME TO CODEALPHA CHATBOT =====")
    print("You can talk to me!")
    print("Type 'bye' to exit.")

    while True:
        user = input("\nYou: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif user in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks! How are you?")

        elif user in ["what is your name", "what is your name?"]:
            print("Bot: My name is CodeAlpha Bot.")

        elif user == "help":
            print("Bot: You can say hello, ask my name, or ask how I am.")

        elif user in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
