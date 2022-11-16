#!/usr/bin/python3

from pytube import YouTube

def Download(path, link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download(path)
        print(f"Download is completed successfully on {path}.")
    except:
        print("An error has occurred.")

link = input("Enter the Youtube video URL: ")
path = input("Enter the download path: ")

print("\nPlease wait, your download is starting now...")

Download(path, link)