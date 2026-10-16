print("AI Chatbot: Hello! I am your first chatbot.")

name = input("AI Chatbot: What is your name? ")

print("AI Chatbot: Nice to meet you,", name)

feeling = input("AI Chatbot: How are you feeling today? ").lower().strip()

while True:
    feeling = input(name + ": ").lower().strip()

    if feeling == "bye":
        print("AI Chatbot: Goodbye! Keep building!")
        break

    elif feeling == "happy":
        print("AI Chatbot: That's wonderful!")

    elif feeling == "sad":
        print("AI Chatbot: I hope things get better.")

    elif feeling == "angry":
        print("AI Chatbot: Take a deep breath. Give yourself a moment.")

    elif feeling == "tired":
        print("AI Chatbot: You deserve some rest.")

    elif feeling == "excited":
        print("AI Chatbot: That's exciting! Tell me more.")

    else:
        print("AI Chatbot: Thank you for sharing with me!")
