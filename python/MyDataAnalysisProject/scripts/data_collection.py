from googleapiclient.discovery import build
import sys
import os

sys.path.append('../data_analysis_project')

from utils.fuctions import collect_youtube_video_data

# Define a YT API Key
youtube_api_key = "AIzaSyAfoJ94EZmxu-GdSrDfuH9lQoZigkGd7aY"

# Build the YouTube API client
youtube = build("youtube", "v3", developerKey=youtube_api_key)

# Youtube videos IDs (pre-selected) 
videos_ids = ["kZaucITWv00", "0osEeTQLk3Q", "DEbALmrsZs8"]

# Collect data
videos_data, comments_data = collect_youtube_video_data(videos_ids=videos_ids, youtube=youtube)

# Define project directory
current_dir = os.getcwd()

# Define a path to save data
data_dir = os.path.join(current_dir, "data", "raw_data") 

# Define data paths
videos_data_path = os.path.join(data_dir, "videosData.txt")
comments_data_path =os.path.join(data_dir, "commentsData.txt")

# save data in a csv format
videos_data.to_csv(path_or_buf=videos_data_path, index=False)
comments_data.to_csv(path_or_buf=comments_data_path, index=False)






