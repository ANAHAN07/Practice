def merge_remove_duplicate(lst_1, lst_2):
    return list(set(lst_1 + lst_2))

print(merge_remove_duplicate([5, 7, 8, 9, 15], [8, 10, 15, 20, 21]))        # Output: [5, 7, 8, 9, 10, 15, 20, 21]