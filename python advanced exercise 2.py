# Question 1
import math
a = 5
b = 10
c = 7
a += 3
b *= 2
c %= 4
final_result = math.sqrt(a**2 + b**2 + c**2)
print(round(final_result, 2))

# Question 2
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))
condition_1 = x % 2 == 0
condition_2 = y > 0
condition_3 = 10 <= z <= 50
final_condition = condition_1 and condition_2 and condition_3
print(final_condition)

# Question 3
base_score = int(input("Enter your base score: "))
base_score += 5
base_score -= 10
base_score = min(100, max(0, base_score))
if base_score >= 90:
    print("A")
elif base_score >= 80:
    print("B")
elif base_score >= 70:
    print("C")
elif base_score >= 60:
    print("D")
else:
    print("F")

# Question 4
num_1 = float(input("Please enter a number: "))
num_2 = float(input("Please enter a number: "))
operation = input("Please enter an operation (+, -, *, /, %, **): ")
if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        print("Cannot divide by zero")
elif operation == "%":
    try:
        result = num_1 % num_2
    except ZeroDivisionError:
        print("Cannot divide by zero")
elif operation == "**":
    result = num_1 ** num_2
print(f"The result is: {result}")