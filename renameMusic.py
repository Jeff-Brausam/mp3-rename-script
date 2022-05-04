import eyed3
import os

musicList = []
CurrentWorkingDirectory = os.getcwd()

def get_mp3_list():
  for file in os.listdir(CurrentWorkingDirectory):
    if file.endswith(".mp3"): 
      musicList.append(file)
get_mp3_list()

def create_ID3_tag(fileName):
  audiofile = eyed3.load(fileName)
  
  # Split the title, grab the artist and title
  nameSplit = fileName.split(' - ')
  artist = nameSplit[0]
  title = nameSplit[1].split('.mp3')[0]
 
  # Edit ID3 tag
  if (audiofile.tag == None):
    audiofile.initTag()
  audiofile.tag.artist = artist
  audiofile.tag.title = title
  audiofile.tag.save()

  # # Rename the file to just the title, the ID3 has the rest of the information
  os.replace(f"{CurrentWorkingDirectory}/{fileName}", f"{CurrentWorkingDirectory}/{title}.mp3")

def process_mp3s():
  for file in musicList:
    create_ID3_tag(file)

process_mp3s()


