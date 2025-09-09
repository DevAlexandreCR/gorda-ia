import os
from openai import OpenAI, RateLimitError, APIConnectionError, AuthenticationError, InternalServerError
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
            
            response = self.client.responses.create(
                model="gpt-5-nano",
                input=message,
                max_output_tokens=50,
                timeout=30,
                instructions="You are a assistant and the service we provided is like uber. we need to get the place name where user wants to be picked up."
            )
            
            # Get the response content
            response_content = response.output_text
            
            return response_content.strip()
            
        except APIConnectionError as e:
            logger.error("API connection error: %s", e.message)
            return "Sorry, there's a connection issue. Please check your internet and try again."
        except RateLimitError as e:
            logger.error("Rate limit exceeded: %s", e.message)
            return "Sorry, the service is currently busy. Please try again later."
        except AuthenticationError as e:
            logger.error("Authentication error: %s", e.message)
            return "Sorry, there's an authentication issue. Please check the API key."
        except InternalServerError as e:
            logger.error("API error: %s", e.message)
            return "Sorry, there was an issue with the API. Please try again later."
        except Exception as e:
            logger.exception("Unexpected error occurred")
            raise
