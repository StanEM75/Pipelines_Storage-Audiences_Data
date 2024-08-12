import pandas as pd
from sqlalchemy import create_engine
import os
import glob

# Logs
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Create an URL to connect
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create SQL Engine
engine = create_engine(db_url)

def transfer_csv_to_db(csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    # Table name : remove .csv
    table_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    
    # Store in SQL Database
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data from {csv_file_path} has been transferred to the table {table_name}.")

# Go to CSV files
csv_directory = '/System/Volumes/Data/Applications/Project_Pipelines/Pipelines/Outputs'
csv_files = glob.glob(csv_directory + '*.csv')

# From csv, transfer to the table
for csv_file in csv_files:
    transfer_csv_to_db(csv_file)

