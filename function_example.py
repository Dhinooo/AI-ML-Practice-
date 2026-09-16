# Function is a reusable block of code that performance a specific task ------------------------

# Parameter -> The value which we receive from a function
# Argument -> The actual value passed on the function

# print("Hello Ravi")
# print("Hello Dinesh")
# print("Hello Raju")


def greet(name):
    print(f"Hello {name}")


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


def add(a, b):
    return a + b


ans = add(5, 7)
# print(ans)

# Function Without Parameters


def sample():
    print("This function is without parameters -")


sample()
