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
OPENAI_MODEL = "gpt-4o"


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

# The information schema query may need some tweaking depending on your database.
# This is a good starting point.
df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

# This will break up the information schema into bite-sized chunks that can be
# referenced by the LLM
plan = vn.get_training_plan_generic(df_information_schema)
print(plan)

# If you like the plan, then uncomment this and run it to train
# print("Training....")
vn.train(plan=plan)

# -------------------------------------------------------------------

st.set_page_config(
    page_title="Chat with local database",
    page_icon="✨",
)

st.title("Chat with PostgreSQL database 💬")

question = st.text_input(
    "Ask me a question that I can turn into SQL & run:",
    key="my_question",
)

# ask my question
if question:
    sql, df, fig = vn.ask(
        question="What are the top 5 jazz artists by sales?",
        print_results=False,
        allow_llm_to_see_data=True,
    )

    # sql = vn.generate_sql(question=question)

    # display SQL as code block
    st.code(sql, language="sql")

    # display results in a grid
    # df = vn.run_sql(sql)
    st.dataframe(df, use_container_width=True)

    # display a plot
    # fig = vn.get_plotly_figure(
    #     plotly_code=vn.generate_plotly_code(question=question, sql=sql, df=df), df=df
    # )
    # st.plotly_chart(fig, use_container_width=True)
