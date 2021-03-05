#1. Write a Python program to calculate the length of a string. Go to the editor

#rumpShaker = 'All I want to do is a boom boom boom and a zoom zoom'
#
#print(len(rumpShaker))

#output - 52
#no assistance

#2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
#website = 'google.com'
#count = {}
#for x in website:
#    count.setdefault(x, 0)
#    count[x] = count[x] + 1

#print(count)
#output {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#needed to refer to book to finish

#6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor

#def add_string(str1):
#    length = len(str1)
#
#    if length > 2:
#        if str1[-3:] == 'ing':
#            str1 += 'ly'
#        else:
#            str1 += 'ing'
#    
#    return str1
#print(add_string('ab'))
#print(add_string('abc'))
#print(add_string('string'))   

#output ab
#abcing
#stringly
#needed lots of help with this one. Solution

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#def not_poor(str1):
#  snot = str1.find('not')
#  spoor = str1.find('poor')
  

#  if spoor > snot and snot>0 and spoor>0:
#    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
#    return str1
#  else:
#    return str1
#print(not_poor('The lyrics is not that poor!'))
#print(not_poor('The lyrics is poor!'))

#output 
#The lyrics is good!
#The lyrics is poor!

# I was totally confused on how to do this.Solution

#8. Write a Python function that takes a list of words and returns the longest word and the length of the longest one.
#def long_word(word_list):
#    word_length = []
#    for x in word_list:
#        word_length.append((len(x), x))
#    word_length.sort()
#    return word_length[-1][0], word_length[-1][1]
#result = long_word(["Super","Califragilistic","Expealadotious"])
#print("\nLongest word: ",result[1])
#print("Length of longest word: ",result[0])

#output 
#Longest word:  Califragilistic
#Length of longest word:  15

#Started ok without but ultimately needed to check the solution

#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

#hello = 'Hello World!'

#print(hello[-1] + hello[1:-1] + hello[:1])

#output - 
# !ello WorldH
# referred to book 

#61. Write a Python program to remove duplicate characters of a given string. 

#def remove_zeros_from_ip(ip_add):
#  new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
#  return new_ip_add ;
#
#print(remove_zeros_from_ip("010.010.010.011"))
#
#output - 10.10.10.11

#https://stackoverflow.com/questions/9841303/removing-duplicate-characters-from-a-string

# Exercise 4: Arrange string characters such that lowercase letters should come first
#text = "PyNaTive"
#lower = []
#upper = []
#for char in text:
#    if char.islower():
#        lower.append(char)
#    else:
#        upper.append(char)
#caseSort = ''.join(lower + upper)
#print(caseSort)

#output
#yaivePNT
#https://stackoverflow.com/questions/19191980/how-do-i-organize-lower-and-upper-case-words-in-python

#Exercise 8: Find all occurrences of “USA” in a given string ignoring the case

#str1 = "Welcome to USA. usa awesome, isn't it?"
#sub = "USA"
#count = 1
 

#if sub.lower() in str1.lower(): 
#    count = count + 1
  
  
#print (" " +  str(count)) 
#output 2

#https://www.geeksforgeeks.org/python-string-find/

#Exercise 14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print([x for x in str_list if x ])