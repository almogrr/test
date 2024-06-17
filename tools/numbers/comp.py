from tools.numbers.flag import check_simp_first_flag,check_simp_two

def sum_of_digits(number):
    global check_simp_first_flag
    global check_simp_two
    if check_simp_first_flag== True and check_simp_two == False:
        # Convert the number to a string to iterate through its digits
            digits = str(number)
            # Initialize a variable to store the sum
            total = 0
            
            # Iterate through each digit in the string
            for digit in digits:
                # Convert each digit back to an integer and add it to the total
                total += int(digit)
            
            return total
    else:
        raise RuntimeError("Error: Please call an initial function from 'simp' module (add or subtract) before using this function.")
        

# print(sum_of_digits(12345))


def is_palindrome(number):
    global check_simp_first_flag
    global check_simp_two
    if check_simp_first_flag== True and check_simp_two == False:
        # Convert the number to a string to compare it with its reverse
            number_str = str(number)
            # Reverse the string representation of the number
            reversed_str = number_str[::-1]
            
            # Check if the original string is equal to its reverse
            return number_str == reversed_str
    else: 
            raise RuntimeError("Error: Please call an initial function from 'simp' module (add or subtract) before using this function.")


# result1 = is_palindrome(121)
# print(result1)  # Output will be True
