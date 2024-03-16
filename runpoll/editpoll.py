import os
import linecache


pollfile = "poll"
rootfolder = os.getcwd()
pollsl = "pollsl.txt"
totalvote = "totalvote.txt"


def lineEdit(file_path, new_content, linenum):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines[linenum-1] = new_content + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)
def optEdit(file_path, new_content, linenum):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines[linenum] = new_content + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines) 
                            
        
        
def editpoll():
            
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
        pollnum = int(input("❓ Which poll you want to edit. Type The Number: "))
        if os.path.exists(pollnum) == False:
            print("❌ The Poll is not listed")
        else:
            edit = int(input("❓ Which Thing You want to edit? \n\tType \n\t➡ 1 for Title\n\t➡ 2 for options \n"))
            if edit == 1:
                os.chdir(str(pollnum))
                pretitle = linecache.getline(f"{pollnum}.txt", 1)
                print(f"❗ Previous Title was :- {pretitle}")
                newtitle = input("➡ Enter Your New title :- ")
                if pretitle == newtitle:
                    print("❌ The title was same can't edited")
                else:
                    lineEdit(f"{pollnum}.txt", newtitle, 1)
                    print("✅ Title Updated successfully")
            if edit == 2:
                os.chdir(str(pollnum))
                sl = 1
            
                with open(f"{pollnum}.txt", "r") as file:
                    lines = file.readlines()
                    lineCount = len(lines)
                    
                for i in range(2,lineCount+1):
                    optionline = linecache.getline(f"{pollnum}.txt", i)
                    print(f"\n➡ Option {sl}. {optionline}", end="") 
                    sl += 1
                    if i == lineCount:
                        print("\n")
                
                uservote = int(input("❓ Which Option You wanna edit :- "))
                if uservote > sl-1:
                    print("❌ The Option is not listed")
                    
                else:
                    newopt = input("➡ Enter The New Option: ")
                    optEdit(f"{pollnum}.txt", newopt, uservote)
                    print("✅ Edited successfully")
        os.chdir(rootfolder)