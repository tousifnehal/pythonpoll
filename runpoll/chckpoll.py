import os
import linecache

pollfile = "poll"
rootfolder = os.getcwd()
pollsl = "pollsl.txt"
totalvote = "totalvote.txt"

def chkpolls():
        os.chdir(pollfile)
        allques = os.listdir()
        print("✅ All Polls Are Listed Here \n")
        for i in range(len(allques)-1):
                file = allques[i]
                os.chdir(file)
                quest = linecache.getline(f"{file}.txt", 1)
                print(f"{i + 1}. {quest}")
                os.chdir(rootfolder)
                os.chdir(pollfile)
            
        os.chdir(rootfolder)