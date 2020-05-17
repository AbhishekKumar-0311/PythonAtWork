# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:59:58 2020

@author: abhi0
"""

"""
Write a class called Wordplay. It should have a field that holds a list of words. The user
of the class should pass the list of words they want to use to the class. There should be the
following methods:
• words_with_length(length) — returns a list of all the words of length length
• starts_with(s) — returns a list of all the words that start with s
• ends_with(s) — returns a list of all the words that end with s
• palindromes() — returns a list of all the palindromes in the list
• only(L) — returns a list of the words that contain only those letters in L
• avoids(L) — returns a list of the words that contain none of the letters in L
"""

class Wordplay:
    ''' This class is to wrap different actions done on string'''
    def __init__(self,lst=['a','b','c','d']):
        self.lst=lst
        
    def words_with_length(self,n):
        _tmp_lst=[]
        for i in self.lst:
            if len(i) == n:
                _tmp_lst.append(i)
        print("The list of word(s) with length {} is {}".format(n,_tmp_lst))
    
    def __words_with_length(self,n):
        _tmp_lst=[i for i in self.lst if len(i) == n]
        print("CMPRHNS: The list of word(s) with length {} is {}".format(n,_tmp_lst))
        
    def starts_with(self,char):
        # This checks only for 1st(one) character and is "WRONG"
        #_tmp_lst=[i for i in self.lst if i[0]==char]
        # This is Better as it takes care of Multicharacter 
        _tmp_lst=[i for i in self.lst if i[:len(char)]==char]
        print("CMPRHNS: The list of word(s) starting with character {} is {}".format(char,_tmp_lst))
    
    def ends_with(self,char):
        _tmp_lst=[i for i in self.lst if i[-1]==char]
        print("CMPRHNS: The list of word(s) ending with character {} is {}".format(char,_tmp_lst))
    
    def palindromes(self):
        _tmp_lst=[i for i in self.lst if i==''.join(reversed(i))]
        print("CMPRHNS: The list of Pallindrome word(s) is {}".format(_tmp_lst))
        
    def only(self,str):
        _tmp_lst=[]
        for i in self.lst:
            for x in str:
                if x in i:
                    _tmp_lst.append(i)
                    break
        print("The list of word(s) with characters from input string is {}".format(_tmp_lst))    

    def avoids(self,str):
        _tmp_lst=[]
        for i in self.lst:
            for x in str:
                if x not in i:
                    flag=1
                else:
                    flag=0
                    break
                # print(i,x,flag)
            # print(i,flag)
            if flag==1:
                _tmp_lst.append(i)
        print("The list of word(s) without characters from input string is {}".format(_tmp_lst))                
                
                
MyObj=Wordplay(['Mita','Abhishek','Vivek','MumuM','Arjun','Reshu','AnuYendu'])
MyObj.words_with_length(4)
MyObj._Wordplay__words_with_length(5) 
MyObj.starts_with('Mu')
MyObj.starts_with('M')
MyObj.ends_with('k')
MyObj.palindromes()
MyObj.only('MAY')
MyObj.avoids('kjM')
# dir(MyObj) 