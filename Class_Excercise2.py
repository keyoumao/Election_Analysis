# @todo: Write a function that returns the arithmetic average for a list of numbers
# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))

def average(num):
    return float(sum(num)) / max(len(num), 1)

num1 = [1, 5, 9]
num2 = []
for i in range(11):
    num2.append(i)
    print(num2)

print(f"{average(num1)}")
print(f"{average(num2)}")