"""
@author: Tom Gulliver

"""

def percentage(numerator, denominator):
    """Quick funtion for finding the percentage of two numbers

    Args:
        numerator (float): the numberator
        denominator (float): the denominator

    Returns:
        float: the resultant percentage value
    """    
    return (numerator/denominator)*100

def ordinal(value):
    """Appends the correct ordinal to a number

    Args:
        value (int): [description]

    Returns:
        string: the number with appended ordinal
    """    

    if value % 100//10 != 1:
        if value % 10 == 1:
            ordval = "{:d}st".format(int(value))
        elif value % 10 == 2:
            ordval = "{:d}nd".format(int(value))
        elif value % 10 == 3:
            ordval ="{:d}rd".format(int(value))
        else:
            ordval = "{:d}th".format(int(value))
    else:
        ordval = "{:d}th".format(int(value))

    return ordval

def minNames(songs):
    """Finds the titles of the songs with the minimum word count

    Args:
        songs (dict[string : int]): A dict mapping a song to it's word count

    Returns:
        list[string]: A list of song titles
    """        

    minimum = min(i for i in songs.values() if i > 1)
    songsout = []
    for title, length in songs.items():
        if length == 0:
            continue
        if length == minimum:
            songsout.append(title)
    return songsout

def maxNames(songs):
    """Finds the titles of the songs with the maximum word count

    Args:
        songs (dict[string : int]): A dict mapping a song to it's word count

    Returns:
        list[string]: A list of song titles
    """    

    maximum = max(songs.values())
    songsout = []
    for title, length in songs.items():
        if length == maximum:
            songsout.append(title)
    return songsout

def getErrors(songs):
    """Finds the errored songs in a dict of title: word count

    Args:
        songs (dict[string : int]): A dict mapping a song to it's word count

    Returns:
        list[string]: A list of song titles
    """    

    songsout = []
    for title, length in songs.items():
        if length == 0:
            songsout.append(title)
    return songsout
