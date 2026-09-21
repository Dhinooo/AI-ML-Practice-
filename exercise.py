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
