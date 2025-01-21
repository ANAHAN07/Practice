def element_wise_operation(lst1, lst2, operation):
    if len(lst1) != len(lst2):
        return "Lists must be of equal length."
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Undefined"
    }
    return [operations[operation](x, y) for x, y in zip(lst1, lst2)] if operation in operations else "Invalid operation."

print(element_wise_operation([1, 35, 1000], [99, 34, 80], "add"))  # Output: [100, 69, 1080]