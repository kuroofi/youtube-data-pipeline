import sqlite3
import os

def folder():
    folder_path = 'output_data'
    os.makedirs(folder_path, exist_ok=True) 
    db_file_path = os.path.join(folder_path, 'youtube_data.db')
    return db_file_path


def create_tables(db_file_path):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ChannelData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT,
        channel_title TEXT,
        subscribers INTEGER,
        Total_views INTEGER
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VideoData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        video_title TEXT,
        channel_id TEXT,
        views INTEGER       
    )
    """)
    conn.commit()
    conn.close


def store_channeldata(db_file_path, channel_id, channel):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO ChannelData (channel_id, channel_title, subscribers, Total_views)
    VALUES (?, ?, ?, ?)
    """, (channel_id, channel["channel_title"], channel["subscribers"], channel["Total_views"])
    )
    conn.commit()
    conn.close


def store_videodata(db_file_path, videos, channel_id):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    for video in videos:
        cursor.execute("""
        INSERT INTO VideoData (channel_id, video_id, video_title, views)
        VALUES (?, ?, ?, ?)
        """, (channel_id, video["video_id"], video["video_title"], video["video_views"])
        )
    conn.commit()
    conn.close
