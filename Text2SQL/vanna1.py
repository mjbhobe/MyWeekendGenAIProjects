import os, sys
from dotenv import load_dotenv

# from rich import print

import vanna

# from vanna.remote import VannaDefault
from vanna.openai import OpenAI_Chat
from vanna.chromadb import ChromaDB_VectorStore
import google.generativeai as genai
from dbutils import get_db_params
import streamlit as st


# load all API keys
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# @see: https://vanna.ai/docs/postgres-openai-vanna-vannadb/

# Your API key from https://vanna.ai/account/profile
# this has been saved to local .env file
api_key = os.getenv("VANNA_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "GPT-4o"


# # Your model name from https://vanna.ai/account/profile
# vanna_model_name = "chinook_mjb"
# vn = VannaDefault(model=vanna_model_name, api_key=api_key)


class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


vn = MyVanna(config={"api_key": OPENAI_API_KEY, "temperature": 0.0})

# connect to your local database
vn.connect_to_postgres(**get_db_params())

# # The information schema query may need some tweaking depending on your database.
# # This is a good starting point.
# df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

# # This will break up the information schema into bite-sized chunks that can be
# # referenced by the LLM
# plan = vn.get_training_plan_generic(df_information_schema)
# print(plan)

# If you like the plan, then uncomment this and run it to train
# print("Training....")
# vn.train(plan=plan)

# ask my question
sql, df, fig = vn.ask(
    question="What are the top 5 jazz artists by sales?", print_results=False
)

print("SQL generated:")
print(sql)
print("\nResults (first 20 rows):")
print(df.head(20))

# display all tables in the database
# tables = pd.read_sql(
#     """
#     SELECT *
#     FROM INFORMATION_SCHEMA.TABLES
#     WHERE TABLE_TYPE = 'BASE TABLE'
#     AND TABLE_SCHEMA = 'public'
#     """,
#     engine,
# )

# print(tables.head(20))

# artists = pd.read_sql("SELECT * FROM artist", engine)
# print(artists.head(20))

# train the model on your database schema


# # vn = VannaDefault(model="chinook", api_key=vanna.get_api_key("mjbhobe@gmail.com"))
# vn = VannaDefault(model="chinook", api_key=os.getenv("VANNA_API_KEY"))
# vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
# vn.ask("What are the top 10 albums by sales?")
