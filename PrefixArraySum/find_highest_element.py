# Example Problem:
# Consider an array of size N with all initial values as 0. Perform the given ‘m’ add operations from index ‘a’ to ‘b’ and evaluate the highest element in the array. An add operation adds 100 to all the elements from a to b (both inclusive).
#
# Example:
#
# Input: n = 5, m = 3
# a = 2, b = 4.
# a = 1, b = 3.
# a = 1, b = 2.
# Output: 300
# Explanation:
# After I operation – A[] = {0, 100, 100, 100, 0}
# After II operation – A[] = {100, 200, 200, 100, 0}
# After III operation – A[] = {200, 300, 200, 100, 0}
# Highest element: 300

# solution approach -
#
# The efficient approach is to use Prefix Sum Array
#
# Follow the given steps to solve the problem:
#
# Run a loop for ‘m‘ times, inputting ‘a‘ and ‘b‘. Add 100 at index ‘a-1‘ and subtract 100 from index ‘b‘. After
# completion of ‘m‘ operations, compute the prefix sum array. Scan the largest element and we’re done. Explanation:
# We added 100 at ‘a’ because this will add 100 to all elements while taking the prefix sum array. Subtracting 100
# from ‘b+1’ will reverse the changes made by adding 100 to elements from ‘b’ onward.


def find_highest(m, indexess):
    arr = [0] * 5
    for i in range(m):
        arr[indexess[i][0] - 1] += 100
        arr[indexess[i][1]] -= 100
    maxx = arr[0]
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
        if arr[i] > maxx:
            maxx = arr[i]
    return maxx


if __name__ == "__main__":
    m = 3
    indexes = [[2, 4], [1, 3], [1, 2]]
    maxx = find_highest(m, indexes)
    print("max ", maxx)
