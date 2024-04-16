#Aaron Kotz, CIS261, IterationAndRecursion

# Iterative function to calculate factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive function to calculate factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Numbers for which to calculate factorial
numbers = [0, 5, 10, 25, 50, 100]

# Print results using the iterative function
print("Factorial results using an iterative function")
for num in numbers:
    print(f"{num}! = {factorial_iterative(num)}")

# Print results using the recursive function
print("\nFactorial results using a recursive function")
for num in numbers:
    print(f"{num}! = {factorial_recursive(num)}")

