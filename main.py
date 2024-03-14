# Importing Modules
import os
import access.details as details
import setup.setup as setup
import access.signup as signup
import access.forgotpass as forgotpass
import access.forgotuname as forgotuname

import runpoll.createpoll as cpoll
import runpoll.chckpoll as chpoll
import runpoll.votepoll as vpoll
import runpoll.rmvpoll as rmvpoll
import runpoll.editpoll as epoll

datafolder = "data"
rootfolder = os.getcwd()
login = False
admin = False
logname = ""
logusername = ""

logincmd = ["1 Login ✅", "2 Sign Up 📜", "3 Forgot Password 🙄", "4 Forgot Username 🙄", "5 Exit ➡"]

setup.runsetup()


valTrue = True

while valTrue:
    
    cmd = int(input(f"❗ Type The Number Besides The Command To Execute The Command \n\t{logincmd[0]}\n\t{logincmd[1]} \n\t{logincmd[2]} \n\t{logincmd[3]} \n\t{logincmd[4]}\n"))
    
    if int(cmd) == 1:
                
        name = details.name().lower()
        uname = details.username().lower()
        os.chdir(datafolder)
        
        
        if os.path.exists(name):
                    password = details.password()
                    os.chdir(name)
                    with open(uname, "r") as x:
                        match = x.read()
                    if password in match:
                        print("✅ Login Successful")
                        logname = name
                        logusername = uname
                        login = True
                        os.chdir(rootfolder)
                        valTrue = False
                    else:
                        print("❌ Password doesn't matched try again")
                        os.chdir(rootfolder)
                                
        elif os.path.exists(name) == False:
                    print("❌ No Account was created with this name try again or sign up")
                    os.chdir(rootfolder)

    elif int(cmd) == 2:
        
        signup.signup()
   
    elif int(cmd) == 3:
        
        forgotpass.forgotpass()
        
    elif int(cmd) == 4:
        forgotuname.forgotuname()
    elif int(cmd) == 5:
        exit()
    else:
        print("❌ Unknown Command Choosen")

if login == True:
    os.chdir(datafolder)
    os.chdir(logname)
    with open(logusername, "r") as f:
        content = f.read()
    if "Admin" in content:
        admin = True
    else: pass
    
if admin == True:
    os.chdir(rootfolder)
    adcmd = ["1 Create Poll", "2 Check All Polls", "3 Vote A Poll", "4 Remove a poll", "5 Edit a poll", "6 Exit"]

    adcmdval = True

    while adcmdval:
        uscmd = int(input(f"❗ Type The Number Besides The Command To Execute The Command \n\t{adcmd[0]}\n\t{adcmd[1]} \n\t{adcmd[2]} \n\t{adcmd[3]} \n\t{adcmd[4]}\n\t{adcmd[5]}\n"))
        
        if uscmd == 1:
            cpoll.create()
            adcmdval = False
        elif uscmd == 2:
            chpoll.chkpolls()
            adcmdval= False
        elif uscmd == 3:
            vpoll.votepoll()
            adcmdval = False
        elif uscmd == 4:
            rmvpoll.rmvpoll()
            adcmdval = False
        elif uscmd == 5:
            epoll.editpoll()
            adcmdval = False  
        elif uscmd == 6:
            exit() 
        else:
            print("Unknown Command choosen")
            adcmdval = False 
else:
    os.chdir(rootfolder)
    adcmd = ["1 Check All Polls", "2 Vote A Poll","3 Exit"]

    adcmdval = True

    while adcmdval:
        uscmd = int(input(f"❗ Type The Number Besides The Command To Execute The Command \n\t{adcmd[0]}\n\t{adcmd[1]} \n\t{adcmd[2]}\n"))
        
        if uscmd == 1:
            chpoll.chkpolls()
            adcmdval= False
        elif uscmd == 2:
            vpoll.votepoll()
            adcmdval = False
        elif uscmd == 3:
            exit()
        else:
            print("Unknown Command choosen")
            adcmdval = False 