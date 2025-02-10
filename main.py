def find_max(lst):
    max_num =lst[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num

numbers = [1, 1, 23, 4, 42, 52, 32, 26]
print(find_max(numbers))