class Money:
    def __init__(self,dollars=0,cents=0):
        self.__dollars=dollars
        self.__cents=cents
    
    def set_dollars(self,dollars):
        self.__dollars=dollars
        
    def get_dollars(self):
        return self.__dollars
    
    def set_cents(self,cents):
        self.__cents=cents
        
    def get_cents(self):
        return self.__cents
    
    def __add__(self,another_money):
        added_cents=self.__cents+another_money.__cents
        added_dollars=self.__dollars+another_money.__dollars
        if added_cents>100:
            added_dollars+=1
            added_cents=added_cents%100
        return Money(added_dollars,added_cents)
    
    def __sub__(self,another_money):
        added_cents=self.__cents-another_money.__cents
        added_dollars=self.__dollars-another_money.__dollars
        if added_cents<0:
            added_dollars-=1
            added_cents=100+added_cents
        if added_cents<10:
                added_cents='0'+str(added_cents)
        return Money(added_dollars,added_cents)
    
    def __eq__(self,another_money):
        if self.__cents==another_money.__cents and self.__dollars==another_money.__dollars:
            return True
        else:
            return False
    
    def __gt__(self,another_money):
        if self.__dollars>another_money.__dollars:
            return True
        elif self.__dollars==another_money.__dollars and self.__cents>another_money.__cents:
            return True
        else:
            return False
        
    def __ge__(self,another_money):
        if self.__dollars>=another_money.__dollars:
            return True
        elif self.__dollars==another_money.__dollars and self.__cents>=another_money.__cents:
            return True
        else:
            return False
    
    def __lt__(self,another_money):
        if self.__dollars<another_money.__dollars:
            return True
        elif self.__dollars==another_money.__dollars and self.__cents<another_money.__cents:
            return True
        else:
            return False
        
    def __le__(self,another_money):
        if self.__dollars<=another_money.__dollars:
            return True
        elif self.__dollars==another_money.__dollars and self.__cents<=another_money.__cents:
            return True
        else:
            return False
    
    def __str__(self):
        return '$'+str(self.__dollars)+'.'+str(self.__cents)

def main():
    m1=Money()
    print("money1 object: ",m1)
    m1.set_dollars(9)
    m1.set_cents(99)
    print("money1 object: ",m1)
    print("money1 object dollars: ",m1.get_dollars())
    print("money1 object cents: ",m1.get_cents())
    m2=Money(2,56)
    print("money2 object: ",m2)
    print('adding two money objects: ',m1+m2)
    print('subtracting two money objects: ',m1-m2)
    print('are the two money objects equal: ',m1==m2)
    print('Is money1 object greater than money2 object: ',m1>m2)
    print('Is money1 object greater than equal to money2 object: ',m1>=m2)
    print('Is money1 object less than money2 object: ',m1<m2)
    print('Is money1 object less than equal to money2 object: ',m1<=m2)
    
main()