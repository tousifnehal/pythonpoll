# Importing Modules
import os
import setup.setup as setup

import access.details as details
import access.signup as signup
import access.forgotpass as forgotpass
import access.forgotuname as forgotuname

import runpoll.createpoll as cpoll
import runpoll.chckpoll as chpoll
import runpoll.votepoll as vpoll
import runpoll.rmvpoll as rmvpoll
import runpoll.editpoll as epoll
import runpoll.votestatus as vspoll

invalid_symbols = ['/', '\\', '?', '%', '*', ':', '"', '<', '>', '|', '.', '(', ')', '[', ']', '{', '}']

def contains_invalid_symbol(name):
    for symbol in invalid_symbols:
        if symbol in name:
            return True
    return False

datafolder = "data"
rootfolder = os.getcwd()
login = False
admin = False
logname = ""
logusername = ""


logincmd = ["Login ✅", "Sign Up 📜", "Forgot Password 🙄", "Forgot Username 🙄", "Exit ➡"]

setup.runsetup()


valTrue = True

while valTrue:
    
    for i in range(len(logincmd)):
        print(f"\t\t{i+1} {logincmd[i]}")
    cmd = int(input("❗ Type The Number Besides The Command To Execute The Command "))
    
    if int(cmd) == 1:
                
        chksymbol = True
        while chksymbol:
                    name = details.name()
                    if contains_invalid_symbol(name):
                        print("Your Name Can't Contain Any Symbols TRY Again")
                    else: chksymbol = False
        chksymbol = True
        while chksymbol:
                        uname = details.username()
                        if contains_invalid_symbol(uname):
                            print("Your Username Can't Contain Any Symbols TRY Again")
                        else: chksymbol = False   
        os.chdir(rootfolder)
        os.chdir(datafolder)
        
        
        if os.path.exists(name):
                    if os.path.exists(uname):
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
                    else:
                        print("Username Not Found. Try again")
                                
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
    
os.chdir(rootfolder)


allcmd =  ["Create Poll [ADMIN]", "Check All Polls", "Vote A Poll", "Remove a poll [ADMIN]", "Edit a poll [ADMIN]","Check a poll's vote status", "Exit"] 


cmdloop = True

while cmdloop:
    for i in range(len(allcmd)):
        print(f"\t\t{i+1} {allcmd[i]}")
    uscmd = int(input("❗ Type The Number Besides The Command To Execute The Command "))
    if uscmd == 1:
        if admin:
            cpoll.create()
            # cmdloop = False
        else:
            print("You are not an Admin")
          
    elif uscmd == 2:
         chpoll.chkpolls()
    elif uscmd == 3:
        vpoll.votepoll()
        # cmdloop = False
    elif uscmd == 4:
        if admin:
            rmvpoll.rmvpoll()
            # cmdloop = False
        else:
            print("You are not an admin")
    elif uscmd == 5:
        if admin:
            epoll.editpoll()
            # cmdloop = False
        else:
            print("You are not an admin")
    elif uscmd == 6:
        vspoll.votestatus()
    elif uscmd == 7:
        print("Exiting Now")
        exit()
    else:
        print("Unknown Command Choosen")

