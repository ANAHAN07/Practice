def rotate_list(lst, x):
    x %= len(lst)
    return lst[-x:] + lst[:-x]

print(rotate_list([8, 9, 10, 33, 48], 6))  # Output: [48, 8, 9, 10, 33]
