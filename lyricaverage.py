import sys
from queue import Queue
import numpy as np
from scipy import stats
import argparse
import threading
import modules.songnames as songnames
import modules.lyrics as lyrics
import modules.helpers as helpers

parser = argparse.ArgumentParser()
parser.add_argument("artist", help="The name of the artist you want to look up")
parser.add_argument("-m", "--minmax", help="Only output min/max lyric count", action="store_true")
parser.add_argument("-s", "--stats", help="Show all calculated statistics", action="store_true")
parser.add_argument("-i", "--interactive", help="Enter song search after stats are displayed", action="store_true")

args = parser.parse_args()

BOLD = "\033[1m"
END = "\033[0m"
queue = Queue()
discography = dict()
instrumentals = []
artist = args.artist

artistid = songnames.getArtistId(artist)

print("\nConstructing song list...")
songslist = songnames.getSongs(artistid)

def loadSongs(songs):
    for song in songs:
        queue.put(song)

def worker():
    while not queue.empty():
        song = queue.get()
        songlyrics = lyrics.getLyrics(artist, song)
        count = lyrics.countWords(songlyrics)

        if count == 1:
            instrumentals.append(song)

        discography[song.lower()] = count

def lyricCounter(numberOfThreads,songs):
    loadSongs(songs)
    threads = []
    try:
        for t in range(numberOfThreads):
            thread = threading.Thread(target=worker)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit()


lyricCounter(100, songslist)


discovalid = np.asarray(list(i for i in discography.values() if i > 1))
discolicence = np.asarray(list(i for i in discography.values() if i < 0))

validmin = np.amin(discovalid)
validmax = np.amax(discovalid)
validmean = np.mean(discovalid)
validstd = np.std(discovalid)
validvar = np.var(discovalid)

print("\nLyric stats for " + BOLD + artist + END)
print("Total Songs: {:d}".format(len(discography.items())))
print("Can be shown: {:d} ({:f}%)".format(discovalid.size, helpers.percentage(discovalid.size, len(discography.items()))))
print("Instrumentals: {:d} ({:f}%)".format(len(instrumentals), helpers.percentage(len(instrumentals), len(discography.items()))))
print("Not licensed : {:d} ({:f}%)".format(discolicence.size, helpers.percentage(discolicence.size, len(discography.items()))))
print("No lyrics on the API (likley covers): {:d} ({:f}%)".format(len(helpers.getErrors(discography)), helpers.percentage(len(helpers.getErrors(discography)), len(discography.items()))))
print("\nMean average song length: {:f}".format(validmean))

if args.minmax:
    print("\nMinimum song length: {:d} words".format(validmin))
    for title in helpers.minNames(discography):
        print(title.title())
    print("\nMaximum song length: {:d}".format(validmax))
    for title in helpers.maxNames(discography):
        print(title.title())

if args.stats:
    print("\nStandard deviation: {:f}".format(validstd))
    print("Variance: {:f}".format(validvar))

if args.interactive:
    while True:
        print("\nEnter a song title for more information, or exit (CTRL+C):")
        try:
            lookup = input(">")
            lookup = lookup.lower()

            if lookup not in discography:
                count = -1
            else:
                count = discography[lookup]

            if count < 1:
                print("Sorry, we couldn't find lyrics for that song\n")
                continue

            print("\nLyric count for {}{}{} by {}: {:d}".format(BOLD, lookup.title(), END, artist,count))

            if count > int(validmean):
                print("{:d} words longer than the average for {}".format(int(count - validmean), artist))
            elif count < int(validmean):
                print("{:d} words shorter than the average for {}".format(int(validmean - count), artist))
            else:
                print("Length is equal to the average for {}".format(artist))
            
            percentile = stats.percentileofscore(discovalid, count)

            print("{} is in the {} percentile of {} songs".format(lookup.title(), helpers.ordinal(percentile), artist))

            fulllyrics = input("\nWould you like to view the full lyrics for {}? (y/n):".format(lookup.title()))

            if fulllyrics.lower() == "y":
                songLyrics = lyrics.getLyrics(artist, lookup)
                print("Full lyrics:\n")
                print(songLyrics + "\n")
            else:
                continue

        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit()
    

        
