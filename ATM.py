l=0
class ATM:
    def __init__(self):
        print("welcome to atm")
    def add(self):
        a=input("enter amount to be added")
        self.l=self.l+int(a)
        print(f"total amount is {self.l}")
    def withdraw(self):
        a=input("enter amount to be withdrawn")
        self.l=self.l-int(a)
        print(f"left amount is {self.l}")
    def check(self):
        print(f"balance available is {self.l}")
    def tran(self):
        pass

while True:
    t=input("enter your name")
    t=ATM()
    A=input("enter what you want, deposit,withdraw,checkbalance,transactions")
    if A.lower()=="deposit":
        t.add()
    elif A.lower()=="withdraw":
        t.withdraw()
    elif A.lower()=="check":
        t.check()
    elif A.lower()=="transactions":
        t.tran()








    
    
