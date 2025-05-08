# Python Simple Chatbot
![image](https://github.com/user-attachments/assets/4043db2a-ddea-47bb-b3a7-3878fdbcce23)


A simple chatbot implementation using Python and Flask.

## Features

- Pattern-based responses using regular expressions
- Web interface using Flask
- Easy to extend with new patterns and responses
- Simple and lightweight design

## Getting Started

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the Flask web server:
```
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:8080
```

## Project Structure

- `app.py` - Flask web application
- `chatbot.py` - Core chatbot implementation
- `templates/` - HTML templates
- `static/` - CSS and JavaScript files

## Adding New Responses

To add new responses, edit the `self.responses` dictionary in `chatbot.py`:

```python
self.responses = {
    r'pattern|alternative': [
        "Response 1",
        "Response 2"
    ],
    # Add more patterns and responses here
}



``` 
