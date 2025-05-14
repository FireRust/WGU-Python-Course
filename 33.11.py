# The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. Any negative index values should return -1.
#
# Ex: If the input is:
#
# 7
# the output is:
#
# fibonacci(7) is 13
# Note: Use a for loop and DO NOT use recursion.
#
def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1   # NOTE: This could be written as "a, b = 0, 1"
    for i in range(2, n + 1):
        b = a + b
        a = b -a    #NOTE: This could be written as "a, b = b, a + b" instead. 'a' is assigned original value of 'b' while 'b' is being assigned 'a + b' simultanesouly.
    return b

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
















# The Fibonacci sequence begins with 0 and then 1 follows.
# All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function,
# which has an index n as parameter and returns the nth value in the sequence. Any negative index values should return -1.
#
# Ex: If the input is:
#
# 7
# the output is:
#
# fibonacci(7) is 13
# Note: Use a for loop and DO NOT use recursion.


def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 0

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')

