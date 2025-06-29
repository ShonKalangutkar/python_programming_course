def is_palindrome_number(number):
    if number < 0:
        return False
    
    num_str = str(number)

    reversed_num_str = num_str[::-1]

    return num_str == reversed_num_str


number = int(input("enter your number to check if it's palindrome or not: "))

if is_palindrome_number(number):
    print("number is palindrome")
else:
    print("number is not palindrome")
    