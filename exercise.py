# input: num = 20
# o/p : The num is positive


# number = int(input("Enter a Number : "))

# if number > 0:
#     print("The number is positive ", number)
# elif number < 0:
#     print("The number is negative", number)
# else:
#     print("The number is Zero")
# number = int(input("Enter a Number : "))

# if number > 0:
#     print("The number is positive ", number)
# elif number < 0:
#     print("The number is negative", number)
# else:
#     print("The number is Zero")


# Our first Machine Learning dataset

# import pandas as pd

# data = {
#     "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
#     "attendance": [55, 60, 65, 70, 80, 85, 90, 95],
#     "result": ["Fail", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass"],
# }

# df = pd.DataFrame(data)

# print(df)


# import matplotlib.pyplot as plt

# for result in ["Fail", "Pass"]:
#     subset = df[df["result"] == result]
#     plt.scatter(subset["hours_studied"], subset["attendance"], label=result)

# plt.xlabel("Hours Studied")
# plt.ylabel("Attendance (%)")
# plt.title("Student Data")
# plt.legend()
# plt.show()

# a = 10
# b = 20

# a, b = b, a  # 10, 20 = 20, 10

# print(a) # 10
# print(b) # 20

# name = "Dhinakaran"
# age = 25

# print("My name is", name)
# print("I am", age, "years old")


# name = "Dhinakaran"
# age = 25
# age = age + 1

# print(name)
# print(age)


# a = 10
# b = 10.5
# c = "10"
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


x = 10
y = 5.5

print(x + y)
print(type(x + y))
a = "10"
b = "20"

print(a + b)


a = 10
b = "20"

print(str(a) + b)


a = "10"
b = "20"

print(int(a) + int(b))


is_student = True

print(is_student)
print(type(is_student))


x = True
y = 10

print(x + y)


x = False
y = 10

print(x + y)


x = 10
y = float(x)

print(y)
print(type(y))

x = 10.5
y = int(x)

print(y)
print(type(y))

x = "10.5"
y = float(x)

print(y)
print(type(y))


x = "10"
y = 5

print(x + str(y))

a = 10
b = 2.5
c = "5"

result = a + b + int(c)

print(result)
print(type(result))

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)

a = 10
b = 3

print(a / b)

a = 10
b = 3

print(a % b)

a = 10
b = 3

print(a // b)

a = 10
b = 3

result = a + b * 2

print(result)

correct = 87
total = 100

accuracy = (correct / total) * 100

print(accuracy)
