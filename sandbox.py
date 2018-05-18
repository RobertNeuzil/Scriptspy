

def givenum(n):
    if n > 2 and n < 6 and n % 2 == 0:
        print ("Not Weird")
        
    elif n > 6 and n < 20 and n % 2 == 0:
        print ("Weird")
        
    elif n > 20 and n < 100 and n % 2 == 0:
            print ("Not Weird")
            
    elif n % 2 != 0:
        print ("Weird")
    
    else:
        pass
givenum(3)