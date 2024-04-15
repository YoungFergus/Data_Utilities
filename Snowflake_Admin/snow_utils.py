import snowflake.connector
import logging
import sys

def execute_snowflake_script(conn, script):
    try:
        cur = conn.cursor()
        cur.execute(script)
        conn.get_query_status_throw_if_error(cur.sfqid)
        return print("Query ran successfully")
    except RuntimeError:
        logging.critical("Query failed to run")
        sys.exit(1)

    