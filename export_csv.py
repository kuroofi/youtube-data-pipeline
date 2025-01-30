import sqlite3
import csv
import os 


def export_channel_csv():
    csv_file_path = os.path.join('output_data', 'ChannelData.csv')

    conn = sqlite3.connect("/Users/rafaelpamintuan/Downloads/youtube-data-pipeline/output_data/youtube_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ChannelData")
    channel_data = cursor.fetchall()
    with open(csv_file_path, "w", newline="", encoding="utf-8") as channel_file:
        writer = csv.writer(channel_file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(channel_data)


def export_video_csv():
    csv_file_path = os.path.join('output_data', 'VideoData.csv')

    conn = sqlite3.connect("/Users/rafaelpamintuan/Downloads/youtube-data-pipeline/output_data/youtube_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VideoData")
    video_data = cursor.fetchall()
    with open(csv_file_path, "w", newline="", encoding="utf-8") as video_file:
        writer = csv.writer(video_file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(video_data)



