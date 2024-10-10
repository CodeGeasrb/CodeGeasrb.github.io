from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import emoji
import re


# Function to retrieve metadata of an specific youtube video
def get_video_data(video_id, youtube):
    """
    Retrieves metadata for a specific YouTube video.

    Args:
        video_id: The ID of the YouTube video.
        youtube: An instance of the YouTube API client.

    Returns:
        A pandas DataFrame containing the video metadata 
        (title, channel title, publish date, view count, like count),
        or None if no video is found.
    """

    request = youtube.videos().list(
        part='snippet,statistics,contentDetails',
        id=video_id
    )
    response = request.execute()
    # video data response
    video_data = response['items'][0]
    # Extract relevant data
    video_info = {
        'video_id': video_data['id'],
        'title': video_data['snippet']['title'],
        'channel_title': video_data['snippet']['channelTitle'],
        'published_at': video_data['snippet']['publishedAt'],
        'view_count': int(video_data['statistics']['viewCount']),
        'like_count': int(video_data['statistics']['likeCount']),
    } 
    return video_info


# Function to retrieve comments of a youtube video
def get_comments_data(video_id, youtube):
    """
    Retrieves comments for a specific YouTube video, handling pagination.

    Args:
        video_id: The ID of the YouTube video.
        youtube: An instance of the YouTube API client.

    Returns:
        A pandas DataFrame containing the comments data 
        (user name, comment text, number of likes, last update timestamp).
    """

    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token
  # use next_page_token for pagination
        )
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({ 
                'video_id': response['items'][0]['snippet']['videoId'],
                'user_name': comment['authorDisplayName'],
                'comment': comment['textDisplay'],
                'n_likes': comment['likeCount'],
                'updated_at': comment['updatedAt']
            })
            
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    return comments


# Function to scrape youtube videos data and comments data using YouTube Data 3.0 API
def collect_youtube_video_data(videos_ids, youtube):
    # arrays to save data
    videos_data = []
    comments_data = []
    # collect video data
    for id in videos_ids:
        # retrive data
        video_data = get_video_data(video_id=id, youtube=youtube)
        comments = get_comments_data(video_id=id, youtube=youtube)
        # save data
        videos_data.append(video_data)
        comments_data.extend(comments) 
    # save data in dataframes
    videos_data = pd.DataFrame(videos_data)
    comments_data = pd.DataFrame(comments_data)
    return videos_data, comments_data


# Function to apply a  basic cleanning process in comments text
def basic_text_cleaning(text):
    # convert text to lowercase
    text = text.lower()
    # remove urls
    text = re.sub(r'http\S+|www.\S+', '', text)  
    # remove mentions
    text = re.sub(r'@\w+', '', text)
    # remove Hashtags  
    text = re.sub(r'#\w+', '', text)
    # normalize blank space use
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# Function to apply specific cleanning process in text for common words analysis
def common_words_cleanning(text, stopwords):
    # basic cleanning
    text = basic_text_cleaning(text)
    # remove emojis, symbols and pictograms
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"  
                           u"\U0001F680-\U0001F6FF"  
                           u"\U0001F700-\U0001F77F"  
                           u"\U0001F780-\U0001F7FF"
                           u"\U0001F800-\U0001F8FF"
                           u"\U0001F900-\U0001F9FF"
                           u"\U0001FA00-\U0001FA6F"
                           u"\U0001FA70-\U0001FAFF"
                           u"\U00002702-\U000027B0"  
                           u"\U000024C2-\U0001F251" 
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    # remove special characters
    text = re.sub(r'[^a-z0-9áéíóúÁÉÍÓÚñÑ ]', '', text)
    # divide text into words
    words = text.split()
    # remove stopwords
    words = [word for word in words if word not in stopwords]
    return ' '.join(words)


# Function to apply specific cleanning process in text for sentiment analysis
def sentiment_analysis_cleanning(text):
    # basic cleanning
    text = basic_text_cleaning(text)
    # convert emojis into text
    text = emoji.demojize(text)
    # remove special characters, except relevants for sentiment analysis
    text = re.sub(r'[^a-zA-Z0-9\s¡!¿?.,;]', '', text)
    # Dvide text and remove stopwords
    return text

"""
# Function to get more frequent words
def get_most_common_words(comments, stopwords, n=50):
    all_words = []
    for comment in comments:
        clean_comment = remove_stopwords(comment, stopwords)
        all_words.extend(clean_comment.split())
    
    word_count = Counter(all_words)
    return dict(word_count.most_common(n))
"""

# Function to generate a word cloud
def generate_wordcloud(words_dict, title):
    wordcloud = WordCloud(width=1000, height=600, background_color='white').generate_from_frequencies(words_dict)
    plt.figure(figsize=(9, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontdict={"fontsize":12.5, "weight":"bold"})
    plt.show()


































