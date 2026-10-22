array = [3, 2, 8, 9, 7, 5, 4]

print(f"Array before sorting {array}")
print("")


def sort(arr):
  """Bubble Sort Algorithm:

  Repeatedly steps through the list, compares adjacent elements, 
  and swaps them if they are in the wrong order.
  - Best Case: O(n) if the array is already sorted.
  - Worst/Average Case: O(n^2) because of the nested loops.
  """
  steps = 0
  temp = 0

  for index in range(len(arr)):
    for i in range(len(arr) - index - 1):
      # Count every time the algorithm compares two numbers
      steps += 1

      if arr[i] > arr[i + 1]:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp

  print(f"The steps taken: {steps}")


sort(array)
print("")
print(f"Array after sorting {array}")