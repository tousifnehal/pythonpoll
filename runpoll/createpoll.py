import os

pollfile = "poll"
rootfolder = os.getcwd()
pollsl = "pollsl.txt"
totalvote = "totalvote.txt"


def create():
        os.chdir(pollfile)
        
        with open(pollsl, "r") as f:
            num = f.read()
            
        pollques = input("➡ Enter The Poll Question : ")
        numopt = int(input("❓ How Many Options? "))
        
        os.mkdir(num)
        os.chdir(num)
        
        with open(f"{num}.txt", "w") as f:
            f.write(f"{pollques} \n")
            
        for i in range(1, numopt+1):
            ques = input(f"➡ Option {i}: ")
            with open(f"{num}.txt", "a") as f:
                f.write(f"{ques} \n")

        for i in range(1, numopt+1):
            optionfile = f"opt{i}.txt"
            with open(optionfile, "w") as f:
                f.write(str(0))
                
        with open(totalvote, "w") as f:
            f.write(str(0))   
     
        os.chdir(rootfolder)
        os.chdir(pollfile)
        
        with open(pollsl, "w") as f:
            numint = int(num)
            numint += 1
            f.write(str(numint)) 
                       
        print("✅ POLL CREATED SUCCESSFULLY")
        os.chdir(rootfolder)