import os
from dotenv import load_dotenv, find_dotenv

# load all API keys
_ = load_dotenv(find_dotenv())

print(f"GROQ_API_KEY is {' set.' if os.environ.get('GROQ_API_KEY') else 'not set.'}")
print(f"AGNO_API_KEY is {' set.' if os.environ.get('AGNO_API_KEY') else 'not set.'}")
