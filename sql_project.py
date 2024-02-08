'''
Module 5: Python and SQL Project

This project uses Python and SQL to analyze historical
Olympic athlete data

'''

# Standard library imports
import sqlite3
import pathlib
import logging
import os


# External library imports
import pandas as pd
import pyarrow

db_file = pathlib.Path("olympics.db")

def insert_data_from_csv():
    '''Function to insert athlete tables from CSV'''
    try:
        athlete_data_push = pathlib.Path("data","athlete_events.csv")
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
    execute_sql_from_file(db_filepath, 'sql/create_tables.sql')
    logging.info("Tables created successfully.")
    #logging.exception("Tables were not created.")

    # Populate data: athletes from CSV due to large number of records
    insert_data_from_csv()

    # Populate data: countries from insert_records sql query
    execute_sql_from_file(db_filepath, 'sql/insert_records.sql')
    logging.info("Country data inserted successfully.")
    #logging.exception("Error loading country data.")
    
    # Execute rest of sql queries
    execute_sql_from_file(db_filepath, 'sql/update_records.sql')
    execute_sql_from_file(db_filepath, 'sql/delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql/query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql/query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql/query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql/query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql/query_join.sql')
    
    logging.info("All SQL operations completed successfully")

    logging.info("Program ended")

# logger.exception([message])

if __name__ == "__main__":
    main()