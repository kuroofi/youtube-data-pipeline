import os
from dotenv import load_dotenv
from src.youtube_api import get_key, get_channel_data, get_video_data
from src.database import create_tables, store_channeldata, store_videodata, folder
from src.export_csv import export_channel_csv, export_video_csv


def main():
    #Get channel ID and API key.
    load_dotenv()
    channel_id = os.getenv("channel_id")
    api_key = os.getenv("api_key")

    #Get youtube client object.
    youtube = get_key(api_key)

    #Get channel and video data data in dictionary form.
    channel = get_channel_data(channel_id, youtube)
    videos = get_video_data(channel_id, youtube)

    #Creates file path to output files.
    file_path = folder()

    #Creates and stores channel and video data into respective SQL tables. 
    create_tables(file_path)
    store_channeldata(file_path, channel_id, channel)
    store_videodata(file_path, channel_id, videos)

    #Exports SQL tables into CSV files.
    export_channel_csv(file_path)
    export_video_csv(file_path)

    print("YouTube data pipeline executed successfully!")


if __name__ == "__main__":
    main()
