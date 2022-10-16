from pytube import YouTube

link = input("enter the url of video to download:")

you = YouTube(link)

print(you.title)

quality = you.streams.all()
vid = list(enumerate(quality))

for i in vid:
    print(i)

choice = int(input("enter your choice:"))
quality[choice].download()
print("succesfull download...")
