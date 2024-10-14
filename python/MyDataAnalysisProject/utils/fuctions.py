from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import sqlite3
import emoji
import os
import re


# Dictionary of common emojis translations to spanish
"""
emoji_translations = {
    ':grinning_face:': 'cara sonriendo',
    ':smiling_face_with_smiling_eyes:': 'cara sonriente con ojos sonrientes',
    ':face_with_tears_of_joy:': 'cara con lágrimas de alegría',
    ':rolling_on_the_floor_laughing:': 'rodando por el suelo riendo',
    ':smiling_face_with_heart_eyes:': 'cara sonriente con ojos de corazón',
    ':winking_face:': 'cara guiñando un ojo',
    ':face_savoring_food:': 'cara saboreando comida',
    ':thumbs_up:': 'pulgar hacia arriba',
    ':clapping_hands:': 'manos aplaudiendo',
    ':raising_hands:': 'manos levantadas',
    ':heart:': 'corazón',
    ':broken_heart:': 'corazón roto',
    ':crying_face:': 'cara llorando',
    ':angry_face:': 'cara enojada',
    ':thinking_face:': 'cara pensativa',
    ':shushing_face:': 'cara pidiendo silencio',
    ':nauseated_face:': 'cara con náuseas',
    ':sleeping_face:': 'cara durmiendo',
    ':star_struck:': 'cara con ojos de estrella',
    ':party_popper:': 'confeti',
    ':sparkles:': 'brillantes',
    ':fire:': 'fuego',
    ':hundred_points:': 'cien puntos',
    ':peace_symbol:': 'símbolo de paz',
    ':victory_hand:': 'mano de victoria',
    ':pensive_face:': 'cara pensativa',
    ':face_with_monocle:': 'cara con monóculo',
}
"""


# Dictionary of common intentional orthography mexican errors
orthography_corrections = {
    # common abbreviations
    "esc": "escuela",
    "q": "que",
    "xq": "porque",
    "xk": "porque",
    "tmb": "también",
    "tb": "también",
    "pa": "para",
    "k": "que",
    "ke": "que",
    "x": "por",
    "xa": "para",
    "xfa": "por favor",
    "pq": "porque",
    "tqm": "te quiero mucho",
    "bno": "bueno",
    "dnd": "dónde",
    "cmo": "cómo",
    "cm": "cómo",
    "xfin": "por fin",
    "ntp": "no te preocupes",
    "vrdd": "verdad",
    "vdd": "verdad",
    "grx": "gracias",
    "grcs": "gracias",
    "kmo": "como",
    "msj": "mensaje",
    "x eso": "por eso",
    "bss": "besos",
    "bye": "adiós",
    # phonetic errors or colloquial adaptations
    "ta": "está",
    "toy": "estoy",
    "pa'": "para",
    "na'": "nada",
    "toa": "toda",
    "asi": "así",
    "io": "yo",
    "d": "de",
    "i": "y",
    "ora": "ahora",
    "pos": "pues",
    "oie": "oye",
    "creo k": "creo que",
    "aki": "aquí",
    "alli": "allí",
    "deveras": "de veras",
    "ke onda": "qué onda",
}


# Define spanish stop words
stop_words = [
    'a', 'al', 'algo', 'alguien', 'algún', 'alguna', 'algunas', 'algunos', 'ambos', 'ante', 'antes', 'aki', 'abajo', 
    'bien', 'como', 'comó', 'con', 'cmo', 'cual', 'cuando', 'cuándo', 'donde', 'dónde', 'durante', 'el', 'él', 'ella', 
    'ellas', 'ellos', 'en', 'entre', 'era', 'eras', 'éramos', 'eran', 'es', 'esa', 'esas', 'ese', 'esos', 'esta', 
    'estaba', 'estabas', 'estaban', 'estamos', 'estar', 'este', 'esto', 'estos', 'estoi', 'toy', 'fue', 'fui', 
    'fuese', 'fuesen', 'fueron', 'siendo', 'sino', 'son', 'soy', 'tal', 'tambn', 'tambien', 'también', 'tan', 'tanta', 
    'tantas', 'tanto', 'tantos', 'te', 'ti', 'tienes', 'tiene', 'tienen', 'tu', 'tú', 'tus', 'un', 'uno', 'unos', 
    'una', 'unas', 'veses', 'veces', 'y', 'ya', 'io', 'yo', 'mi', 'mí', 'mios', 'míos', 'tuyo', 'tuyos', 'suyo', 
    'suyos', 'mio', 'nos', 'nosotros', 'vosotros', 'su', 'sí', 'si', 'les', 'los', 'nuestras', 'nuestras', 'nuestros', 
    'otros', 'otra', 'otras', 'o', 'os', 'se', 'sé', 'asi', 'así', 'alli', 'allá', 'aka', 'aquí', 'ora', 'ahora', 
    'apenas', 'ante', 'aun', 'aún', 'además', 'aunque', 'como', 'cómo', 'contra', 'cual', 'cuales', 'cuando', 
    'cuándo', 'desde', 'de', 'despues', 'después', 'dice', 'dijo', 'dixo', 'dicho', 'donde', 'dónde', 'dos', 'durante', 
    'e', 'él', 'ella', 'ellas', 'ellos', 'en', 'entre', 'era', 'eras', 'eran', 'es', 'esa', 'esas', 'ese', 'eso', 
    'esos', 'esta', 'estan', 'están', 'estar', 'este', 'esto', 'estos', 'toy', 'toi', 'fue', 'fui', 'fueron', 
    'fueron', 'fuesen', 'fui', 'hago', 'izo', 'hizo', 'hemos', 'asta', 'hasta', 'hay', 'iba', 'iban', 'iwal', 'igual', 
    'incluso', 'ir', 'está', 'estabamos', 'estamos', 'estan', 'iban', 'igual', 'incluso', 'ir', 'acia', 'hacia', 'ha', 
    'había', 'había', 'asta', 'hice', 'izo', 'hizo', 'la', 'las', 'lo', 'los', 'más', 'mas', 'menos', 'me', 'mí', 
    'misma', 'mismas', 'mismo', 'mismos', 'muy', 'mucho', 'muxo', 'muchos', 'nada', 'ni', 'no', 'nos', 'nosotros', 
    'o', 'otra', 'otras', 'otros', 'para', 'pero', 'poco', 'por', 'porq', 'porque', 'porqué', 'cual', 'cuál', 
    'cuales', 'cuáles', 'cuando', 'cuándo', 'que', 'qué', 'se', 'sin', 'sobre', 'soy', 'sólo', 'solo', 'su', 'sus', 
    'también', 'tambn', 'tan', 'tanta', 'tantas', 'tanto', 'tantos', 'tiene', 'tu', 'tuya', 'tuyas', 'tuyo', 'tuyos', 
    'un', 'una', 'unas', 'uno', 'unos', 'ya'
]


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


# Function to save data into a sqlite db
def save_to_db(dataframe, db_dir, db_name, table_name):
    # create path where db will be save
    db_path = os.path.join(db_dir, db_name)
    # connect to db
    conn = sqlite3.connect(db_path)
    # save dataframe in a table into the db
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
    # close connection
    conn.close()


# Function to make sql query in a db en retrive result in a dataframe
def make_sql_query(db_dir, db_name, query):
    # create path where db will be save
    db_path = os.path.join(db_dir, db_name)
    # connect to db
    conn = sqlite3.connect(db_path)
    # save query result in a df
    dataframe = pd.read_sql(query, conn)
    # close connection
    conn.close()
    return dataframe


# Function to correct datetime format
def correct_datetime(datetime):
    # correct datetime to a more suitable format
    datetime = pd.to_datetime(datetime)
    return datetime


# Function to remove special characters in text
def remove_special_characters(text):
    # text in lower case
    text = text.lower()
    # remove HTML tags and attributes
    text = re.sub(r'<[^>]+>', '', text) 
    # remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove full URLs
    # remove mentions "@" but keep the username
    text = re.sub(r'@\w+', '', text)
    # remove hashtags but keep the word
    text = re.sub(r'(?<=#)\w+', '', text)
    # remove punctuation at the end of words (except for ? and !)
    text = re.sub(r'(\b\w+)[.,;:]+', r'\1', text)  
    # keep only letters, digits, spaces, and the specified punctuation
    text = re.sub(r'[^a-zA-Z\s¡!¿?]', '', text)  # Remove other unwanted characters
    # normalize blank spaces
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize multiple spaces to a single space
    return text


# Function to correct mexican-spanish orthography
def correct_ortography(text):
    # split text into single words
    words = text.split()
    # return the corrected word if it is in corrections dictionary
    return ' '.join(orthography_corrections.get(word, word) for word in words)


# Function to remove spanish stop words
def remove_stop_words(text):
    # split text into single words
    words = text.split()
    # return text without stop words
    return ' '.join(word for word in words if word not in stop_words)


# Function to preprocess text
def preprocess_text(text):
    # remove special characters
    text = remove_special_characters(text=text)
    # correct intentional ortography errors
    text = correct_ortography(text=text)
    # remove stop words
    text = remove_stop_words(text=text)
    # lemmatize text
    
    return text


# Function to split emoji names in the text
def split_emoji_text(text):
    # use a regular expression to find the names of emojis and add spaces
    emoji_pattern = re.compile(r':[a-zA-Z0-9_]+:')
    # find a match with emoji pattern
    emojis_found = emoji_pattern.findall(text)
    # add blank space between emojis translations
    for emoji_name in emojis_found:
        text = text.replace(emoji_name, emoji_name + ' ') 
    return text.strip()     # remove blank space remaining




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


































