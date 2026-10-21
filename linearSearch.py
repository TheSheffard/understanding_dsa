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


print(search_Array(numbers, 9))



