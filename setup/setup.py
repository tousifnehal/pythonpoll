# Path creation
import os
import access.details as details

datafolder = "data"
rootfolder = os.getcwd()
pollfile = "poll"
pollsl = "pollsl.txt"
totalvote = "totalvote.txt"

def runsetup():  
    
    if os.path.exists(pollfile) == False:
        
        os.mkdir(pollfile)
        os.chdir(pollfile)

        with open(pollsl, "w") as f:
                f.write(str(1))
                os.chdir(rootfolder)    
        
    else:
        pass


    if os.path.exists(datafolder) == False:
        os.mkdir(datafolder)
        print(f"LOG :- ✅ Folder For Storing Data Created Successfully \n ")
        signupval = True
        while signupval:
                print("❗ Running This Script For The First Time Sign Up As An Admin")
                os.chdir(datafolder)
            
                name = details.name().lower()
            
                if os.path.exists(name) == True:
                    print(f"❌ There was an account named {name} Try with another name.")
                    signupval = False    
                        
                else:    
                    uname = details.username().lower()
                    password = details.password()
                

                    secques = details.secques()
                
                    if os.path.exists(name) == False:
                        os.makedirs(name)
                        os.chdir(name)
                        with open(uname, "w") as x:
                            x.write(f"PASSWORD :- {password} \n")
                        with open(uname, "a") as x:
                            x.write(f"Question:- {secques[0]} \nAnswer:- {secques[1]}\n")
                            x.write("Admin\n")
                        print("✅ Admin Sign Up successful")
                        os.chdir(rootfolder)
                        signupval = False
                        
                        
    elif os.path.exists(datafolder) == True:
        pass