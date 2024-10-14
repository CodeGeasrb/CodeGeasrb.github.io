# Import required tools
import pandas as pd
import sys
import os


# Add project directory to the path
sys.path.append('../data_analysis_project')

# Import required functions
from utils.fuctions import preprocess_text, correct_datetime, save_to_db, make_sql_query

# Define db directory, where db is stored
db_dir = os.path.join(os.getcwd(), "data")

# Define a sql query
query = """
        SELECT *
        FROM comments
        """

# Retrieve raw data from db
comments = make_sql_query(db_dir=db_dir, db_name="youtube_data_analysis.db", query=query)

# Clean comments for common words analysis
comments_preprocessed = comments.copy()[['comment_id']]    # make a copy from original data
comments_preprocessed['comment_preprocessed'] = comments['comment'].apply(preprocess_text)   
comments_preprocessed['updated_at_corrected'] =  comments['updated_at'].apply(correct_datetime)

# Load preprocessed data into a db
save_to_db(dataframe=comments_preprocessed, db_dir=db_dir, db_name="youtube_data_analysis.db", table_name="comments_preprocessed")








