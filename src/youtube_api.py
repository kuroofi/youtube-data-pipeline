from googleapiclient.discovery import build


def get_key(api_key):
    """
    Fetches API key and returns youtube API client.

    param api_key: (str) API key.
    return: (obj) youtube API client object.
    """
    youtube = build("youtube", "v3", developerKey=api_key)
    
    return youtube


def get_channel_data(channel_id, youtube):
    """
    Fetches channel data from client object.

    param channel_id : (str) channel ID.
    param youtube: (obj) client object.
    return: (list) A list containing channel data.
    """
    # Specifies which channel and what data is wanted
    request_channel = youtube.channels().list(
        part="snippet,statistics", 
        id=channel_id,
    )
    response_channel = request_channel.execute()
    channel_data = response_channel["items"][0]

    # Returns the data in dictionary format
    return {
        "channel_title": channel_data["snippet"]["title"],
        "subscribers": int(channel_data["statistics"]["subscriberCount"]),
        "Total_views": int(channel_data["statistics"]["viewCount"]),
        }


def get_video_data(channel_id, youtube):
    """
    Fetches video data from client object.

    param channel_id: (str) ID for specific channel.
    param youtube: (obj) client object.
    return: (list) A list containing video data for each video.
    """
    # Specifies which channel and what data is wanted
    request_video = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=200,
        order="date"
    )
    response_video = request_video.execute()

    # For every video in the videos object, fetches their data
    videos = []
    for item in response_video["items"]:
        # Specifices which data types from the videos is wanted
        video_request = youtube.videos().list(
            part="statistics,contentDetails",
            id=item["id"]["videoId"],
            maxResults=200
        )
        video_response = video_request.execute()
        video_data = video_response["items"][0]["statistics"]

        # Appends each video's data to the list
        videos.append(
            {
            "video_id": item["id"]["videoId"],
            "video_title": item["snippet"]["title"],
            "publish_date": item["snippet"]["publishedAt"],
            "video_duration": parse_duration(video_response["items"][0]["contentDetails"]["duration"]),
            "view_count": video_data["viewCount"],  
            "like_count": video_data["likeCount"], 
            "comment_count": video_data["commentCount"]
            }
        )

    return videos


def parse_duration(duration_str):
    """
    Parses the ISO 8601 duration string and convert it into total minutes.
    
    :param duration_str: (str) ISO 8601 duration string.
    :return: (int) Total duration in minutes.
    """
    # Remove the "PT" part of the string (start of the duration)
    duration_str = duration_str[2:]
    hours = minutes = seconds = 0

    # Check if the string contains hours (H)
    if 'H' in duration_str:
        hours_part = duration_str.split('H')[0]
        hours = int(hours_part)
        duration_str = duration_str.split('H')[1]  # Remove the part with hours

    # Check if the string contains minutes (M)
    if 'M' in duration_str:
        minutes_part = duration_str.split('M')[0]
        minutes = int(minutes_part)
        duration_str = duration_str.split('M')[1]  # Remove the part with minutes

    # The remaining string will be the seconds (S)
    if 'S' in duration_str:
        seconds_part = duration_str.split('S')[0]
        seconds = int(seconds_part)

    # Convert to total minutes
    total_minutes = (hours * 3600 + minutes * 60 + seconds) / 60
    return total_minutes


