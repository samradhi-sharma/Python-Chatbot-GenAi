"""
Flask web interface for the simple Python chatbot
"""
from flask import Flask, render_template, request, jsonify
from chatbot import SimpleChatbot

app = Flask(__name__)
chatbot = SimpleChatbot()

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Process chat messages and return responses"""
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Please type a message.'})
    
    # Get response from chatbot
    response = chatbot.get_response(user_message)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 