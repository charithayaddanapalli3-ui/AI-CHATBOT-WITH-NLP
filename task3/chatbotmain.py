import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Chatbot response patterns
pairs = [

    # Greetings
    [
        r"(hi|hello|hey|hai)",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],

    # Identity
    [
        r"(who are you ?|what is your name ?)",
        ["I am an AI Chatbot developed using Python and NLTK."]
    ],

    # Working
    [
        r"(how do you work ?|how are you working ?)",
        ["I work by matching user input with predefined patterns and generating suitable responses."]
    ],

    [
        r"(what technology do you use ?)",
        ["I use Python programming language and Natural Language Toolkit (NLTK)."]
    ],

    [
        r"(are you ai ?)",
        ["Yes, I am a rule-based AI chatbot."]
    ],

    [
        r"(are you ml based ?)",
        ["No, I do not use machine learning. I am a rule-based chatbot."]
    ],

    [
        r"(what is rule based chatbot ?)",
        ["A rule-based chatbot responds using predefined rules and patterns."]
    ],

    # Features
    [
        r"(what are your features ?)",
        ["My features include text-based interaction, predefined responses, and easy customization."]
    ],

    [
        r"(what can you do ?)",
        ["I can answer basic questions about Python, AI, NLP, and chat with users."]
    ],

    # Advantages
    [
        r"(what are your advantages ?)",
        ["I am fast, simple, easy to implement, and do not require training data."]
    ],

    # Limitations
    [
        r"(what are your limitations ?)",
        ["I cannot learn automatically and depend only on predefined patterns."]
    ],

    # Future Scope
    [
        r"(what is your future scope ?)",
        ["I can be upgraded using machine learning and deep learning techniques."]
    ],

    # General Info
    [
        r"(what is python ?)",
        ["Python is a high-level programming language used for AI, ML, web development, and automation."]
    ],

    [
        r"(what is ai ?)",
        ["AI stands for Artificial Intelligence. It enables machines to simulate human intelligence."]
    ],

    [
        r"(what is nlp ?)",
        ["NLP stands for Natural Language Processing. It helps machines understand human language."]
    ],

    # Exit
    [
        r"(bye|exit|quit)",
        ["Goodbye! Have a nice day 👋"]
    ],

    # Default
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Please ask something else."]
    ]
]


# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("AI Chatbot 🤖")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ").strip().lower()
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break
    response = chatbot.respond(user_input)
    print("Bot:", response)
