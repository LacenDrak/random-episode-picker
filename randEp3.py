__author__  = "Scott Maslin"
__version__ = "2.0.8"

import wx
import pickergui
import os
import subprocess
import random

print("### DEBUG ###")
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

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

class myInterface(pickergui.mainscreen):
    files = []
    path = os.getcwd()
    filesCollected = False
    includeSubdirs = True
    currentChar = 0
    targetFileTypes = [".mp4", ".avi", ".mkv", ".m4v", ".mpg"]
    
    def __init__(self, parent):
        pickergui.mainscreen.__init__(self, parent)
        self.dirPicker.SetPath(self.path)

    def printToDebug(self, inputStr):
        self.currentChar += len(inputStr)
        self.debugOutputBox.AppendText(inputStr)

    def isWantedFiletype(self, filename):
        for filetype in self.targetFileTypes:
            if(hasFileExtension(filename, filetype)):
                return True
        return False

    def printErrorToDebug(self, inputStr):
        prevCurrentChar = self.currentChar
        self.printToDebug(inputStr)
        self.debugOutputBox.SetStyle(prevCurrentChar, self.currentChar,(wx.TextAttr(wx.RED)))
        self.debugOutputBox.SetStyle(self.currentChar, self.currentChar + 2048, (wx.TextAttr(wx.BLACK)))

    def setNewPath(self, event):
        self.path = self.dirPicker.GetPath()
        print(f"Dir changed to {self.path}")
        self.printToDebug(f"Directory changed to {self.path}\n")

    def changeSubdir(self, event):
        self.includeSubdirs = self.subdirCheckBox.GetValue()
        if(self.includeSubdirs):
            print("Including subdirectories in collection")
            self.printToDebug("Include subdirectories\n")
        else:
            print("Not including subdirectories in collection")
            self.printToDebug("Don't include subdirectories\n")

    def collectfiles(self, event):
        self.files = [] #An empty list of the files in all subdirectories
        numTotalFiles = 0
        #ToDo: Modify to include/not include subdirectories
        if(self.includeSubdirs):
            for (dirpath, dirnames, filenames) in os.walk(self.path):  #Walk through all subdirs
                for fname in filenames:                           #Get all the files in each subdir
                    numTotalFiles += 1
                    if(self.isWantedFiletype(fname.lower())):
                         self.files.append(os.path.join(dirpath,fname))#Then add their total path to the list (not just the relative path)
        else:
            for (dirpath, dirnames, filenames) in walklevel(self.path,0):
                for fname in filenames:
                    numTotalFiles += 1
                    if(self.isWantedFiletype(fname.lower())):
                         self.files.append(os.path.join(dirpath,name))#Then add their total path to the list (not just the relative path)
        print(f"Collecting files function complete! Collected {len(self.files)} files of {numTotalFiles}.")
        self.printToDebug(f"Collecting files...\n")
        if(len(self.files) == 0):
            self.printErrorToDebug(f"Found no video files in {numTotalFiles} files!\n")
            return
        else:
            self.printToDebug(f"Found {len(self.files)} video files in {numTotalFiles} files.\n")
        self.filesCollected = True

    def pickepisodes(self, event):
        if(self.filesCollected == False):
            self.printErrorToDebug("Files not yet collected! Running collection first...\n")
            self.collectfiles(wx.EVT_BUTTON)
        if(len(self.files) == 0):
            self.printErrorToDebug("Can't pick from no files! Try a different directory.\n")
            #https://stackoverflow.com/questions/46313673/how-can-i-change-the-color-of-specific-words-in-wxpython-textctrl
            return
        print("Pick episodes button pressed!")
        numToPick = int(self.numEpsSpinner.GetValue())
        print(f"Picking {numToPick} episodes...")
        self.printToDebug(f"Picking {numToPick} episodes...\n")
        print("Randomising files")
        self.printToDebug("Randomising files...\n")
        random.shuffle(self.files)
        print("Running VLC Media Player...")
        self.printToDebug("Running VLC Media Player:\n")
        commandStr = "vlc --one-instance --playlist-enqueue"
        if(len(self.files) >= numToPick):
            indices = random.sample(range(1,len(self.files)),numToPick) 
            for i in range(numToPick):
                commandStr += ' "' +self.files[indices[i]] +'"'
        else:
            for i in range(len(self.files)):
                commandStr += ' "' +self.files[i] +'"'
        print(commandStr)
        self.printToDebug("\t" +commandStr +"\n")
        subprocess.Popen(commandStr)
                                                      
app = wx.App(redirect=False)

frame = myInterface(None)

frame.Show(True)

app.MainLoop()
