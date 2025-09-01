from dotenv import load_dotenv     # load env file
import os                          # one file to other file
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig       # open ai sdk framework

load_dotenv()   # loading env variable

gemini_api_key = os.getenv("GEMINI_API_KEY")            # getting gemini key from .env file through the os.getenv

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
)