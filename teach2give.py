
'''
DONE IN PYTHON PROGRAMMING LANGUAGE
'''


'''
Question 1: FizzBuzz
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
"FizzBuzz".
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


'''
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.
'''
def fibonacci_sequence(limit):
    a, b = 0, 1
    fibonacci_list = []
    
    while a <= limit:
        fibonacci_list.append(a)
        a, b = b, a + b
        
    return fibonacci_list
fibonacci_numbers = fibonacci_sequence(100)
print("Fibonacci sequence up to 100:")
print(fibonacci_numbers)

'''Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.
'''
def is_power_of_two(number):
    if number <= 0:
        return False
    mask = 1
    while mask & number != mask:
        mask <<= 1
    exponent = 0
    while mask > 1:
        if mask == 2:
            break
        mask >>= 1
        exponent += 1

    return exponent >= 1 and (mask == number or mask * 2 == number)

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    result = is_power_of_two(num)
    print(f"{num} is {'' if result else 'not'} a power of two.")
'''
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
'''
def capitalize_words(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    result_string = ' '.join(capitalized_words)
    return result_string
input_string = input("Enter a string: ")
output_string = capitalize_words(input_string)
print(f"The capitalized string is: {output_string}")
'''
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
'''
def reverse_integer(number):
    sign = '-' if number < 0 else ''
    number = abs(number)
    digits = [int(d) for d in str(number)[::-1]]
    reversed_digit_sum = sum(digits) * int(sign == '-')
    return reversed_digit_sum
user_input = int(input('Please enter an integer: '))
result = reverse_integer(user_input)
print(f'Reversed integer: {result}')


'''
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
'''
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    sentence = "".join(char for char in sentence if char.isalnum()).lower()
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count