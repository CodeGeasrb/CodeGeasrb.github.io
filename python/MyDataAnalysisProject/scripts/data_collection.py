# Import required tools
from googleapiclient.discovery import build
import uuid
import sys
import os


# Add project directory to the path
sys.path.append('../data_analysis_project')

# Import required functions
from utils.fuctions import collect_youtube_video_data, save_to_db

# Define a YT API Key
youtube_api_key = "AIzaSyAfoJ94EZmxu-GdSrDfuH9lQoZigkGd7aY"

# Build the YouTube API client
youtube = build("youtube", "v3", developerKey=youtube_api_key)

# Youtube videos IDs (pre-selected) 
videos_ids = ["kZaucITWv00", "0osEeTQLk3Q", "DEbALmrsZs8"]

# Collect data
videos_data, comments_data = collect_youtube_video_data(videos_ids=videos_ids, youtube=youtube)

# Create a new column with 4 digits-unique IDs for comments
comments_data['comment_id'] = [str(uuid.uuid4()) for _ in range(comments_data.shape[0])]

# Get project directory
project_dir = os.getcwd()

# Get/Create a data directory (all data will be saved here)
data_dir = os.path.join(project_dir, "data")
os.makedirs(data_dir, exist_ok=True) # check if directory exists, if not, create it

# Load data into a DataBase
save_to_db(dataframe=videos_data, db_dir=data_dir, db_name="youtube_data_analysis.db", table_name="videos")
save_to_db(dataframe=comments_data, db_dir=data_dir, db_name="youtube_data_analysis.db", table_name="comments")






