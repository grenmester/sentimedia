import json
import sys
from urllib import *
import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import urlopen

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

    url_data = urlparse(vid)
    query = parse_qs(url_data.query)
    video = query["v"][0]

    parms = {
        'part': 'snippet',
        'videoId': video,
        'key': 'AIzaSyBsuQEzXjJ81-8ywBftLva-0j19hWNMc1w'
            }

    try:

        matches = openURL('https://www.googleapis.com/youtube/v3/commentThreads', parms)
        mat = json.loads(matches)
        load_comments()

    except KeyboardInterrupt:
        print("User Aborted the Operation")

    except:
        print("Cannot Open URL or Fetch comments at a moment")

    return final_comments

def get_channel_comments(channel):
    channel_comments = []
    def load_channel_comments():
        for item in mat["items"]:
            comment = item["snippet"]["topLevelComment"]
            text = comment["snippet"]["textDisplay"]
            channel_comments.append(text)

    try:
        channel_id = channel.rsplit('/', 1)
        chanfinal = channel_id[-1]

    except:
        print("Invalid YouTube URL")

    parms = {
        'part': 'snippet',
        'channelId': chanfinal,
        'key': 'AIzaSyBsuQEzXjJ81-8ywBftLva-0j19hWNMc1w'
            }

    try:


        matches = openURL('https://www.googleapis.com/youtube/v3/commentThreads', parms)
        mat = json.loads(matches)
        load_channel_comments()

    except KeyboardInterrupt:
        print("User Aborted the Operation")

    except:
        print("Cannot Open URL or Fetch comments at a moment")

    return channel_comments

def get_embed_id(vid):
    video_id = urlparse(str(vid))
    q = parse_qs(video_id.query)
    vidID = q["v"][0]
    embed = 'https://www.youtube.com/embed/' + vidID
    return embed

def openURL(url, parms):
        f = urlopen(url + '?' + urlencode(parms))
        data = f.read()
        f.close()
        matches = data.decode("utf-8")
        return matches
