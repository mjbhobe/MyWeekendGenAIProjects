"""
dbutils.py - database utilities for the text-2-sql demo

Author: Manish Bhobe
My experiments with Python, ML, and Generative AI.
Code is provided as-is and meant for learning purposes only!
"""

import configparser
import pathlib
import urllib.parse
import pandas as pd
from typing import Dict

config_path = pathlib.Path(__file__).parent / "db_conn.ini"

assert (
    config_path.exists()
), f"FATAL ERROR: unable to find config file for database connection"


def get_db_uri() -> str:
    """returns database connection string after reading settings from config file
    return string is of the following format
        "postgres+psycopg2://user_name:password@host:port/db_name"
    where values of user_name, password, host, port, and db_name are read from the config file
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    SECTION: str = "Postgres"

    db_name = config.get(SECTION, "db_name")
    user_name = config.get(SECTION, "user_name")
    password = config.get(SECTION, "password")
    # password may contain special chars, encode them
    encoded_pwd = urllib.parse.quote_plus(password)
    host = config.get(SECTION, "host")
    port = config.get(SECTION, "port")

    return f"postgresql+psycopg2://{user_name}:{encoded_pwd}@{host}:{port}/{db_name}"


def get_db_params() -> Dict[str, str]:
    config = configparser.ConfigParser()
    config.read(config_path)
    SECTION: str = "Postgres"

    db_params = {
        "host": config.get(SECTION, "host"),
        "dbname": config.get(SECTION, "db_name"),
        "user": config.get(SECTION, "user_name"),
        "password": config.get(SECTION, "password"),
        "port": config.get(SECTION, "port"),
    }

    return db_params


def dataframe_from_query(sql: str, engine) -> pd.DataFrame:
    """returns a pandas dataframe from the result of the sql query"""
    return pd.read_sql(sql, engine)
