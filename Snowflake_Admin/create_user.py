import snowflake.connector
import logging
import os
import sys
import re
import random
import string
from sql_scripts import *
from snow_utils import *
logging.basicConfig(level=logging.WARNING,filename='logs/connections.log', format='%(asctime)s - %(message)s')

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def load_local_config(filename):
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split("=")
            os.environ[key] = value

def connect_w_snowflake()
    try:
        conn = snowflake.connector.connect(
            user = os.environ.get("SNOWFLAKE_USER")
            , password = os.environ.get("SNOWFLAKE_PASSWORD")
            , account = os.environ.get("SNOWFLAKE_ACCOUNT")
            , database = "DEMO_DB"
            , warehouse = "DEMO_WH"
            , role = "ACCOUNTADMIN"
        )
        logging.debug(f"Snowflake connection for user {os.environ.get('SNOWFLAKE_USER')}")
        return conn
    except RuntimeError:
        logging.error("Snowflake connection string failed")
        sys.exit(1)

def create_user():
    conn = connect_w_snowflake()
    user_type = int(input("Type in 1 for Personal User, 2 for Service User: "))

    if user_type == 1: # personal
        loop = 1
        while loop == 1:
            email = input("What is the email of the person: ")
            email_validation_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\[a-zA-Z]{2,}$'
            if re.match(email_validation_pattern, email):
                # Extract portion before the "@" symbol
                basename = email.split("@")[0]
                loop = 0
            else:
                print("Invalid email. Try again")
        
        script = PERSONAL_USER_SCRIPT.format(basename=basename,
                                             email=email,
                                             )
        
    if user_type == 2: #service user
        password = generate_password()
        username = input("Choose a username: ")
        script = SERVICE_USER_SCRIPT.format(username=username,
                                            password=password)
        
        print(f"Creating user: {username}. Password: {password}")
    print(script)
    execute_snowflake_script(conn=conn, script=script)

load_local_config(".env")
create_user()
