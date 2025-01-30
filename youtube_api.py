from googleapiclient.discovery import build

def get_key(api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    return youtube


def get_channel_data(channel_id, youtube):
    request_channel = youtube.channels().list(
        part="snippet,statistics", 
        id=channel_id,
    )

    response_channel = request_channel.execute()
    channel_data = response_channel["items"][0]
    channel_title = channel_data["snippet"]["title"]
    subscribers = int(channel_data["statistics"]["subscriberCount"])
    total_views = int(channel_data["statistics"]["viewCount"])
    print(f"Channel: {channel_title}, Subscribers: {subscribers}, Views: {total_views}")
    return {"channel_title": channel_title, "subscribers": subscribers, "Total_views": total_views}


def get_video_data(channel_id, youtube):
    request_video = youtube.search().list(
    part="snippet",
        channelId=channel_id,
        maxResults=200,
        order="date"
    )
    response_video = request_video.execute()
    print("\nVideos:")
    lst = []
    for item in response_video["items"]:
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]

        video_request = youtube.videos().list(
            part="statistics,contentDetails",
            id=video_id
        )

        video_response = video_request.execute()
        video_data = video_response["items"][0]["statistics"]
        video_views = video_data["viewCount"]
        video_duration = video_response['items'][0]['contentDetails']['duration']

        print(f"Title:{video_title}, Views: {video_views}, Duration: {video_duration}")
        lst.append({"video_id": video_id, "video_title": video_title, "video_views": video_views})
    return lst 
