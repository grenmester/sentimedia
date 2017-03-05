import json
import sys
from urllib import *
import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import  urlopen

def get_video_comments(vid):
    final_comments = []
    def load_comments():
        for item in mat["items"]:
            comment = item["snippet"]["topLevelComment"]
            text = comment["snippet"]["textDisplay"]
            final_comments.append(text)


    try:
        video_id = urlparse(str(vid))
        q = parse_qs(video_id.query)
        vidfinal = q["v"][0]

    except:
        print("Invalid YouTube URL")

    parms = {
        'part': 'snippet,replies',
        'videoId': vidfinal,
        'key': 'AIzaSyBsuQEzXjJ81-8ywBftLva-0j19hWNMc1w'
            }

    try:

        matches = openURL('https://www.googleapis.com/youtube/v3/commentThreads', parms)
        i = 0
        mat = json.loads(matches)
        load_comments()

    except KeyboardInterrupt:
        print("User Aborted the Operation")

    except:
        print("Cannot Open URL or Fetch comments at a moment")

    return final_comments

def get_video_id(vid):
    video_id = urlparse(str(vid))
    q = parse_qs(video_id.query)
    vidID = q["v"][0]
    return vidID

def openURL(url, parms):
        f = urlopen(url + '?' + urlencode(parms))
        data = f.read()
        f.close()
        matches = data.decode("utf-8")
        return matches
