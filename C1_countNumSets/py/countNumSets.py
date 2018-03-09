"""
In order to have a valid set, the sum of each two numbers in the set should be 
greater than the third number. It means that; if the sum of any two numbers in a 
set is less than or equal to the third number, the condition will NOT be satisfied; 
therefore we cannot count that set as a valid set. i.e. [6, 4, 2] 

Sorting the list in ascending order would make our program more efficient;
if we have a sorted list such as [17, 14, 10, 9, 8, 5, 2, 1] and start from the 
first number which will initially be the largest number, and set our second 
number to initially be the one next to our largest number, then we would need to 
find the smallest number that would satisfy the condition: 
    largest < mid + smallest 
That's when having the list in ascending order will be beneficial, we will be able
to start searching for the smallest number that will satisfy the condition, and 
once we find the rightmost one that would satisfy the condition, all the other ones 
between the middle and rightmost number would be satisfying the condition as well, 
and we can directly add the total count of them to our valid set count.

To refer our example array, the initial values will be:
    largest: 17
    mid: 14
    smallest: 1

For the first iteration: 
    17 < 15 (14 + 1)    ---> does NOT satisfy, we will try the second smallest:
    17 < 16 (14 + 2)    ---> does NOT satisfy, we will try the third smallest:
    17 < 19 (14 + 5)    ---> satisfies!

We found the smallest number that satisfies our condition, which will also mean
that, as all the other numbers that are in the middle between our mid number and 
the left of our smallest satisfying number are larger than our smallest number,
so they would automatically satisfy our condition as well.
(Such that: 17 < 22 (14 + 8) and 17 < 23 (14 + 9) and 17 < 24 (14 + 10))

From there, we can find the count of these satisfying numbers by simply subtracting 
the indices of our mid and smallest numbers:
    index mid: 1 (for 14)
    index smallest: 5 (for 5)
    Total count for this iteration: 5 - 1 = 4 (10, 9, 8, 5)

After this step, we will need to reset our mid number to right by one so the next 
iteration will be finding: 17 < 10 + ?
    .
    .
    .
After exhausting all possible iterations with the largest number, all the possible
mid numbers until the one before the end of the list, we will reset our largest 
number and do the same process of finding the index of the smallest for our second 
largest number and the mid numbers in between. (Such that: 14 < 10 + ?)
    .
    .
    .
In the end of this operation, we will have the total number of possible sets.
"""

def count_num_sets(arr):
  """
  Return the number of sets of three in a list such that 
  the sum of each two element in the set is greater than the third one
  :param arr: List[int]
  :return: int
  """
  # If there are less than three numbers in the list, we should return 0
  if len(arr) < 3:
    return 0
  arr.sort(reverse = True)
  num_sets = 0  
  for i in range(len(arr) - 2):
    j, k = i + 1, len(arr) - 1
    while j < k:
      if arr[i] < arr[j] + arr[k]:
        num_sets += k - j
        j += 1
      else:
        k -= 1
  return num_sets
