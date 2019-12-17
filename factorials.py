# --- Factorials --- #
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

num = int(input("Pick a number: "))
x = factorial(num)
print("{}! is {}.".format(str(num), str(x)))
