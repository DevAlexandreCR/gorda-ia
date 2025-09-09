import os
from openai import OpenAI, RateLimitError, APITimeoutError, APIConnectionError, AuthenticationError, InternalServerError
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatBot:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_KEY", "default-api-key")
        self.client = OpenAI(api_key=self.api_key)

        print(f"ChatBot initialized with API Key: {self.api_key}")
        # Initialize other necessary attributes

    def get_response(self, message: str) -> str:
        try:
            # Validate input
            if not message or message.strip() == "":
                return "Please provide a valid message."
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                max_tokens=150,
                temperature=0.7,
                timeout=30
            )
            
            # Check if response has choices
            if not response.choices or len(response.choices) == 0:
                logger.error("No choices returned from OpenAI API")
                return "Sorry, I couldn't generate a response at the moment."
            
            # Get the response content
            response_content = response.choices[0].message.content
            
            return response_content.strip()
            
        except APIConnectionError as e:
            logger.error("API connection error: %s", e.message)
            return "Sorry, there's a connection issue. Please check your internet and try again."
        except RateLimitError as e:
            logger.error("Rate limit exceeded: %s", e.message)
            return "Sorry, the service is currently busy. Please try again later."
        except APITimeoutError as e:
            logger.error(f"Request timed out: %s", e.message)
            return "Sorry, the request timed out. Please try again."
        except AuthenticationError as e:
            logger.error("Authentication error: %s", e.message)
            return "Sorry, there's an authentication issue. Please check the API key."
        except InternalServerError as e:
            logger.error("API error: %s", e.message)
            return "Sorry, there was an issue with the API. Please try again later."
        except Exception as e:
            logger.error("Unexpected error: %s", e.message)
            return "Sorry, an unexpected error occurred. Please try again later."