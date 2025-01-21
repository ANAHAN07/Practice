def average_excluding_extreme(numbers):
    if len(numbers) <= 2:
        return 0 
    return sum(numbers) - max(numbers) - min(numbers) / (len(numbers) - 2)

print(average_excluding_extreme([50, 90, 69, 99, 1080]))  # Output: 291.3333333333333 