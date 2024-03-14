import os
import linecache
import access.details as details
  
datafolder = "data"
rootfolder = os.getcwd()
    
def forgotpass():
    name = details.name().lower()
    uname = details.username().lower()    
    os.chdir(datafolder)
        
        
    if os.path.exists(name):
                    os.chdir(name)
                    question = linecache.getline(uname, 2)
                    passwd = linecache.getline(uname, 1)
                    chckans = linecache.getline(uname, 3)
                    ans = input(f"{question}➡ Your Answer :- ")
                    formatans = f"{ans}\n"
                    
                    if chckans == formatans:
                        print(f"{passwd}")
                        os.chdir(rootfolder)
                    else:
                        print("❌ Sorry Your answer is wrong. Try Again or Create a New account")
                        os.chdir(rootfolder)

    elif os.path.exists(name) == False:
                    print("❌ No Account was created with this name try again or sign up")
                    os.chdir(rootfolder)
                    