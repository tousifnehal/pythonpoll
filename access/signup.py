import os 
import access.details as details

datafolder = "data"

def signup():
    signupval = True
    while signupval:
                
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
                            x.write(f"Question:- {secques[0]} \n{secques[1]}\n")
                        print("✅ Sign Up successful")
                        signupval = False