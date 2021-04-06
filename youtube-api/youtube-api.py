from googleapiclient.discovery import build

api_key = "AIzaSyCMpQbH0agQ-d6qYgxFCkUBtkPxVR58YtY"
youtube_service = build('youtube','v3', developerKey=api_key)

request = youtube_service.channels().list(
    part='statistics',
    forUsername= 'sentdex'
)
response = request.execute()
print(response)