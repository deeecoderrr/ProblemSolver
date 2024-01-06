# Problem: we have to find a element which occurs more than n/3 times
# soln:
# 1)traverse the array and find unqiue set of three elements , if found then reduce the count of both the contenders by 1
# 2) keep c1 and c2 as two contenders , and assign them a value if the value of that contender is not equal to the other contender and count is 0
# 3) at the end , both or one of the contender bvalue will be greater that 0,
# 4) travserse the array agains and check which one of them ( if both non ero) is present more than n/3 + 1 times is the answer

# Note : if we need to find a element which happens more than n/k times than ,
# we need to main k-1 variables iterating those will increase the time complexity so hashing will be good in that cas


def find_majority_element(arr_list, size_n):
    maj_ele_contender_1 = arr_list[0]
    maj_ele_contender_2 = arr_list[1]
    count_1 = 0
    count_2 = 0
    for i in range(0, size_n):
        if count_1 == 0:
            maj_ele_contender_1 = arr_list[i]
            count_1 += 1
            continue
        if count_2 == 0:
            maj_ele_contender_2 = arr_list[i]
            count_2 += 1
            continue
        if arr_list[i] != maj_ele_contender_1 and arr_list[i] != maj_ele_contender_2:
            count_1 -= 1
            count_2 -= 1
            continue

        if arr_list[i] == maj_ele_contender_1:
            count_1 += 1
            continue

        if arr_list[i] == maj_ele_contender_2:
            count_2 += 1
            continue


    count_check_1 = 0
    count_check_2 = 0
    for i in range(0, size_n):
        if arr_list[i] == maj_ele_contender_1:
            count_check_1 += 1
        elif arr_list[i] == maj_ele_contender_2:
            count_check_2 += 1



    import math

    if count_check_1 >= (math.floor(size_n / 3) + 1):
        print("Majority element is ", maj_ele_contender_1)
    elif count_check_2 >= (math.floor(size_n / 3) + 1):
        print("Majority element is ", maj_ele_contender_2)
    else:
        print("No Majority element.")


if __name__ == "__main__":
    size_n = int(input("Enter the size"))
    arr_list = list(map(int, input("Enter space separated values").split()))

    find_majority_element(arr_list, size_n)
