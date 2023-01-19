# -*- coding: utf-8 -*-
"""regularExp_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ggMwcwCdSZgu62PSfj20pGBfgPs77qI
"""

import re 
S = input()
s = S.lower()
C = input()
c = C.lower()
array = re.split(",", c)
output = main(s,array)
print(output)

from pickle import FALSE


def wordGroup(s):
  list1 = list()
  rep_letters = re.compile(r'([a-z])\1*')
  list2 = list()
  for rep_ltr in rep_letters.finditer(s):
      grp = rep_ltr.group()
      list2.append((grp[0], len(grp)))
  return list2

def main(s,array):
  word=wordGroup(s)
  ctr = 0
  for wrd in array: 
    flag = int() 
    if set(s) == set(wrd):
      for idx, i in enumerate(wordGroup(wrd)): 
        if i[1] < word[idx][1] and word[idx][1] >= 3:
          flag+=1
        elif i[1] == word[idx][1]:
           pass
        else: 
           flag = 0 
      if flag: 
          ctr+=1  
    return ctr