import os, sys
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

import vanna as vn
from dbutils import get_db_uri, get_db_params

# load all API keys
load_dotenv()

# read API key from local .env file
# vn.set_api_key(os.getenv("VANNA_API_KEY"))
# vn.set_model("chinook-mjb")
# connect to model
vn.connect_to_postgres(**get_db_params())

sys.exit(-1)

db_uri = get_db_uri()
print(db_uri)
engine = create_engine(db_uri)

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
