"""Choose ten random video files in the directory the script is in"""
__author__  = "Scott Maslin"
__version__ = "1.2"

import os
import subprocess
from random import shuffle, sample

#Function to find all occurences of a substring within a string
#(unlike str.find which just finds the first)
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

#Function to determine if a given filename has the given extension
#Checks whether the extension substring constitutes the end of the string
def hasFileExtension(filename, extension):
    occurances = list(find_all(filename, extension))
    if not occurances: return False   #True when list is empty, so filename doesn't contain the extension (avoids index error)
    return occurances[-1] == len(filename)-len(extension) #Else check if last occurance at end of str

print("Collecting files...")

#Get the current working directory of the program
path = os.getcwd()

files = [] #An empty list of the files in all subdirectories
numTotalFiles = 0
for (dirpath, dirnames, filenames) in os.walk(path):  #Walk through all subdirs
    for fname in filenames:                           #Get all the files in each subdir
        numTotalFiles += 1
        name = fname.lower()                          #Make the filename case insensitive
        if  (hasFileExtension(name, ".mp4")
          or hasFileExtension(name, ".avi")           #Filter out the non-video filenames
          or hasFileExtension(name, ".mkv")          
          or hasFileExtension(name, ".m4v")
          or hasFileExtension(name, ".mpg")):        
              files.append(os.path.join(dirpath,name))#Then add their total path to the
                                                      #list (not just the relative path)
print(f"Found {numTotalFiles} files, {len(files)} videos...")

#Random shuffle the list of files
print("Randomising files...")
shuffle(files)

print("Running VLC Media Player...")

#Command to add the following files to VLC playlist
commandStr = "vlc --one-instance --playlist-enqueue"

#Add up to 10 files to VLC playlist
if(len(files) >= 10):
    indices = sample(range(1,len(files)),10) #10 exclusive random indices
    for i in range(10):
        commandStr += ' "' +files[indices[i]] +'"'
else:
    for i in range(len(files)):
        commandStr += ' "' +files[i] +'"'
        
subprocess.Popen(commandStr) #Run the command to open VLC, then immediately close the shell
