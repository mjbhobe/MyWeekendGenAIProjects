import os
from textwrap import dedent
from dotenv import load_dotenv
import yaml
import pathlib

from agno.agent import Agent
from agno.models.google import Gemini
import google.generativeai as genai

# import my tools
from finanalysis.tools import FinancialAnalysisTools

# load API keys from local .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# instantiate the LLM & ask a question
llm = Gemini(id="gemini-2.0-flash")

config_file_path = pathlib.Path(__file__).parent / "config/prompts.yaml"
assert (
    config_file_path.exists()
), f"FATAL ERROR: configuration file {config_file_path} does not exist!"

# load prompts from config
config = None
with open(str(config_file_path), "r") as f:
    config = yaml.safe_load(f)

if config is None:
    raise RuntimeError(
        f"FATAL ERROR: unable to read from configuration file at {config_file_path}"
    )


agent = Agent(
    name="Financial Analysis Agent",
    model=llm,
    tools=[FinancialAnalysisTools()],
    goal=dedent("""
        Analyse the financial ratios of a company and come up with a recommendation
        of the long term investment potential of the company, with reasons for the same.
    """),
    description=dedent(config["prompts"]["system_prompt"]),
    instructions=dedent(config["prompts"]["financial_analysis_prompt"]),
    markdown=True,
    show_tool_calls=True,
    debug_mode=True,
)

# and call our agent
agent.print_response("Analyze performance of AMZN", stream=True)