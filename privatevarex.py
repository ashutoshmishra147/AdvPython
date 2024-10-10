# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:26:53 2023

@author: u398142
"""

class JustCounter:
   __secretCount = 0;
  
   def __count(self):
      self.__secretCount += 1;
      print( self.__secretCount);



counter = JustCounter();
counter.__count();
counter.__count();

#counter.count();
#counter.count();
#counter.count();
#print(counter.__secretCount)
