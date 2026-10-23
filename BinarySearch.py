numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def search1(arr, target):
  """Binary Search Algorithm:

  Repeatedly divides the search interval in half.
  - Best Case: O(1) if the target is right in the middle on the first try.
  - Worst/Average Case: O(log n) because the search space is cut in half every step.
  """
  steps = 0
  left = 0
  right = len(arr) - 1

  while left <= right:
    steps += 1
    mid = (left + right) // 2

    if arr[mid] == target:
      print(f"The steps taken: {steps}")
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  print(f"The steps taken: {steps}")
  return -1


# print(search1(numbers, 20))



""""
Question 1 — Basic binary search
Write a Python function that searches for a target in a sorted list and returns its index. If the target doesn't exist, return -1.

"""

ques1 = [3, 7, 11, 15, 19, 23, 27]

def basic_binary(arr):
  
  target = 19
  
  left  = 0
  right = len(arr) - 1 
  
  
  while left <= right:
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
      
      return mid
    
    elif arr[mid] > target:
      
      right = mid - 1

    else:

      left = mid + 1
      
  return -1


# print(basic_binary(ques1))



""""
Question 2 — Search Insert Position

Given a sorted list of distinct integers, return the index of the target if it exists. Otherwise, return the index where it should be inserted to keep the list sorted.
"""

ques2 = [1, 3, 5, 6]
target2 = 2

# Expected output: 1


def Search_insert_position(arr, target):
  
  left = 0
  right = len(arr) - 1

  while left <= right:
      mid = (left + right) // 2

      if arr[mid] == target:
        return mid
      elif arr[mid] > target:
        
        right = mid - 1
      else:
        left = mid + 1

  return left


# print(Search_insert_position(ques2, target2))
  
    
    
  
""""
Question 3 — Sqrt(x)

Given a non-negative integer x, return its square root rounded down to the nearest integer. Do not use a built-in square-root function or exponentiation.

"""

ques3 = 8

def check_for_sqrt(number):
    left = 0
    right = number
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == number:
            return mid

        elif mid * mid > number:
            right = mid - 1

        else:
            answer = mid
            left = mid + 1

    return answer

# print(check_for_sqrt(ques3))


""""
Question 4: Valid Perfect Square
Given a positive integer num, return True if it is a perfect square, otherwise return False.
"""

ques4 = 16

# Expected output: True


def valid_perfect_square(x):
  
  left  = 0
  right = x
  
  
  while left <= right:
    
    mid  = (left + right ) // 2
    
    if mid * mid == x:
      return True
    
    elif mid * mid > x:
      right = mid - 1
      
    else:
      left = mid + 1
      
  return False


# print(valid_perfect_square(ques4))

  
""""
Question 5  Guess Number Higher or Lower

I'm thinking of a number between 1 and n. Your task is to guess it using binary search.
"""

ques5 = 10
target5 = 7

def guess_number(n, target):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        if mid == target:
          return mid
        
        elif mid > target:
          right = mid - 1
        
        else:
          left = mid + 1
          
    return  -1
  
  
# print(guess_number(ques5, target5))



""""
Question 6  First Bad Version

Imagine an application has versions numbered from 1 to n. At some point, a version becomes faulty, and every version after it is faulty too.
"""


ques6 = 5
first_bad6 = 4

def first_bad_version(n, first_bad):
    left = 1
    right = n
    answer = - 1

    while left <= right:
        mid = (left + right) // 2
          
        if mid > first_bad:
          answer = mid 
          right = mid - 1
          
        else:
          answer = mid 
          left = mid + 1
          
    return answer
  
print(first_bad_version(ques6, first_bad6))