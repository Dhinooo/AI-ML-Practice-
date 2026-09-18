# print("Hello World")
# print("Hello World")
# print("Hello World")

# print("--------------------------")

# for i in range(30):
#     print("Hello World :",i)

# fruits = ['apple','Orange','mango','papaya']

# for i in fruits:
#     print('The Fruit Name is : ',i)


# stu_name ="I am the student, my name is dhina "

# for i in stu_name:
#     print("Student Name is : ",i)

# for i in range(1, 30, 2):
#     print("HELLO", i)


students = {
    "name": "dhina",
    "age": 25,
    "course": "python",
    "Marks": [20, 40, 20, 40, 20],
}

# for key,value in students.items():
#     print("The key is :",key, "....","The value is :",value)

# ----------------------------FOR LOOP-------------------------------------------

# for key in students.keys():
#     print("The key is :", key)

# for value in students.values():
#     print("The value is :",value)
# -------------------------------------------------------------------------------

# i = 1

# while i < 10:
#     print("The Value Of I is :", i) # While loop execute until the condition are met (True)
#     # i+=1
#     i += 1

# --------------------------------------------------------------------------------


i = 0

while i < 10:
    print("The value is :", i)

    if i == 8:
        break
    i += 1
# --------------------------------------------------------------------------------


i = 0

while i < 5:
    i += 1
    if i == 3:
        continue

    print("value :", i)
