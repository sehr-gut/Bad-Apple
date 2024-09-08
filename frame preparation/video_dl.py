from pytubefix import YouTube
from pytubefix.cli import on_progress

def dl(link):
    yt = YouTube(link, on_progress_callback = on_progress)

    videos = yt.streams.filter(progressive= True, file_extension="mp4").first()
    print(videos)
    videos.download("C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/badAppleVideo")





if __name__ == "__main__":
    inp = input("put yo link here: ")
    dl(inp)