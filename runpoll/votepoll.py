import os
import linecache
import random
import runpoll.checkPollStatus as chkps

pollfile = "poll"
rootfolder = os.getcwd()
pollsl = "pollsl.txt"
totalvote = "totalvote.txt"

def votepoll():
        os.chdir(pollfile)
        allques = os.listdir()
        print("➡ Enter The Number Beside The Poll Question To Select Which one to vote \n")
        for i in range(len(allques)-1):
                file = allques[i]
                os.chdir(file)
                quest = linecache.getline(f"{file}.txt", 1)
                print(f"{i + 1}. {quest}")
                os.chdir(rootfolder)
                os.chdir(pollfile)
        os.chdir(rootfolder)
        os.chdir(pollfile)
        selectedPoll = int(input("❓ Type the number :- "))
        if os.path.exists(str(selectedPoll)) == False:
            print("❌ The Poll is Not listed")
        else :
            os.chdir(str(selectedPoll))
            
            selectedFile = f"{selectedPoll}.txt"
            
            sl = 1
            
            with open(selectedFile, "r") as file:
                lines = file.readlines()
                lineCount = len(lines)
                
            for i in range(2,lineCount+1):
                optionline = linecache.getline(selectedFile, i)
                print(f"\n➡ Option {sl}. {optionline}", end="") 
                sl += 1
                if i == lineCount:
                    print("\n")
            
            uservote = int(input("❓ Which Option You wanna vote :- "))
            if uservote > sl-1:
                print("❌ The Option is not listed")
                # adcmdval = False
            else:    
                optionvoted = f"opt{uservote}.txt"
                print(optionvoted)
                with open(optionvoted, "r") as f:
                    optvoted = f.readline()
                optcalc = int(optvoted) + 1
                
                with open(optionvoted, "w") as f:
                    f.write(str(optcalc))

                
                tvotecounter = linecache.getline(totalvote, 1)
                
                totalint = int(tvotecounter) + 1

                
                with open(totalvote, "w") as f:
                    f.write(str(totalint)) 
                
                print("✅ Voted Successfully")
            
                
                chkps.checkpollstauts(selectedFile, totalint)
                # stars = "*" * random.randint(15,30)
                # totalvotes = linecache.getline(totalvote, 1)
                
                # print(stars)
                # print("➡ VOTE RESULT")
                # print(f"➡ The Poll Was About : {linecache.getline(selectedFile, 1)}")
                # sl = 1
                # for i in range(2,lineCount+1):
                #     optionline = linecache.getline(selectedFile, i)
                #     optvotedgrab = f"opt{sl}.txt"
                #     with open(optvotedgrab, "r") as f:
                #         numvoted = f.read()
                #     totalOptvotes = int(numvoted)
                #     votecalc = (totalOptvotes /int(totalvotes) ) * 100
                #     rounded_number = round(votecalc, 2)
                #     print(f"\n➡ Option {sl}. {optionline}", end="") 
                #     print(f"➡ {totalOptvotes} Persons voted {optionline}Percentage : {rounded_number}%")
                #     sl += 1
                # print(f"\n ➡ Total Votes : {totalvotes}")
                # print(stars)  
                os.chdir(rootfolder)