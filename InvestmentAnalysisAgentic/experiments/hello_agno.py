import os
from textwrap import dedent
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
import google.generativeai as genai

# load API keys from local .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True
)

# and call our agent
agent.print_response("Tell me about a breaking news story from New York.", stream=True)