import pandas as pd

# Load the CSV file
india_ehr_database = pd.read_csv('./src/ehr_database/ehr_data.csv')

# Assign to dictionary
india_attrs = {
    "india_ehr_database": india_ehr_database
}
