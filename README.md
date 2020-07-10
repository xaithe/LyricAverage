# LyricAverage
LyricAverage is a CLI program for getting statistics about the words in an artist's songs.


## Prerequisites
The script has a few dependencies, all defined in _requirements.txt_.

They can be installed with:

```
pip install -r requirements.txt
```

## Usage
The script is fairly simple and allows you to specify what stats you want to view. A future deveopment would be to write the data to a file i.e. CSV or JSON.

```
Python lyricaverage.py <"artist name"> [-m, --minmax] [-s, --stats] [-i, --interactive]
```

The optional args can also be written as a single string. 
For example, if I wanted to get the minimum and maximum word count, the additonal stats (standard deviation and variance), and enter the interactive search for the Foo Fighters:

```
Python lyricaverage.py "Foo Fighters" -msi
```

## Args

### No args

Just entering the name of an artist will return the total number of songs by the artist and the mean average word count of all those songs.

### -m/--minmax

Enables the return of the minimum and maximum word counts in the artist's discography.

### -s/--stats

Enables the return of an extended list of statistics about the artist's discography. Currently includes standard deviation and variance.

### -i/--interactive

Allows the user to enter the interactive "search" following the intial display of data. This allows the user to gain insight into a specific song, and how it relates to the overall discography of the artist.

![](https://i.gyazo.com/b2a43d3f0f2d600be40b24446368cd71.png)