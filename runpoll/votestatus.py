import os

import runpoll.chckpoll as chkp
import runpoll.checkPollStatus as chkps


def votestatus():
    chkp.chkpolls()
    selectedPoll = int(input("❓ Type the number :- "))
    if os.path.exists(str(selectedPoll)) == False:
                print("❌ The Poll is Not listed")
    else :
                os.chdir(str(selectedPoll))
                
                selectedFile = f"{selectedPoll}.txt"
                chkps.checkpollstauts(selectedFile)