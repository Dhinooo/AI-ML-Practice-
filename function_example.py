# Function is a reusable block of code that performance a specific task ------------------------

# Parameter -> The value which we receive from a function
# Argument -> The actual value passed on the function

# print("Hello Ravi")
# print("Hello Dinesh")
# print("Hello Raju")


# def greet(name):
#     print(f"Hello {name}")


# greet("Ravi")
# greet("Ramu")
# greet("Raju")


# Addition of two values
# -------USING VOID FUNCTION----------
# Function With Parameters

# def add(a, b):
#     print(f"Addition of value is : {a+b}")


# add(5, 5)

# ---------USING RETURN FUNCTION ------------------
# Function With Parameters


# def add(a, b):
#     return a + b


# ans = add(5, 7)
# print(ans)

# Function Without Parameters


# def sample():
#     print("This function is without parameters -")


# sample()


# ---------------Lambda Function -----------
# Its a small Function it is usually used for simpler operation---------------


# Addition

# add = lambda a, b: a + b
# print(add(3, 2))

# Square

# square = lambda a, b: a * b
# print(square(2,5))


# square = lambda x: x * x
# print(square(5))

# GLOBAL VARIABLE AND LOCAL VARIABLE

# GLOBAL SCOPE AND LOCAL SCOPE

i = 10


def value():

    print("This is local variable value is : ", i)  # This is local scope


value()

print("This is Global Variable value is : ", i)  # This is Global Scope
