def common_elements(lst_1, lst_2):
    return list(set(lst_1) & set(lst_2))

print(common_elements([20, 25, 30, 77, 59],[2, 70, 30, 9, 25]))    # Output: [25, 30]