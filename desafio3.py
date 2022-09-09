from pytube import YouTube

url = input("digite a url do YouTube:")

video = YouTube(url)

#video.streams.get_lowest_resolution().download(
#    output_path="C:\YTD-DOWNLOADS",
#    filename=video.title
#)

video.streams.filter(only_audio=True).first().download(
    output_path="C:\YTD-DOWNLOADS",
    filename=video.title + ".mp3"
)


