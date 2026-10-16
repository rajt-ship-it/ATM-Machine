import os
import re
if not os.path.exists("python all works"):#here we are creating a folder using os module and if already exist then use it
    os.mkdir("python all works")
file="python all works/ATM.txt"#here we have created a file in that folder if not exist then it is formed automatically
f=open(file,'r')
text=f.read()
import os
print("File is formed here:", os.path.abspath("python all works/ATM.txt"))
li=text.splitlines()#isse jo bhi pehle ka data hai vo list mein convert hojayega with /n operator wala matlab second line wale next ellemnt of list
class ATM:
    def __init__(self,name):
        self.user_name=name
        self.l=5000
        print("welcome to atm")
        self.list=[]
        # self.list.append(li) ##look this will create an error because append statement will add li(which is a list) as list only so now it will become nested list which is a problem becuse when for loop will run that will create an issue when adding a new string to a nested list
        self.list.extend(li)#yeh list ke ander nahi add karta yeh banni banayi list mein ange add karta hai
    def save_info(self,input,totalamount): #note here 2 input i am taking one is for updating the transaction and second is for updating total amount left in user account 
        with open("python all works/ATM.txt",'w') as f:
            for i in self.list:#yeh bas list ki information bapis notepad mein dalne keliye kiya hai becauise write karne se notepad ka purana data hatjata hai issliye sabse pehle hamne list banayi thi purane data ki
                f.write(i+"\n")
            f.write(input + "\n")
            f.write(totalamount +"\n")
    def add(self):
        a=int(input("enter amount to be added"))
        if a<=0:
            print("amount must be greater then 0")
        self.l=self.l+int(a)
        print(f"total amount is {self.l}")
        texttoadd=f"name :-{self.user_name} added amount:-{a}"
        total=f"name :-{self.user_name} total amount:-{self.l}"
                # self.list.append(texttoadd)
        # self.list.append(texttoadd)#acha yaha yeh bhi karsakte the per yaha extend yaha nahi lagta warna problem hojati because extend ek string ko add kardeta or fir jab for loop chalta toh vo string hi ek ek letter se tutjati
        self.save_info(texttoadd,total)
    def withdraw(self):
        a=input("enter amount to be withdrawn")
        self.l=self.l-int(a)
        if self.l>=0:
            print(f"left amount is {self.l}")
            texttoadd=f"name :-{self.user_name} removed amount:-{a}"
            total=f"name :-{self.user_name} total amount:-{self.l}"
            #self.list.extend(texttoadd) yaha append kaam karta per extend lagane se string ke ek ek letters add hojate or fir for loop wale mein ek ek letter print hota transactions mein.. @@ by the way meine toh yeh sab use nahi kiya direct function mein hi input dediya iosse mujhe list mein add karne ki naubat hi nahi aayi 
            self.save_info(texttoadd,total)
        else:
            print("insufficient balance")
    def check(self):
        print(f"balance available is {self.l}")
    def tran(self):
        file=open("python all works/ATM.txt","r")
        z=file.read()
        print(z)

# while True:
#     t=input("enter your name")
#     k=ATM(t)
#     A=input("enter what you want, deposit,withdraw,check,transactions")
#     if A.lower()=="deposit":
#         k.add()
#     elif A.lower()=="withdraw":
#         k.withdraw()
#     elif A.lower()=="check":
#         k.check()
#     elif A.lower()=="transactions":
#         k.tran()
#iss while loop mein loop holes hain .like if you deposited or withdraw when it will execute again it will create a new class with earlier value of 5000 means everything restarts.also here if we put class out then other users cant be formed then only one user will work so for all these issue we use loop inside loop
while True:
    name=input("enter your name or type 'quit' to logout")
    if name.lower()=="quit":
        break
    user=ATM(name)
    while True:
        A=input("enter what you want, deposit,withdraw,check,transactions,exit")
        if A.lower()=="deposit":
            user.add()
        elif A.lower()=="withdraw":
            user.withdraw()
        elif A.lower()=="check":
            user.check()
        elif A.lower()=="transactions":
            user.tran()
        elif A.lower()=="exit":
            break
        else:
            print("invalid option try again")
# now finally everything was working fine but there was an issue here if i add or withdraw then my transaction history will be saved but when i will come back then transaction histpory can be fetched but my money will agian start from 5000 only not from my last transactions
#so sol i thought is i will have to extract complete data of notepad and in that i have to get that first word(name ) and last number(that is total amount left)
#text="Raj total amount:-6000" NOTE :- number=re.findall(r"\d+",text) here module required will be "re" NOTE :- import re










    
    
