import os

def name():
    return input("➡ Your Name : ")

def username():
    return input("➡ Your Username : ")
 
def password():
   valtrue = True
   while valtrue:
        password = input("➡ Your Password (Must Contain 8 Characters) : ")
        password = str(password)
        if len(password) != 8 and len(password) < 8:
            print("❌ Password Must Contain 8 Characters")
        else:
            valtrue = False
            return password
            
            
    
def secques():
    ques = int(input("➡ Which Security Question You want to answer? This Will Help You If you forgot your password or username \n\t Type :- \n\t ➡ 1 Your Petname\n\t ➡ 2 Your Grandmother's Name \n\t ➡ 3 Your School, College, University Name\n\t ➡ 4 You Want To Select Your Own Question \n"))
    
    if ques == 1:
        q1 = "Your Petname"
        return q1, input("➡ Your Pet Name : ").lower()
    elif ques == 2 :
        q2 = "Your Grandmother's Name"
        return q2, input ("➡ Your Grandmother's name : ").lower()
    elif ques == 3 :
        q3 = "Your School, College, University Name"
        return q3, input("➡ Your School, College, University Name : ").lower()
    elif ques == 4:
        q4 = input("➡ Enter Your Question : ")
        ans = input("➡ Enter Your answer : ")
        return q4, ans.lower()
        
    



