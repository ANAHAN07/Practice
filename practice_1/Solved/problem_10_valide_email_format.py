import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

print(validate_email("oyshitasnim2016@gmail.com"))           # Output: True
print(validate_email("fasdfadfadsffsayjc"))                  # Output: False 