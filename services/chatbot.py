import os
from openai import OpenAI, RateLimitError, APIConnectionError, AuthenticationError, InternalServerError
from utils.logger import get_logger

# Get logger instance
logger = get_logger()

class ChatBot:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_KEY", "default-api-key")
        self.client = OpenAI(api_key=self.api_key)

    def get_response(self, message: str) -> str:
        try:
            logger.info(f"Processing message request: {message[:10]}...")
            
            response = self.client.responses.create(
                model="gpt-3.5-turbo",
                input=message,
                prompt={
                    "id": "pmpt_68bf9e8505388194b3ed8f3b76d5699d0b4eba68f39ab425",
                    "version": "2"
                }
            )
            
            response_content = response.output_text
            
            logger.info("Successfully generated response")
            return response_content.strip()
            
        except APIConnectionError as e:
            logger.error(f"API connection error: {e}")
            return "Sorry, there's a connection issue. Please check your internet and try again."
        except RateLimitError as e:
            logger.error(f"Rate limit exceeded: {e}")
            return "Sorry, the service is currently busy. Please try again later."
        except AuthenticationError as e:
            logger.error(f"Authentication error: {e}")
            return "Sorry, there's an authentication issue. Please check the API key."
        except InternalServerError as e:
            logger.error(f"API error: {e}")
            return "Sorry, there was an issue with the API. Please try again later."
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            return "Sorry, an unexpected error occurred. Please try again later."
