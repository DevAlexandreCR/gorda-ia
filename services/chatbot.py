import os

class ChatBot:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_KEY", "default-api-key")
        print(f"ChatBot initialized with API Key: {self.api_key}")
        # Initialize other necessary attributes

    def get_response(self, message: str) -> str:
        # Logic to interact with the chatbot API using the api_key
        # and return the response
        return "This is a mock response to the message: " + message