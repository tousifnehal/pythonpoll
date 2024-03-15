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


logincmd = ["1 Login ✅", "2 Sign Up 📜", "3 Forgot Password 🙄", "4 Forgot Username 🙄", "5 Exit ➡"]

setup.runsetup()


valTrue = True

while valTrue:
    
    cmd = int(input(f"❗ Type The Number Besides The Command To Execute The Command \n\t{logincmd[0]}\n\t{logincmd[1]} \n\t{logincmd[2]} \n\t{logincmd[3]} \n\t{logincmd[4]}\n"))
    
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
                        valTrue = False
                                
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

allcmd =  ["1 Create Poll [ADMIN]", "2 Check All Polls", "3 Vote A Poll", "4 Remove a poll [ADMIN]", "5 Edit a poll [ADMIN]","6 Check a poll's vote status", "7 Exit"] 


cmdloop = True

while cmdloop:
    uscmd = int(input(f"❗ Type The Number Besides The Command To Execute The Command \n\t{allcmd[0]}\n\t{allcmd[1]} \n\t{allcmd[2]} \n\t{allcmd[3]} \n\t{allcmd[4]}\n\t{allcmd[5]}\n\t{allcmd[6]}\n"))
    
    if uscmd == 1:
        if admin:
            cpoll.create()
            cmdloop = False
        else:
            print("You are not an Admin")
          
    elif uscmd == 2:
         chpoll.chkpolls()
    elif uscmd == 3:
        vpoll.votepoll()
        cmdloop = False
    elif uscmd == 4:
        if admin:
            rmvpoll.rmvpoll()
            cmdloop = False
        else:
            print("You are not an admin")
    elif uscmd == 5:
        if admin:
            epoll.editpoll()
            cmdloop = False
        else:
            print("You are not an admin")
    elif uscmd == 6:
        vspoll.votestatus()
    elif uscmd == 7:
        print("Exiting Now")
        exit()
    else:
        print("Unknown Command Choosen")

