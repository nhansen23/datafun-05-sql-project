'''
Module 5: Python and SQL Project

This project uses Python and SQL to analyze historical
Olympic athlete data

'''

# Standard library imports
import sqlite3
import pathlib
import logging


# External library imports
import pandas as pd
import pyarrow

db_file = pathlib.Path("olympics.db")

def insert_data_from_csv():
    '''Function to insert athlete tables from CSV'''
    try:
        athlete_data_push = pathlib.Path("athletes","athlete_events.csv")
        athletes_df = pd.read_csv(athlete_data_push)
        with sqlite3.connect(db_file) as conn:
            athletes_df.to_sql("athletes", conn, if_exists="replace", index=False)
            logging.info("Athlete data inserted successfully.")
    except(sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.info("Error inserting data:", e)



def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


def main():
    # Set database
    db_filepath = 'olympics.db'

    # Configure logging to write to a file and append new logs to existing file
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Program started")

  
    # Create database schema
    execute_sql_from_file(db_filepath, 'create_tables.sql')

    # Populate data: athletes from CSV and countries from sql
    insert_data_from_csv()
    execute_sql_from_file(db_filepath, 'insert_records.sql')

    # Execute rest of sql queries
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")

    logging.info("Program ended")

# logger.exception([message])

if __name__ == "__main__":
    main()