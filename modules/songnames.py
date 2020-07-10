"""
@author: Tom Gulliver

"""

import json
import requests

ARTIST_SEARCH_MAIN = "https://musicbrainz.org/ws/2/artist?query="
ARTIST_SEACH_END = "&limit=1&fmt=json"

SONG_BROWSE_MAIN = "https://musicbrainz.org/ws/2/work?artist="
SONG_BROWSE_END = "&limit=100&fmt=json&offset="
#SONG_BROWSE_INITAL = ""
def getArtistId(artistName):
    """Function to get the ID of a given artist on the musicbrainz.org API

    Args:
        artistName (string): The name of the artist to search for

    Returns:
        string: ArtistID
    """    

    querystring = ARTIST_SEARCH_MAIN + artistName + ARTIST_SEACH_END
    req = requests.get(querystring)
    
    response = req.json()
    artistid = response["artists"][0]["id"]

    return artistid

def songSearch(artistId,offset):
    """[summary]

    Args:
        artistId ([type]): [description]
        offset ([type]): [description]

    Returns:
        [type]: [description]
    """    

    querystring = SONG_BROWSE_MAIN + artistId + SONG_BROWSE_END + str(offset)
    req = requests.get(querystring)

    return req.json()

def getWorkCount(artistId):
    """[summary]

    Args:
        artistId ([type]): [description]

    Returns:
        [type]: [description]
    """    

    querystring = SONG_BROWSE_MAIN + artistId + SONG_BROWSE_END + "0"
    req = requests.get(querystring)

    response = req.json()
    return response["work-count"]

def getSongs(artistId):
    """[summary]

    Args:
        artistId ([type]): [description]

    Returns:
        [type]: [description]
    """    

    offset = 0
    songcount = getWorkCount(artistId)
    songnames = set()

    while offset < songcount:
        searchpage = songSearch(artistId, offset)
        for song in searchpage["works"]:
            if song["type"] == "Song":
                songnames.add(song["title"])

        offset+=100

    return songnames
    