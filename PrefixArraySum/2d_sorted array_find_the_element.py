# Problem: Given an 2d array of size n x m , which is already sorted row and column wise, find any element x
#
# Soln: If the array is sorted row and column wise, lets pick the top right most element ,
# check if the x element is greater or less than the top right element
# if x is greater that means , in that row the element is not present , we increase the row and move down in the same column
# if x is less that means, in the column , the element will not be present , becuase the vlaue of all below will be greater , so
#     we decrease the column value and keep the row same, keep doing this until, either row crosses n size or column reaches to 0


def find_max_value_element(twod_array, find_element):
    size_n_row = len(twod_array)
    size_m_col = len(twod_array[0])
    row = 0
    col = size_m_col - 1
    while(True):
        print(row, col)
        if row >= size_n_row  or col < 0:
            return -1,-1
        if find_element == twod_array[row][col]:
            return row, col
        if find_element > twod_array[row][col]:
            row += 1
        elif find_element < twod_array[row][col]:
            col -= 1



if __name__ == "__main__":
    # size_n_row, size_m_col = tuple(map(int, input("Enter the size: ").split()))
    # twod_array = [[0]* size_m_col for _ in range(size_n_row)]
    #
    # print(twod_array)
    # # find_majority_element(arr_list, size_n)
    # for i in range(size_n_row):
    #     arr_list = list(map(int, input(f"Enter space separated values row {i}").split()))
    #     twod_array[i] = arr_list

    # print(twod_array)
    twod_array = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    find_element = int(input("Enter the element you want to find: "))

    val1, val2 = find_max_value_element(twod_array, find_element)

    if val1 == -1:
        print("Element not found")
    else:
        print(f"Element found at row {val1+1} col {val2+1}")
