def percentage(numerator, denominator):
    """[summary]

    Args:
        numerator ([type]): [description]
        denominator ([type]): [description]

    Returns:
        [type]: [description]
    """    
    return (numerator/denominator)*100

def ordinal(value):
    """[summary]

    Args:
        value ([type]): [description]

    Returns:
        [type]: [description]
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
    """[summary]

    Args:
        songs ([type]): [description]

    Returns:
        [type]: [description]
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
    """[summary]

    Args:
        songs ([type]): [description]

    Returns:
        [type]: [description]
    """    

    maximum = max(songs.values())
    songsout = []
    for title, length in songs.items():
        if length == maximum:
            songsout.append(title)
    return songsout

def getErrors(songs):
    """[summary]

    Args:
        songs ([type]): [description]

    Returns:
        [type]: [description]
    """    

    songsout = []
    for title, length in songs.items():
        if length == 0:
            songsout.append(title)
    return songsout
