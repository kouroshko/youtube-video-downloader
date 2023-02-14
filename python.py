from pytube import YouTube

download = False


def downloader():
    link = input('link :')
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    download = True
    if download == True:
        print("\033[32m Done downloaded succesfully!\033[0m")


downloader()
