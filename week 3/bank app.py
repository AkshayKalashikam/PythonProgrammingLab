def credit (bal,value):
    bal = bal + value
    return bal
    
def debit (bal,value):  
    bal = value - bal
    return bal
    
def show_bal(bal):
    print (bal)
    
bal = int(input("enter the amount:")) 
amount = int(input("enter the amount to be credited or debited :"))
sys = int(input("pres1 to credit \n press2 to debit :"))    
if(sys==1):
   bal = credit(amount,bal)
   show_bal(bal)
if(sys==2):
   bal = debit(amount,bal)
   show_bal(bal)
