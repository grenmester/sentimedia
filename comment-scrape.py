import json
import sys
from urllib import *
import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import  urlopen

final_comments = []
YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

class YouTubeApi():

    def get_video_comment(self):

        def load_comments(self):
            for item in mat["items"]:
                comment = item["snippet"]["topLevelComment"]
                text = comment["snippet"]["textDisplay"]
                final_comments.append(text)

        parser = argparse.ArgumentParser()
        mxRes = 10
        vid = str()
        parser.add_argument("--c", help="calls comment function by keyword function", action='store_true')
        parser.add_argument("--max", help="number of comments to return")
        parser.add_argument("--videourl", help="Required URL for which comments to return")
        parser.add_argument("--key", help="Required API key")

        args = parser.parse_args()

        if not args.max:
            args.max = mxRes

        if not args.videourl:
            exit("Please specify video URL using the --videourl=parameter.")

        try:
            video_id = urlparse(str(args.videourl))
            q = parse_qs(video_id.query)
            vid = q["v"][0]

        except:
            print("Invalid YouTube URL")

        parms = {
                    'part': 'snippet,replies',
                    'videoId': vid,
                    'key': 'AIzaSyBsuQEzXjJ81-8ywBftLva-0j19hWNMc1w'
                }

        try:

            matches = self.openURL(YOUTUBE_COMMENT_URL, parms)
            i = 0
            mat = json.loads(matches)
            load_comments(self)

        except KeyboardInterrupt:
            print("User Aborted the Operation")

        except:
            print("Cannot Open URL or Fetch comments at a moment")


    def openURL(self, url, parms):
            f = urlopen(url + '?' + urlencode(parms))
            data = f.read()
            f.close()
            matches = data.decode("utf-8")
            return matches

def main():
    y = YouTubeApi()
    y.get_video_comment()
    print(final_comments)

if __name__ == '__main__':
    main()