def count_minimum_rotations(list):
    low, high = 0, len(list) - 1
    mid = (low + high) // 2 

    # Edge Case: if List is Empty or One Element
    if len(list) == 0 or len(list) == 1:
            return 0

    while low <= high:
        mid = (low + high) // 2
        mid_number = list[mid]

        # print(f'mid = {mid}')
        # print(f'low = {low}')
        # print(f'high = {high}')
        # print('*' * 50)

        if mid_number <= list[high]:
            if mid_number != list[mid - 1] and mid_number < list[mid - 1]:
                return mid
            high = mid - 1
        elif mid_number > list[high]:
            low = mid + 1
    return mid

# print(count_minimum_rotations([19, 25, 29, 3, 5, 6, 7, 9, 11, 14])) Pass
# print(count_minimum_rotations([11, 1, 5, 6, 7, 8, 9, 10])) Pass
# print(count_minimum_rotations([7, 8, 9, 10, 11, 1, 5, 6])) Pass
# print(count_minimum_rotations([5, 6, 9, 0, 2, 3, 4])) Pass
# print(count_minimum_rotations([5, 6, 6, 9, 9, 9, 0, 0, 0, 0, 2, 3, 3, 3, 3, 4, 4])) Pass
# print(count_minimum_rotations([5, 6, 9, 0, 2, 3, 4])) Pass
# print(count_minimum_rotations([2, 3, 3, 3, 3, 4, 1, 1, 1])) Pass
# print(count_minimum_rotations([1, 2, 3, 4])) Pass 
# print(count_minimum_rotations([1, 2])) Pass
# print(count_minimum_rotations([])) Pass


