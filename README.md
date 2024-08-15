# Audiences Data - Data Ingestion, Pre-Processing & Storage in a Database

![Project Image](https://image.cnbcfm.com/api/v1/image/103478083-GettyImages-82457591.jpg?v=1663251593)

## 🚀 Introduction

The objective of this project is to consolidate multiple data sources, both structured and semi-structured, to transform and harmonize them. Once the data is made usable, it will be transferred to a PostgreSQL database hosted on AWS.

## 🛠️ Technos Used

- **Python**
- **Pandas**
- **AWS**
- **json**
- **PostgreSQL**

## 🔑 Project Workflow

1. **Gather all datasources in one folder**
- The files are in JSON, Excel, or CSV format, all gathered in the same folder : /Pipelines/data

2. **Process the Data**
- Open the files.
- Process if needed. Main transformation includes data format, data splitting, removing columns.
- Check the consistency of the output dataframes.

3. **Export Data**
- Export all the dataframes to CSV.
- Store these CSV in the folder /Pipelines/Outputs.

4. **Transform CSV into tables and store in the SQL Database**
- File connect_db.py
- Connect to the database.
- Based on the CSV's names, give a name to the tables.
- Transfer the CSV to the table.
