import os
import subprocess
files=os.listdir("videos")
for file in files:
    tutorial_number = file.split("#")[1].split(".")[0]
    filename=file.split("_")[0]
    print(tutorial_number)
    print(filename)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{tutorial_number}_{filename}.mp3"])