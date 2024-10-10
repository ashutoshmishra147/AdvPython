# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:47:40 2023

@author: u398142
"""

class Base:
   ''' def __init__(self):
          # Protected member
        self.a = 2'''
        
def add(a,b,c=10):
        print("the total is ",(a+b+c));
        return a+b+c;
        
add(4,5)
add(3,6,9)
        
'''  # Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ", 
              self.a)
          # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self.a)
  
  
obj1 = Derived()
obj2 = Base()
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1.a)
  
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2.a)'''
