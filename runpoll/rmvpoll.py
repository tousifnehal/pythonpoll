import os
import linecache
import shutil

pollfile = "poll"
rootfolder = os.getcwd()
pollsl = "pollsl.txt"
totalvote = "totalvote.txt"

def rmvpoll():
        os.chdir(pollfile)
        allques = os.listdir()
        print("➡ All Polls Are Listed Here \n")
        for i in range(len(allques)-1):
                file = allques[i]
                os.chdir(file)
                quest = linecache.getline(f"{file}.txt", 1)
                print(f"{i + 1}. {quest}")
                os.chdir(rootfolder)
                os.chdir(pollfile)
        polldlt = int(input("❓ Which poll you want to delete. Type The Number: "))
        if os.path.exists(polldlt) == False:
            print("❌ The Poll is not listed")
        else:
            shutil.rmtree(str(polldlt))
            print("✅ Poll Deleted Successfully")
        os.chdir(rootfolder)