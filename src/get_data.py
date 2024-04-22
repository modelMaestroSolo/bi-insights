import pyodbc
from dotenv import (
    dotenv_values,
)  # import the dotenv_values function from the dotenv package
import pandas as pd

# Load environment variables from .env file into a dictionary
environment_variables = dotenv_values(".env")

# Get the values for the credentials you set in the '.env' file
server = environment_variables.get("SERVER")
database = environment_variables.get("DATABASE")
username = environment_variables.get("USERNAME")
password = environment_variables.get("PASSWORD")

# Create a connection string
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;"

# Use the connect method of the pyodbc library and pass in the connection string.
# This will connect to the server and might take a few seconds to be complete.
# Check your internet connection if it takes more time than necessary

connection = pyodbc.connect(connection_string)

# Now the sql query to get the data is what what you see below.
# Note that you will not have permissions to insert delete or update this database table.

query = "SELECT * FROM Sales_July_2019.csv"

data = pd.read_sql(query, connection)
