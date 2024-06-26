def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a chatbot created by OpenAI. What's your name?",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure, I'm here to help! Ask me anything.",
    }

    for key in responses:
        if key in user_input:
            return responses[key]
    
    # Default response if no match is found
    return "I'm sorry, I don't understand that. Can you rephrase?"

if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
