def divisor_counter(num):
    return len([i for i in range(1, num + 1) if num % i == 0])

print(divisor_counter(1080))        # Output: 32 