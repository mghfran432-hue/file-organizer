import os
print("file organizer")
folder = os.getcwd()
for file in os.listdir(folder):
    extension = os.path.splitext(file)
    if extension in( ".jpg",".png",".jpeg"):
       
       os.makedirs("Images",exist_ok=True)
       os.rename(file,os.path.join("Images",file))
    if extension == ".mp3":
       os.makedirs("Music",exist_ok=True)
       os.rename(file,os.path.join("Music",file))
       
    if extension == ".pdf":
       os.makedirs("Documents",exist_ok=True)
       os.rename(file,os.path.join("Documents",file))
    if extension == ".docx":
       os.makedirs("Documents",exist_ok=True)
       os.rename(file,os.path.join("Documents",file))
       
    if extension == ".mp4":
       os.makedirs("Videos",exist_ok=True)
       os.rename(file,os.path.join("Videos",file))
      
