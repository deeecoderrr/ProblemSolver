
# Problem : Need to find the chain of 1's' that has maximum 1 in a chain. after 1 swap between any 1 pair of zero and one

# [1,0,1,1,1,0,0,1,1,0,1,0,1,1]
# [1,0,1,2,3,0,0,1,2,0,1,0,1,2]
# [1,0,3,2,1,0,0,2,1,0,1,0,2,1]

# solution :
# 1) we will create two arrays for storing summation as we move forward each index and backward each index for the seond array,
# we will increase the count of summation if the element at that index is 1 otherwise reset the count to 0 if we encounter 0
# 2) in the same way we will create another array and do the same thing from backside of array
# 3) then for each 0 in the main array we will add the l[i-1] and r[i+1], to see the total length of 1 ,
# if we swap that 0 with 1 , and find the max , by checking the length where ever 0 is encountered
# we add add 1 , if length of the 1 is less than the total 1's present in the array,


a = [1,0,1,1,1,0,0,1,1,0,1,0,1,1]
# a = [1,1,1,0,1,1,1,0,0]
n = len(a)
l = [0] * n
r = [0] * n


l[0] = 1 if a[0] == 1 else 0
r[n-1] = 1 if a[n-1] == 1 else 0
ones_count = 0
for i in range(1, n):
    if a[i] == 1:
        l[i] = l[i-1] + 1
    else:
        l[i] = 0

    if a[n-1-i] == 1:
        r[n-1-i] = r[n-i] + 1
    else:
        r[n-1-i] = 0

for i in range(0,n):
    if a[i] == 1:
        ones_count += 1

maxx = 0

for i in range(0,n):
    if a[i] == 0:
        ones_total = ((0 if i == 0 else l[i-1]) + (0 if i == n-1 else r[i+1]))
        if maxx < ones_total:
            maxx = ones_total


if maxx < ones_count:
    maxx += 1
print(maxx)


