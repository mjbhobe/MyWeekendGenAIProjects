import os
from typing import List
from rich.pretty import pprint
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from agno.agent import Agent, RunResponse

from agno.models.google import Gemini
import google.generativeai as genai

# load API keys from local .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(
        ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")

# Agent that uses JSON mode
json_mode_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    description="You write movie scripts.",
    response_model=MovieScript,
)
# Agent that uses structured outputs
structured_output_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    description="You write movie scripts.",
    response_model=MovieScript,
    structured_outputs=True,
)

# Get the response in a variable
# json_mode_response: RunResponse = json_mode_agent.run("New York")
# pprint(json_mode_response.content)
# structured_output_response: RunResponse = structured_output_agent.run("New York")
# pprint(structured_output_response.content)

json_mode_agent.print_response("New York")
structured_output_agent.print_response("New York")