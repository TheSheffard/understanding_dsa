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


print(search1(numbers, 20))