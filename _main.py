from dotenv import load_dotenv
import os


from scripts.youtube_api import get_key, get_channel_data, get_video_data
from scripts.database import create_tables, store_channeldata, store_videodata, folder
from scripts.export_csv import export_channel_csv, export_video_csv

def main():
    load_dotenv()

    channel_id = os.getenv("channel_id")
    api_key = os.getenv("api_key")

    youtube = get_key(api_key)

    channel = get_channel_data(channel_id, youtube)
    videos = get_video_data(channel_id, youtube)

    x = folder()
    create_tables(x)

    store_channeldata(x, channel_id, channel)
    store_videodata(x, videos, channel_id)


    export_channel_csv()
    export_video_csv()

if __name__ == "__main__":
    main()
