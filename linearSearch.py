numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def search_Array(arr, target):
  """Linear Search Algorithm:

  Iterates through each element in the collection one by one from start to end.
  - Best Case: O(1) if the target is the first element.
  - Worst/Average Case: O(n) where n is the number of elements (it checks
  every single item if the target is at the end or missing).
  """
  
  """"
  How to check how many steps it will take for this to run 
  """
  steps = 0
  for i in arr:
    steps +=1 
    if i == target:
      print(f"The steps taken {steps}")
      return i

  return "Target not found"


# print(search_Array(numbers, 9))

# Questions

""""
Question 1: Find a number

"""

ques1 = [4, 7, 2, 9, 5]
def Find_a_number(arr):
  target = 9
  
  
  for i in range(len(arr)):
    
    if ques1[i] == target:
      
      return i
  return -1


# print(Find_a_number(ques1)) 

"""
Question 2: Check whether a number exists
""" 

ques2 = [10, 20, 30, 40]


"""
Given a list of names and a target name, return the index of the name if it exists, 
or -1 otherwise. Treat uppercase and lowercase letters as different.
"""


def check_if_number_exist(arr):
  
  target = 25
  
  for i in range(len(arr)):
    
    if arr[i] == target:
      return True

  return False





names = ["Ada", "John", "Mary", "David"]


def check_name(arr):
  target = "Mary"
  
  for i in range(len(arr)):
    
    if arr[i] == target:
      
      return i
    
  return -1

# print(check_name(names))
  
  
  
  
"""
Question 4: Find the first occurrence

Given a list that may contain duplicate numbers, return the index of the first occurrence of the target.
"""


ques4 = [3, 8, 5, 8, 2, 8]
# Expected output: 1


def first_occurrence(arr):
  
  target = 8
  
  
  for i in range(len(arr)):
    
    if arr[i] == target:
      
      return  i
  
# print(first_occurrence(ques4))


""""
Question 5: Count occurrences

Given a list and a target, count how many times the target appears. Return 0 if it doesn't appear.
"""

ques5 = [2, 4, 2, 7, 2, 9, 4]
def count_occurrences(arr):
 
  target = 2
  occurrence = 0
  
  for i in range(len(arr)):
    
    if arr[i] == target:
        occurrence += 1
  return occurrence

 
# print(count_occurrences(ques5))


""""
Question 6: Find the last occurrence

Given a list and a target, return the index of its last occurrence, or -1 if it doesn't exist.

# Expected output: 5

"""

ques6 = [6, 3, 8, 3, 9, 3]

def find_last_occurrence(arr):
  
  target = 3
   
  last = -1
  
  
  for i in range(len(arr)):
    
    
    if arr[i] == target:
      last = i
      
  return last

# print(find_last_occurrence(ques6))


""""
Question 7: Find the first even number

Given a list of integers, return the index of the first even number. If there is no even number, return -1.

# Expected output: 3
"""

ques7 = [7, 9, 11, 14, 18]

def first_even_number(arr):
  
  for i in range(len(arr)):
    
    if arr[i] %  2 == 0:
      
      return i
    
  return -1


# print(first_even_number(ques7))



""""
Question 8: Find all occurrences

Given a list and a target, return a list containing every index where the target appears. If the target isn't present, return an empty list.

# Expected output: [0, 2, 4]
"""


ques8 = [5, 2, 5, 7, 5, 1]


def find_all_occurrence(arr):
  target = 5

  new = []
  
  
  for i in range(len(arr)):
    
    if arr[i] == target:
      
      new.append(i)
      
  return new


# print(find_all_occurrence(ques8))


"""
Question 9: Search in an empty list

Write a linear search function that works correctly even if the input list is empty.
# Expected output: -1

"""


ques9 = []

  
def search_empty(arr):
    
  target = 10
  
  if len(arr) == 0: return 0 
  
  
  for i in range(len(arr)):
    
    
    if arr[i] == target:
      
      return i
    
  return -1


# print(search_empty(ques9))


""""
Question 10: Find the first number greater than a target

Given a list of integers and a target, return the index of the first number strictly greater than the target. Return -1 if no such number exists.
# Expected output: 2

"""
  
  
ques10 = [2, 5, 8, 3, 10]


def find_first_highest(arr):
  
  target = 6
  
  for i in range(len(arr)):
    
    if arr[i] >target:
      
      return i
    
  return -1
  

# print(find_first_highest(ques10))
  
  
  
  
  
    
  
      
    



