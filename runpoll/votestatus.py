import os
import linecache
import runpoll.chckpoll as chkp
import runpoll.checkPollStatus as chkps

totalvote = "totalvote.txt"

def votestatus():
    chkp.chkpolls()
    selectedPoll = int(input("❓ Type the number :- "))
    os.chdir(chkp.pollfile)
    if os.path.exists(str(selectedPoll)) == False:
                print("❌ The Poll is Not listed")
    else :
                os.chdir(str(selectedPoll))
                
                selectedFile = f"{selectedPoll}.txt"
                totalvotes = linecache.getline(totalvote, 1)
                chkps.checkpollstauts(selectedFile, totalvotes)
    os.chdir(chkp.rootfolder)