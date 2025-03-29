import sqlite3
import csv
import os 


def export_channel_csv(db_file_path):
    """
    Exports channel SQL table into CSV file. 

    param db_file_path: (str) String representation of the file path to the SQL file.
    """
    # Connects a filepath for the CSV file to go to
    csv_file_path = os.path.join("output_data", "ChannelData.csv")

    # Fetches all video data from the SQL table
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ChannelData")
    channel_data = cursor.fetchall()

    # Writes channel data from SQL table into the CSV file
    with open(csv_file_path, "w", newline="", encoding="utf-8") as channel_file:
        writer = csv.writer(channel_file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(channel_data)


def export_video_csv(db_file_path):
    """
    Exports video SQL table into CSV file.

    param db_file_path: (str) String representation of the file path to the SQL file.
    """
    # Connects a filepath for the CSV file to go to 
    csv_file_path = os.path.join("output_data", "VideoData.csv")

    # Fetches all video data from the SQL table
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VideoData")
    video_data = cursor.fetchall()

    # Writes video data into the CSV file
    with open(csv_file_path, "w", newline="", encoding="utf-8") as video_file:
        writer = csv.writer(video_file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(video_data)



