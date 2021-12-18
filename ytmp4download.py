import pytube
from pytube.streams import Stream

link = input('type your link here ')

def downloadVideo(link):
    youTube = pytube.YouTube(link)
    stream = youTube.streams.get_highest_resolution()
    stream.download()
downloadVideo(link)
