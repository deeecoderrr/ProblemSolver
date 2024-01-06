# Problem: Given a array of size n , filled with elements, that may repeat. Find out the majaority element if present. A majority element is that
# which is present in the array atleast (n/2)+1 times or more than (n/2) times
#
# Solution:
# 1) with sorting it can be done in nlogn
# 2) better way is, start from the first index and traverse till last,
# 3) at each iteration , check if count == 0 , then set that element as majority element and increase the count by 1
# 4) if the element is equal to the majority element , increase the count of element by 1
# 5) if the element is not the majority element , reduce the count by -1
# 6) All this will take o(n) time
# 7) then to conifrm if this is the majority element , run a loop again to check how many times that ME has repaeated itself in the array,
# if its occurence in more than or equal go (n/2)+ 1 times, then thats the majority element , else no mE presnt
# time complexity - o(2n)
#
# code---------------->


def find_majority_element(arr_list, size_n):
    maj_ele = arr_list[0]
    count = 0
    for i in range(0, size_n):
        if count == 0:
            maj_ele = arr_list[i]
            count += 1
        if arr_list[i] != maj_ele:
            count -= 1

        if arr_list[i] == maj_ele:
            count += 1

    count_check = 0
    for i in range(0, size_n):
        if arr_list[i] == maj_ele:
            count_check += 1

    import math

    if count_check >= (math.floor(size_n / 2) + 1):
        print("Majority element is ", maj_ele)
    else:
        print("No Majority element.")


if __name__ == "__main__":
    size_n = int(input("Enter the size"))
    arr_list = list(map(int, input("Enter space separated values").split()))

    find_majority_element(arr_list, size_n)
