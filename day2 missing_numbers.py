def missing_numbers(num_list):
    new_list = []
    for num in range(num_list[0], num_list[-1]):
        if num not in num_list:
            new_list.append(num)          
    print(new_list)
missing_numbers([1, 2, 3, 4, 6, 7, 10])
missing_numbers([10, 11, 12, 14, 17])
