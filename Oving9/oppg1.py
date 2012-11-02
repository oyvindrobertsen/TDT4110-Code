videoer = [
        'http://www.youtube.com/watch?v=oKI-tD0L18A',
        'http://www.youtube.com/watch?v=82LCKBdjywQ',
        'http://www.youtube.com/watch?v=GpNSip5gyKo',
        'http://www.youtube.com/watch?v=rHG-JO8gIGk',
        'http://www.youtube.com/watch?v=ZFngtBIxRPk',
        'http://www.youtube.com/watch?v=OZBWfyYtYQY',
        ]

def yt_short(videoliste):
    videoer_short = []
    for i in videoliste:
        videoer_short.append('youtu.be/' +  i[(i.find('=') + 1):])

    return videoer_short

def main():
    print(yt_short(videoer))


main()
