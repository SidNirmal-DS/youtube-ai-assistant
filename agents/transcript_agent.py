import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable

class TranscriptAgent:
    def __init__(self, url: str):
        self.url = url
        self.video_id = self.extract_video_id()

    def extract_video_id(self):
        # Extract the video ID from a standard YouTube URL
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", self.url)
        if not match:
            raise ValueError("Invalid YouTube URL")
        return match.group(1)

    def transcribe(self):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
            return " ".join([item['text'] for item in transcript])

        except TranscriptsDisabled:
            return "Transcript is disabled for this video."

        except VideoUnavailable:
            return "This video is not available."

        except Exception as e:
            return f"Error retrieving transcript: {str(e)}"