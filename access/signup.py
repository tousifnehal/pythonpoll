import os 
import access.details as details

invalid_symbols = ['/', '\\', '?', '%', '*', ':', '"', '<', '>', '|', '.', '(', ')', '[', ']', '{', '}']

def contains_invalid_symbol(name):
    for symbol in invalid_symbols:
        if symbol in name:
            return True
    return False

datafolder = "data"






def signup():
    signupval = True
    while signupval:
                os.chdir(datafolder)

                chksymbol = True
                while chksymbol:
                    name = details.name()
                    if contains_invalid_symbol(name):
                        print("Your Name Can't Contain Any Symbols TRY Again")
                    else: chksymbol = False
                        
                if os.path.exists(name) == True:
                    print(f"❌ There was an account named {name} Try with another name.")
                    signupval = False    
                        
                else:
                    chksymbol = True 
                    while chksymbol:
                        uname = details.username()
                        if contains_invalid_symbol(uname):
                            print("Your Username Can't Contain Any Symbols TRY Again")
                        else: chksymbol = False   
                    
                    password = details.password()
                

                    secques = details.secques()
                
                    if os.path.exists(name) == False:
                        os.makedirs(name)
                        os.chdir(name)
                        with open(uname, "w") as x:
                            x.write(f"PASSWORD :- {password} \n")
                        with open(uname, "a") as x:
                            x.write(f"Question:- {secques[0]} \n{secques[1]}\n")
                        censored = "*" * len(password)
                        print("✅ Sign Up successful")
                        print(f"Your name : {name}, Username : {uname}, Password : {censored}, Question:- {secques[0]}")
                        signupval = False