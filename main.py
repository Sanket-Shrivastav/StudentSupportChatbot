from chatbot.chatbot import StudentSupportChatbot

def main():
    chatbot = StudentSupportChatbot("data/faqs.json")
    print("🎓 Student Support Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
