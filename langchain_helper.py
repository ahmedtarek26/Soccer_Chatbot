from langchain_openai import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from snowflake.sqlalchemy import URL
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)


def db_chain():

    db_url = URL(
        user=os.environ["user"],
        password= os.environ["password"],
        warehouse="COMPUTE_WH",
        database="STATSBOMB",
        schema='PUBLIC',
        role='ACCOUNTADMIN',
    )


    # Create a SQLDatabase object from the DB url
    db = SQLDatabase.from_uri(db_url) 
    llm = OpenAI(google_api_key=os.environ['OPENAI_API_KEY'], temperature=0.7)
    
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    return chain