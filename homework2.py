"""
Author: Jose Pablo Murillo
File: homework2
Description: Use of for and while
Last update: 02/12/2018
Python version 3.6.4
"""

#exercise 1
def invert(number: int) -> int:
    """
    Inputs: An integer
    Outputs: The integer with the digits inverted or error
    Process: a digit is extracted from right to left and then added to the result
    the result is multiplied by 10 and then the digit is added
    the parameters is then shrunk to a smaller number dividing by 10
    Restrictions:use while, number must be integer
    """
    if (type(number) != int):
        return "Number must be integer"
    else:
        negative = number < 0
        number = abs(number)
        result = 0
        while (number > 0):
            currentDigit = number % 10
            result = result * 10
            result = result + currentDigit
            number = number // 10
        if (negative):
            return -result
        else:
            return result



#exercise 2
def palindrome(number: int) -> bool:
    """
    Inputs: A number
    Outputs: Boolean if number is palindrome
    Process: The function invert is called and then verified if numbers match
    Restrictions: Number must be integer
    """
    result = invert(number)
    if (type(result) != int):
        return result
    else:
        return result == number



#exercise 3
def rombus(size: int) -> str:
    """
    Inputs:The size of each side of the rombus
    Outputs:Error or none
    Process: The amount of spaces to print from beginning is
        calculated multiplying the side by 2
        The number of asterisk to print starts in 1
        first we print the top level adding the amount of asterisk to print
        and decreasing the amount of spaces and level

        We reestablish the values used for printing to get ready for bottom level
        and use the inverse of what we did for the top level
    Restrictions:Size must be positive integer >= 2
    """
    copy = size
    if (type(size) != int):
        return "Size must be integer"
    else:
        if (size < 2):
            return "Size must be greater than or equal to 2"
        else:
            leftSide = size * 2
            rightSide = size * 2
            numberAsterisk = 1
            while (size > 0):
                print(" " * leftSide + "*" * numberAsterisk + " " * rightSide)
                leftSide = leftSide - 1
                rightSide = rightSide - 1
                numberAsterisk = numberAsterisk + 2
                size = size - 1
                
            size = copy
            size = size - 1             
            numberAsterisk = numberAsterisk - 4
            leftSide = leftSide + 2
            rightSide = rightSide + 1
            
            while (size > 0):
                print(" " * leftSide + "*" * numberAsterisk + " " * rightSide)
                leftSide = leftSide + 1
                rightSide = rightSide + 1
                numberAsterisk = numberAsterisk - 2
                size = size - 1



#Exercise 4
def printTable(number: int, beginning: int, end: int) -> None:
    """
    Inputs:The number for the multiplication table, its start and end
    Outputs:A multiplication table is shown on screen, returns nothing
    Process:a for loop is done to iterate from beginning to end(including end)
        to print the multiplication
    Restrictions:Inputs must be integers, beginning must be less than end
    """
    
    if ((type(number) != int) or (type(beginning) != int) or (type(end) != int)):
        return "Inputs must all be integers"
    else:
        if (beginning > end):
            return "Beginning cannot be less than end"
        else:
            end = end + 1
            for i in range(beginning, end):
                print(str(number) + " x " + str(i) + " = " + str(i * number))

#Exercise 5
def seriesAhead(start: int, end: int) -> int:
    """
    Inputs:Number of beginning and number of end
    Outputs:A number composed of numbers from the beginning to end
    Process:get the amount of digits of current number to make space in result
        then add the current number to result
    Restrictions:start and end must be positive integers, use for
    """
    if ((type(start) != int) or (type(end) != int)):
        return "Inputs must be all integers"
    else:
        if (start > end):
            return "Beginning cannot be less than end"
        else:
            result = 0
            end = end + 1
            for i in range(start, end):
                length = amountDigits(i)
                result = result * (10**length)
                result = result + i
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



#Exercise 6
def seriesBehind(start: int, end: int) -> int:
    """
    Inputs:Number of beginning and end of series
    Outputs:Number composed of numbers in series
    Process:Get amount of digits of current result, make space in current number
        then add current result
    Restrictions:Use for, start and end must be positive integers
    """
    if ((type(start) != int) or (type(end) != int)):
        return "Inputs must be all integers"
    else:
        if (start > end):
            return "Beginning cannot be less than end"
        else:
            result = 0
            end = end + 1
            for i in range(start, end):
                if (result == 0):
                    result = start
                else:
                    length = amountDigits(result)
                    i = i * (10**length)
                    i = i + result
                    result = i
            return result



#Exercise 7
def intersect(firstNumber: int, secondNumber: int) -> int:
    """
    Inputs: firstNumber and secondNumber
    Outputs: Number composed of common digits
    Process: We invert the number in order to work with it using % and
        because the result must be shown in order from left to right of
        the first number in case the digit appears, it is appended to result
    Restrictions: both inputs must be integers with no repeated digits
    """
    if ((type(firstNumber) != int) or (type(secondNumber) != int)):
        return "Inputs must be all integers"
    elif ((firstNumber < 0) or (secondNumber < 0)):
        return "Numbers must be positive"
    elif(tuple(str(firstNumber)) != list(str(firstNumber)) or
         (tuple(str(SecondNumber)) != list(str(secondNumber)))):
        return "Numbers must not include repeated digits"
    else:
        result = 0
        includeZero = False
        inverted = invert(firstNumber)
        if( firstNumber == 0):
            if (digitInNumber(secondNumber, 0)):
                return 0
            else:
                return False
            
        if (amountDigits(inverted) != amountDigits(firstNumber)):
            includeZero = True

        while (inverted != 0):
            currentDigit = inverted % 10
            inverted = inverted // 10
            if (digitInNumber(secondNumber, currentDigit)):
                result = result * 10
                result = result + currentDigit
        if (result == 0):
            return False
        elif (includeZero):
            return result * 10
        else:
            return result
        
def digitInNumber(number, digit):
    if (number == 0):
        if (digit == 0):
            return True
        else:
            return False
    else:
        while (number != 0):
            current = number % 10
            if (current == digit):
                return True
            number = number // 10
        return False



#Exercise 8
def printEvenOrOddW(start: int , end: int, option: str) -> None:
    """
    Inputs: start number of sequence, end number and option of printing
    Outputs: Sequence of specified numbers from option 
    Process: The number is checked if it is even by checking if the
        remainder is 2. This is done for every number in between start and
        end
    Restrictions: both inputs must be integers and option must be 'odd' or
        'even', must be done using for
    """
    if ((type(start) != int) or (type(end) != int)):
        return "Numbers must be integers"
    else:
        if (start > end):
            return "Start must be greater than end"
        else:
            if (option != "even" and option != "odd"):
                return "Option must be 'even' or 'odd'"
            else:
                if (option == 'even'):
                    if (start % 2 != 0):
                        start = start + 1

                if (option == 'odd'):
                    if (start % 2 == 0):
                        start = start + 1

                end = end + 1
                while (start < end):
                    if (option == 'even'):
                        if (start % 2 == 0):
                            print(str(start) + ",", end="", flush=True)
                    else:
                        if (option == 'odd'):
                            if (start % 2 != 0):
                                print(str(start) + ",", end="", flush=True)
                    start = start + 1





#Exercise 9
def printEvenOrOddF(start: int , end: int, option: str) -> None:
    """
    Inputs: start number of sequence, end number and option of printing
    Outputs: Sequence of specified numbers from option 
    Process: The number is checked if it is even by checking if the
        remainder is 2. This is done for every number in between start and
        end
    Restrictions: both inputs must be integers and option must be 'odd' or
        'even', must be done using for
    """
    if ((type(start) != int) or (type(end) != int)):
        return "Numbers must be integers"
    else:
        if (start > end):
            return "Start must be greater than end"
        else:
            if (option != "even" and option != "odd"):
                return "Option must be 'even' or 'odd'"
            else:
                if (option == 'even'):
                    if (start % 2 != 0):
                        start = start + 1

                if (option == 'odd'):
                    if (start % 2 == 0):
                        start = start + 1

                end = end + 1
                for i in range(start, end):
                    if (option == 'even'):
                        if (i % 2 == 0):
                            print(str(i) + ",", end="", flush=True)
                    else:
                        if (option == 'odd'):
                            if (i % 2 != 0):
                                print(str(i) + ",", end="", flush=True)



#Exercise 10
def doubleFactorial(number: int) -> int:
    """
    Inputs: number
    Outputs: the double factorial or error
    Process: a starting point is defined
        the result is the product of all numbers
            between the start and the number, the
            increment goes every 2 since its double factorial
    Restrictions:number must be positive integer
    """
    if (type(number) != int):
        return "Number must be integer"
    elif(number < 0):
        return "Number must be greater than 0"
    else:
        if (number == 0):
            return 1
        else:
            start = -1
            if (number % 2 == 0):
                start = 2
            else:
                start = 1
            number = number + 1
            result = 1
            for i in range(start, number, 2):
                result = result * i
            return result



#Exercise 11
def sumW(start: int, end: int) -> int:
    """
    Inputs: start of sequence, end of sequence
    Outputs:Sum of numbers between sequence including start and end
    Process:Start with initial sum and then add while start < end
    Restrictions:Start and end must be integers and start < end, use while
    """
    if ((type(start) != int) or (type(end) != int)):
        return "Input must be positive integers"
    elif (start > end):
        return "Start must be less than or equal to end"
    else:
        result = 0
        while (start < end):
            result = result + start
            start = start + 1
        result = result + end
        return result

#Exercise 12
def sumF(start: int, end: int) -> int:
    """
    Inputs: start of sequence, end of sequence
    Outputs:Sum of numbers between sequence including start and end
    Process:Start with initial sum and then add while start < end
    Restrictions:Start and end must be integers and start < end, use while
    """
    if ((type(start) != int) or (type(end) != int)):
        return "Input must be positive integers"
    elif (start > end):
        return "Start must be less than or equal to end"
    else:
        result = 0
        end = end + 1
        for i in range(start, end):
            result = result + i
        return result

#Exercise 13
def fibo(n: int) -> None:
    """
    Inputs: number indicating how many elements of fibonacci will be printed
    Outputs: fibonacci sequence
    Process:Begin with the first two terms first, and step (the next one)
        in case the number is greater than 2, we add the first two terms,
            define the first as the step and then the step is the new sum
            we continue updating using while
    Restrictions:n must be positive integer
    """
    if ((type(n) != int)):
        return "Input must be integer"
    elif (n < 0):
        return "Input must be integer greater than 0"
    else:
        first = 0
        step = 1
        if (n == 1):
            print(str(first))
        elif(n == 2):
            print(str(first), end=",", flush=True)
            print(str(step), end=",", flush=True)
        else:
            print(str(first), end=",", flush=True)
            print(str(step), end=",", flush=True)
            while (n > 2):
                new = first + step
                first = step
                step = new
                print(str(new), end=",", flush=True)
                n = n - 1



#Exercise 14
def nameOfDay(date: int) -> str:
    """
    Inputs: date
    Outputs: Corresponding day or false if it doesn't exist
    Process: We validate the input and then use Zeller's algorithm
        to determine the day
    Restrictions: date must be in format ddmmaaaa
    """
    if (type(date) != int):
        return "Input must be integer"

    if (dateValid(date)):
        year:int = date % 10000
        date = date // 10000
        month:int = date % 100
        day:int = date // 100

        if (month < 2):
            month = month + 12
            year = year - 1
       
        k = year % 100
        c = year // 100

        w = int(2.6 * month - 5.39)
        w = w + int(k / 4)
        w = w + int(c / 4)
        w = w + day
        w = w + k
        w = w - 2 * c
        w = w % 7
        if (w == 0):
            return "Sunday"
        elif (w == 1):
            return "Monday"
        elif (w == 2):
            return "Tuesday"
        elif (w == 3):
            return "Wednesday"
        elif (w == 4):
            return "Thursday"
        elif (w == 5):
            return "Friday"
        elif (w == 6):
            return "Saturday"
    else:
        return False

def isLeap(year: int) -> bool:
    """
    Inputs: a year
    Output: boolean or error
    Process: Determines if year is a leap year by checking if the year is
    divisible by 4
    Restrictions: year must be an integer, year must be >= 2000 and have 4 digits
    """
    if (year < 2000 or year > 9999):
        return "Error: year not in permitted range"
    else:
        return (year % 4 == 0)


def dateValid(date: int) -> bool:
    """
    Inputs: a date as int with format ddmmaaaa
    Output: boolean
    Process: the date is broken down into separate components day, month and year
    and performs the validation acording to the provided restrictions
    Restrictions: date must be int
    year must be >= 1900
    month must be between 1 and 12
    february has 29 days if year is leap, else it has 28
    january, march, may, july, august, october and december have 31 days
    april, june, september and november have 30 days
    """
    year:int = date % 10000
    date = date // 10000
    month:int = date % 100
    day:int = date // 100

    if (year >= 1900):
        if (month >= 1 and month <= 12):
            if (month == 2):
                if (isLeap(year)):
                    if (day >= 1 and day <= 29):
                        return True
                else:
                    if (day >= 1 and day <= 28):
                        return True
            else:
                if (month == 1 or month == 3 or month == 5 or month == 7 \
                    or month == 8 or month == 10 or month == 12):
                    if (day >= 1 and day <= 31):
                        return True
                else:
                    if (month == 4 or month == 9 or month == 11):
                        if (day >= 1 and day <= 30):
                            return True
    return False



#Exercise 15
def divisors(number: int) -> None:
    """
    Input: a integer
    Output: prints the divisors of the number
    Process: starting from 1, we check if number is divisible by the current
        i
    Restrictions:Number must be positive integer, use for
    """
    if (type(number) != int):
        return "Input must be integer"
    elif (number < 0):
        return "Input must be positive integer"
    else:
        
        for i in range(1, number + 1):
            if ((number % i) == 0):
                print(str(i), end=",", flush=True)



#Exercise 16
def sumDivisors(number: int) -> int:
    """
    Input: a number
    Output: sum of divisors of the number
    Process: starting from 1, we check if number is divisible by the current
        i
    Restrictions: Number must be positive integer, use while
    """
    if (type(number) != int):
        return "Input must be integer"
    elif (number < 0):
        return "Input must be positive integer"
    else:
        result = 0
        divisor = 1
        while (divisor <= number):
            if ((number % divisor) == 0):
                result = result + divisor
            divisor = divisor + 1
        return result



#Exercise 17
def prime(number: int) -> bool:
    """
    Input: a number
    Output: boolean to determine if it is prime
    Process: we check if 1 + the number is equal to the sum of divisors
    We put exception for 1, which does not follow the previous rule
    Restrictions: number must be positive integer
    """
    if (type(number) != int):
        return "Input must be integer"
    elif (number < 0):
        return "Input must be positive integer"
    else:
        if (number == 1):
            return True
        else:
            if (number + 1 == sumDivisors(number)):
                return True
            else:
                return False



#Exercise 18
def prime2(number: int) -> bool:
    """
    Input: a number
    Output: boolean to determine if it is prime
    Process: we check if 1 + the number is equal to the sum of divisors
    We put exception for 1, which does not follow the previous rule
    Restrictions: number must be positive integer
    """
    if (type(number) != int):
        return "Input must be integer"
    elif (number < 0):
        return "Input must be positive integer"
    else:
        for i in range(2, number):
            if (number % i == 0):
                return False
            else:
                pass
        return True



#Exercise 19
def sumPrimes(start: int, end: int) -> int:
    """
    Input: start and end of sequence
    Output: sum of primes between sequence including ends
    Process: for each number in sequence if it is prime, we add to result
    Restrictions: Numbers must be positive integers
    """
    if ((not isinstance(start, int)) or (not isinstance(end, int))):
        return "Input must be integers"
    elif (start < 0 or end < 0):
        return "Input must be positive integers"
    elif (start > end):
        return "Start cannot be greater than end"
    else:
        result = 0
        end = end + 1
        for i in range(start, end):
            if prime(i):
                result = result + i
        return result



#Exercise 20
def friends(number1: int, number2: int) -> str:
    """
    Input: two numbers
    Output: 'Friendly pair' or 'not a friendly pair'
    Process: We calculate the sum of divisors of each number
        If the numbers themselves are different, they are friends
    """
    if ((type(number1) != int) or (type(number2) != int)):
        return "Input must be integers"
    elif (number1 < 0 or number2 < 0):
        return "Input must be positive integers"
    else:
        sum1 = sumDivisors(number1)
        sum2 = sumDivisors(number2)
        if (sum1 == sum2 and number1 != number2):
            return "Friendly pair"
        else:
            return "Not friendly pair"
        


        
        
                    
                    
                    
                
            
    
            
