# try, except, finally [handle the any type of error and exception in the python]

a = 10
b = 0


try:
    print(a / b)

except ZeroDivisionError:
    print("You can't divide a value by Zero (it is mathemeticaly wrong)")
