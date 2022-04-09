# Paragon National Group Spring 2022
# Computer Science / Data Science Track
# HW 2

# Assigned: April 7, 2022
# Due: April 12, 2022 11:59pm

# This is the second programming assignment of the computer science track.
# For each function, a skeleton is provided, where your job is to fill the *TODO* out.
# The questions will cover the topics learned in the second lecture, which entailed
# recursive functions, for and while loops, string indexing, and linked lists.

# This function takes a natural number as an argument (so it can't be negative) 
# and returns a boolean value of true or false that shows whether the inputted 
# number is a palindrome or not. A palindrome is something that reads the same 
# backward as forward (i.e. '2002'). Use a for or while for the implementation 
# of this function.
# Ex) iterative_palindrome(1) -> true
#     iterative_palindrome(12) -> false
#     iterative_palindrome(2468642) -> true
def iterative_palindrome(n):
    n_list = [int(digit) for digit in str(n)]
    new_n = []
    is_palindrome = False

    for digit in n_list:
        new_n.insert(0, digit)

    iteration = 0

    for i in n_list:
        if i == new_n[iteration]:
            is_palindrome = True
            iteration += 1
        else:
            is_palindrome = False
            break

    return is_palindrome

print(iterative_palindrome(2002))
print(iterative_palindrome(1234))

# This function is the same as iterative_palindrome() except instead of using a
# loop, implement the function in a recursive way.
# Ex) recursive_palindrome(1) -> true
#     recursive_palindrome(12) -> false
#     recursive_palindrome(2468642) -> true
def recursive_palindrome(n):

    n_list = [int(digit) for digit in str(n)]
    new_n = []

    for digit in n_list:
        new_n.insert(0, digit)

    no_of_iterations = len(n_list)

    is_palindrome = True

    def helper(iteration):

        global is_palindrome

        if iteration == no_of_iterations:
            is_palindrome = True
        else:
            if n_list[iteration] == new_n[iteration]:
                iteration += 1
                is_palindrome = True
                helper(iteration)
            else:
                is_palindrome = False

        return is_palindrome

    return helper(0)

print(recursive_palindrome(2002))
print(recursive_palindrome(1234))

# Helper function for sum_factorials(). Takes a number as an argument and returns
# the factorial of that number.
# Ex) factorial(1) -> 1
#     factorial(4) -> 24
#     factorial(7) -> 5040
def factorial(n):

    i = 1

    factorial = 1

    while i <= n:
        factorial *= i
        i += 1

    return factorial

print(factorial(1))
print(factorial(4))
print(factorial(7))

# Helper function for sum_factorials(). Takes a number as an argument and returns
# a boolean value of true or false that shows whether the inputted number is a 
# prime or not.
# Ex) is_prime(7) -> true
#     is_prime(12) -> false
#     is_prime(23) -> true
def is_prime(n):

    i = 2
    no_divisors = 0

    while i < n:
        if n % i == 0:
            no_divisors += 1
            i += 1
        else:
            no_divisors += 0
            i += 1

    return no_divisors == 0

print(is_prime(2))
print(is_prime(7))
print(is_prime(12))
print(is_prime(23))

# Function that creates a node to help testing of sum_factorials()
class Node:
    def __init__(self, content): 
        self.content = content
        self.next = None

# Function to insert a node to the beginning of a linked list
def push(head_ptr, new_content):
    new_node = Node(0)
    new_node.content = new_content
    new_node.next = (head_ptr)
    (head_ptr) = new_node
    return head_ptr

# This function takes a pointer to the head node of the linked list as an argument
# and returns the sum of factorials of prime numbers in the linked list. Above are
# two helper functions for this that are highly recommended.
# Ex) lst = None
#     lst = push(lst, 2)
#     lst = push(lst, 14)
#     lst = push(lst, 5)
#     lst = push(lst, 3)
#     lst = push(lst, 6)
#     sum_factorials(lst) -> 128
def sum_factorials(head_ptr):
    cur = head_ptr
    res = 0

    while cur is not None:
        if is_prime(cur.content):
            res += factorial(cur.content)
        cur = cur.next

    return res

lst = None
lst = push(lst, 2)
lst = push(lst, 14)
lst = push(lst, 5)
lst = push(lst, 3)
lst = push(lst, 6)

print(sum_factorials(lst))