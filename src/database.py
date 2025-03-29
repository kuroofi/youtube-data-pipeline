import sqlite3
import os


def folder():
    """
    Creates a file path to the sqlite file. 
    """
    os.makedirs("output_data", exist_ok=True) 
    db_file_path = os.path.join("output_data", "youtube_data.db")
    return db_file_path


def create_tables(db_file_path):
    """
    Creates new tables for channel and video data. 

    param db_file_path: (str) String representation of the file path to the SQL file.
    """
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Create channel data table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ChannelData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT,
        channel_title TEXT,
        subscribers INTEGER,
        Total_views INTEGER
    )
    """)

    # Create video data table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VideoData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT,
        video_id TEXT,
        video_title TEXT,
        publish_date INTEGER,
        duration REAL,
        views INTEGER,
        likes INTEGER,
        comments INTEGER  
    )
    """)

    conn.commit()
    conn.close()


def store_channeldata(db_file_path, channel_id, channel):
    """
    Inserts channel data into table.

    param db_file_path: (str) String representation of the file path to the SQL file.
    param channel_id: (str) ID of the specific channel.
    param channel: (dict) Dictionary containing channel data.
    """
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Inserts channel data from dict to SQL table
    cursor.execute("""
    INSERT INTO ChannelData (channel_id, channel_title, subscribers, Total_views)
    VALUES (?, ?, ?, ?)
    """, (
        channel_id,
        channel["channel_title"], 
        channel["subscribers"], 
        channel["Total_views"]
        )
    )

    conn.commit()
    conn.close()


def store_videodata(db_file_path, channel_id, videos):
    """
    Inserts video data into table.
    
    param db_file_path: (str) String representation of the file path to the SQL file.
    param channel_id: (str) Channel ID. 
    param channel: (dict) Dictionary containing channel data.
    """
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Inserts each video's data as a row in the SQL table
    for video in videos:
        cursor.execute("""
        INSERT INTO VideoData (channel_id, video_id, video_title, publish_date, duration, views, likes, comments)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            channel_id,
            video["video_id"],
            video["video_title"],
            video["publish_date"],
            video["video_duration"],
            video["view_count"],
            video["like_count"],
            video["comment_count"]
            )
        )

    conn.commit()
    conn.close()
