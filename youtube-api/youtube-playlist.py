from googleapiclient.discovery import build
from datetime import timedelta
import re


api_key = "AIzaSyCMpQbH0agQ-d6qYgxFCkUBtkPxVR58YtY"
youtube_service = build('youtube','v3', developerKey=api_key)

# playlist_request = youtube_service.playlists().list(
#     part='contentDetails, snippet',
#     channelId= 'UCkUq-s6z57uJFUFBvZIVTyg'
# )

playlist_id = 'PLyb_C2HpOQSCsDpbNPSLql4Xqlg6p11e5'
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')
nextPageToken= None
total_seconds = 0

while True:

    playlist_request = youtube_service.playlistItems().list(
        part='contentDetails, snippet',
        playlistId= playlist_id,
        maxResults = 50, 
        pageToken = nextPageToken
    )


    playlist_response = playlist_request.execute()
    video_list = []

    for item in playlist_response['items']:
        print(item, end='\n\n')
        video_list.append(item['contentDetails']['videoId'])

    vid_request = youtube_service.videos().list(
        part = "contentDetails",
        id = ",".join(video_list)
    )

    vid_response_pattern = vid_request.execute()


    for item in vid_response_pattern['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)
        
        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0
        
        video_seconds = timedelta(
            hours = hours,
            minutes = minutes,
            seconds = seconds
        ).total_seconds()

        total_seconds += video_seconds
    
    nextPageToken = playlist_response.get('nextPageToken')
    
    if not nextPageToken:
        break

total_seconds = int(total_seconds)
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f'{hours}:{minutes}:{seconds}')
