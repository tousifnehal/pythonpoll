import random
import linecache
totalvote = "totalvote.txt"


def checkpollstauts(selectedFile):
                with open(selectedFile, "r") as file:
                    lines = file.readlines()
                    lineCount = len(lines)
                stars = "*" * random.randint(15,30)
                totalvotes = linecache.getline(totalvote, 1)
                
                print(stars)
                print("➡ VOTE RESULT")
                print(f"➡ The Poll Was About : {linecache.getline(selectedFile, 1)}")
                sl = 1
                for i in range(2,lineCount+1):
                    optionline = linecache.getline(selectedFile, i)
                    optvotedgrab = f"opt{sl}.txt"
                    with open(optvotedgrab, "r") as f:
                        numvoted = f.read()
                    totalOptvotes = int(numvoted)
                    votecalc = (totalOptvotes /int(totalvotes) ) * 100
                    rounded_number = round(votecalc, 2)
                    print(f"\n➡ Option {sl}. {optionline}", end="") 
                    print(f"➡ {totalOptvotes} Persons voted {optionline}Percentage : {rounded_number}%")
                    sl += 1
                print(f"\n ➡ Total Votes : {totalvotes}")
                print(stars)  