#!/usr/local/bin/python3

def min_max_helper(array, start, end):
    if (end - start <= 1):
        return ( array[start], array[start] )

    min = array[start]
    max = array[start]
    rest_of_list = min_max_helper(array, start + 1, end)

    if ( min > rest_of_list[0] ):
        min = rest_of_list[0]
    if ( max < rest_of_list[1] ):
        max = rest_of_list[1]

    return (min, max)

def min_max(array, start, end):
    if ( end - start == 0 ):
        return (0, 0);

    return min_max_helper( array, start, end )

array = [];
while True:
    data_in = input("Enter a number or #END when you're done: ")
    if data_in == "#END":
        break
    array.append(int(data_in))


minmax_tuple = min_max(array, 0, len(array) - 1)
print(f"The minimum value is { minmax_tuple[0] }")
print(f"The maximum value is { minmax_tuple[1] }")

# test_arr = []
# test_tuple = min_max( test_arr, 0, len(test_arr) )
# print("test 1")
# print(f"max: { test_tuple[1] }")
# print(f"min: { test_tuple[0] }")
# print()

# test_arr = [1, 2, 3, 4, 5, 6]
# test_tuple = min_max( test_arr, 0, len(test_arr) )
# print("test 2")
# print(f"max: { test_tuple[1] }")
# print(f"min: { test_tuple[0] }")
# print()

# test_arr = [0, 0, 0, 0, 0, 0, 0]
# test_tuple = min_max( test_arr, 0, len(test_arr) )
# print("test 3")
# print(f"max: { test_tuple[1] }")
# print(f"min: { test_tuple[0] }")
# print()

# test_arr = [-1, -6, -5, -4, -9]
# test_tuple = min_max( test_arr, 0, len(test_arr) )
# print("test 4")
# print(f"max: { test_tuple[1] }")
# print(f"min: { test_tuple[0] }")
# print()

# test_arr = [0, 9, 5, -3, -1, 4, -5, -5, -5, -5, 6, 9, 100, -4, 123]
# test_tuple = min_max( test_arr, 0, len(test_arr) )
# print("test 5")
# print(f"max: { test_tuple[1] }")
# print(f"min: { test_tuple[0] }")
# print()

# test_arr = ["cat", "dog"]
# test_tuple = min_max( test_arr, 0, len(test_arr) )
# print("test 6")
# print(f"max: { test_tuple[1] }")
# print(f"min: { test_tuple[0] }")
# print()