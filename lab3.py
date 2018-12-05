"""
Author: Jose Pablo Murillo
File: lab3 for/while
Description: Use of for and while
Last update: 03/12/2018
Python version 3.6.4
"""

#Exercise 1
def deleteDigit(number: int, digit: int) -> int:
    """
    Input:A number and a digit
    Output:The number without specified digit
    Process:We access the digits from left to right using amountOfDigits
        if the currentDigit is not the one we need to delete, we append to
        the result, if the result is negative, it means we did not append digits
        Special case must be taken into consideration when 0 is the last digit
    Restriction:Number and digit must be integers
        Number can be negative or positive
        Digit must be between 0 and 9
    """
    negative = False
    if ((not isinstance(number, int) or (not isinstance(digit, int)))):
        return "Input must be int"
    if (number < 0):
        negative = True
        number = -number
    if (digit < 0 or digit not in range(0,10)):
        return "Digit must be positive integer between 0 and 9"
    else:
        if (number == 0 and number == digit):
            return "Number ends without digits"
        else:
            copy = number
            result = -1
            while (number > 0):
                length = amountDigits(number) - 1
                currentDigit = number // (10**length)
                number = number % (10**length)
                if (currentDigit != digit):
                    if (result < 0):
                        result = currentDigit
                    else:
                        result = result * 10
                        result = result + currentDigit
            if (copy % 10 == 0):
                if (copy % 10 != digit):
                    result = result * 10
            if (result < 0):
                return "Number ends without digits"
            else:
                if (negative):
                    return -result
                else:
                    return result
                                   
def amountDigits(number: int) -> int:
    if number == 0:
        return 1
    else:
        count = 0
        while (number != 0):
            count = count + 1
            number = number // 10
        return count



#Exercise 2
def evenOdds(number: int) -> tuple:
    """
    Inputs: number
    Outputs: even digits and odd digits in number
    Process: Using amountOfDigits, we get the currentDigit from left
        to right
        we then place it in the variable even or odd depending if
        it is divisible by 2
        Some special cases were taken into consideration like 0
    Restrictions: number must be integer
    """
    if (not isinstance(number, int)):
        return "Input must be integer"
    elif (number < 0):
        number = abs(number)
    copy = number
    even = -1
    odd = -1
    zero = False
    while (number > 0):
        length = amountDigits(number) - 1
        currentDigit = number // (10**length)
        number = number % (10**length)
        if (currentDigit % 2 == 0):
            if (currentDigit == 0):
                zero = True
                
            elif (even < 0):
                even = currentDigit
            else:
                even = even * 10
                even = even + currentDigit
        else:
            if (odd < 0):
                odd = currentDigit
            else:
                odd = odd * 10
                odd = odd + currentDigit
    if (copy % 10 == 0):
        even = even * 10
    if (even < 0):
        even = "None"
    if (odd < 0):
        odd = "None"
    return (even, odd)


#Exercises 3,4,5,6 are in homework1.py

#Exercise 7
def intersection(number1: int, number2: int) -> int:
    """
    Inputs: two numbers
    Output: number composed of common digits or false
    Process:We start from left to right to determine if the digit from
        the first number exists in the second number and does not exist in
        the result since we do not take repeated
    Restriction: numbers must be integers
    """
    if ((not isinstance(number1, int)) or (not isinstance(number2, int))):
        return "Inputs must be integers"
    else:
        number1 = abs(number1)
        copy = number1
        number2 = abs(number2)
        result = -1
        zero = False
        while (number1 > 0):
            length = amountDigits(number1) - 1
            currentDigit = number1 // (10**length)
            number1 = number1 % (10**length)
            if (existDigit(number2, currentDigit)):
                if (result < 0):
                    result = currentDigit
                    if (currentDigit == 0):
                        zero = True
                elif (not existDigit(result, currentDigit)):
                    result = result * 10
                    result = result + currentDigit
        if (copy % 10 == 0):
            if (existDigit(number2, 0)):
                if (result < 0):
                    result = 0
                else:
                    result = result * 10
        
        if (zero):
            print("enter")
            if (result < 0):
                result = 0
            else:
                result = result * 10
                
        if (result < 0):
            return False
        else:
            return result
        
def existDigit(number: int, digit: int):
    if (number == 0 and digit == 0):
        return True
    else:
        while (number > 0):
            currentDigit = number % 10
            if (currentDigit == digit):
                return True
            else:
                number = number // 10
        return False
        
        
                    

    
            
