"""
Simple Python Chatbot
"""
import random
import re

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            r'hi|hello|hey': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! How can I assist you?"
            ],
            r'how are you': [
                "I'm just a computer program, but I'm functioning well. How are you?",
                "I don't have feelings, but I'm operational. How about you?"
            ],
            r'what is your name': [
                "I'm a simple chatbot created with Python.",
                "You can call me PythonBot."
            ],
            r'bye|goodbye': [
                "Goodbye! Have a nice day!",
                "See you later!",
                "Bye! Come back soon."
            ],
            r'thanks|thank you': [
                "You're welcome!",
                "Happy to help!",
                "No problem!"
            ],
            r'what can you do': [
                "I can have simple conversations. I'm a basic chatbot, so my capabilities are limited.",
                "I can chat with you, but I'm pretty basic. Just a simple demo of a Python chatbot."
            ],
            r'tell me a joke': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What did one wall say to the other wall? I'll meet you at the corner!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ],
            r'what time is it': [
                "I don't have access to the current time. I'm just a simple script!",
                "Sorry, I can't tell the time. I'm a very basic program."
            ],
            r'who made you': [
                "I was created as a simple Python chatbot.",
                "I'm a basic chatbot made with Python."
            ],
            # New patterns and responses
            r'what is python': [
                "Python is a high-level, interpreted programming language known for its readability and versatility.",
                "Python is a popular programming language created by Guido van Rossum in 1991. It's known for its simple syntax and wide range of applications."
            ],
            r'weather|forecast': [
                "I don't have access to real-time weather data. You might want to check a weather service or look outside!",
                "Sorry, I can't tell you the weather. I'm just a simple chatbot without internet access."
            ],
            r'favorite (color|colour)': [
                "If I had to choose, I'd say blue – the color of Python's logo!",
                "Maybe blue, like the Python logo? As a program, I don't actually have preferences."
            ],
            r'how old are you': [
                "I don't have an age. I'm just a computer program!",
                "I was just created recently, so I'm quite young in bot years."
            ],
            r'what is the meaning of life': [
                "42, according to The Hitchhiker's Guide to the Galaxy!",
                "That's a profound question! Many philosophers have spent their lives contemplating it."
            ],
            r'tell me about yourself': [
                "I'm a simple chatbot created with Python. I can have basic conversations but I'm still learning!",
                "There's not much to tell - I'm just a basic Python program designed to chat with humans."
            ],
            r'help': [
                "I can answer simple questions and have basic conversations. Try asking me things like 'tell me a joke' or 'what is Python?'",
                "You can ask me questions, tell me about yourself, or just chat. I'm not very advanced, but I'll try my best to respond!"
            ],
            r'what is flask': [
                "Flask is a lightweight web framework for Python. It's designed to make getting started quick and easy.",
                "Flask is a micro web framework written in Python. It's classified as a microframework because it doesn't require particular tools or libraries."
            ],
            r'how (do you work|are you made)': [
                "I'm built using Python and work by matching patterns in your messages to predetermined responses.",
                "I'm a simple pattern-matching program. I look for keywords in what you say and respond with pre-written answers."
            ],
            r'what is your favorite food': [
                "As a program, I don't eat, but if I could, maybe I'd like... bytes? That's a programmer joke!",
                "I don't eat food, but I do consume data!"
            ]
        }
        
        # Default response when no pattern matches
        self.default_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "Interesting, tell me more.",
            "I don't have a response for that yet.",
            "I'm still learning and don't know how to respond to that."
        ]
    
    def get_response(self, user_input):
        """Generate a response based on user input"""
        # Convert input to lowercase
        user_input = user_input.lower()
        
        # Check for matches in our patterns
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # If no match, return a default response
        return random.choice(self.default_responses)

# Test the chatbot directly if the script is run
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    print("Simple Python Chatbot (type 'bye' to exit)")
    print("-----------------------------------------")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['bye', 'exit', 'quit', 'goodbye']:
            print("\nChatbot: Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print(f"\nChatbot: {response}") 