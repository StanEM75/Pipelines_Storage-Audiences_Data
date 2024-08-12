def transfer_csv_to_db(csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    # Table name : remove.csv
    table_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    
    # Store in SQL Table
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data from {csv_file_path} has been transferred to the table {table_name}.")

