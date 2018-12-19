__author__  = "Scott Maslin"
__version__ = "2.0.0"

import wx
import pickergui
import os
import subprocess
import random

print("###DEBUG###")
print("Program start!")

#Function to find all occurences of a substring within a string
#(unlike str.find which just finds the first)
#Yields a generator of substring occurances
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

path = os.getcwd()
#path = "F:/"

class myInterface(pickergui.mainscreen):
    files = []
    filesCollected = False
    def __init__(self, parent):
        pickergui.mainscreen.__init__(self, parent)

    def collectfiles(self, event):
        self.files = [] #An empty list of the files in all subdirectories
        numTotalFiles = 0
        for (dirpath, dirnames, filenames) in os.walk(path):  #Walk through all subdirs
            for fname in filenames:                           #Get all the files in each subdir
                numTotalFiles += 1
                name = fname.lower()                          #Make the filename case insensitive
                if (hasFileExtension(name, ".mp4")
                 or hasFileExtension(name, ".avi")           #Filter out the non-video filenames
                 or hasFileExtension(name, ".mkv")          
                 or hasFileExtension(name, ".m4v")
                 or hasFileExtension(name, ".mpg")):        
                     self.files.append(os.path.join(dirpath,name))#Then add their total path to the list (not just the relative path)
        print(f"Collecting files function complete! Collected {len(self.files)} files of {numTotalFiles}.")
        self.debugOutputBox.AppendText(f"Collecting files...\n")
        self.debugOutputBox.AppendText(f"Found {len(self.files)} video files in {numTotalFiles} files.\n")
        self.filesCollected = True

    def pickepisodes(self, event):
        if(self.filesCollected == False):
            strToPrint = "Files not yet collected! Running collection first...\n"
            #https://stackoverflow.com/questions/46313673/how-can-i-change-the-color-of-specific-words-in-wxpython-textctrl
            self.debugOutputBox.SetStyle(0, len(strToPrint),(wx.TextAttr(wx.RED)))
            self.debugOutputBox.AppendText(strToPrint)
            print("Files not collected, running collection...\n")
            self.debugOutputBox.SetStyle(len(strToPrint), 1024, (wx.TextAttr(wx.BLACK)))
            self.collectfiles(wx.EVT_BUTTON)
        print("Pick episodes button pressed!")
        numToPick = int(self.numEpsSpinner.GetValue())
        print(f"Picking {numToPick} episodes...")
        self.debugOutputBox.AppendText(f"Picking {numToPick} episodes...\n")
        print("Randomising files")
        self.debugOutputBox.AppendText("Randomising files...\n")
        random.shuffle(self.files)
        print("Running VLC Media Player...")
        self.debugOutputBox.AppendText("Running VLC Media Player:\n")
        commandStr = "vlc --one-instance --playlist-enqueue"
        if(len(self.files) >= numToPick):
            indices = random.sample(range(1,len(self.files)),numToPick) 
            for i in range(numToPick):
                commandStr += ' "' +self.files[indices[i]] +'"'
        else:
            for i in range(len(self.files)):
                commandStr += ' "' +self.files[i] +'"'
        print(commandStr)
        self.debugOutputBox.AppendText("\t" +commandStr +"\n")
        subprocess.Popen(commandStr)
                                                      
app = wx.App(redirect=False)

frame = myInterface(None)

frame.Show(True)

app.MainLoop()
