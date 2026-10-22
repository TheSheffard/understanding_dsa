# Selection Sort Algorithm:
# Divides the input list into two parts: a sorted sublist of items built up
# from left to right and an unsorted sublist of remaining items.
# It repeatedly finds the minimum element from the unsorted sublist,
# swaps it with the leftmost unsorted element, and advances the sublist boundary.
# - Time Complexity: O(n^2) for Worst, Average, and Best cases.

array = [6, 5, 2, 8, 9, 4]

print(f"Before sorting {array}")
print()


def sort(arr):
  size = len(arr)
  temp = 0

  for i in range(size - 1):
    minIndex = i

    for j in range(i + 1, size):
      if arr[minIndex] > arr[j]:
        minIndex = j

    temp = arr[minIndex]
    arr[minIndex] = arr[i]
    arr[i] = temp


sort(array)

print(f"After sorting {array}")