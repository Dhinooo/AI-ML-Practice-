greetings = "HI, my name is Dhina "

ans = len(greetings)
# print(ans)





#------------------- Index Concepts --------------------------
indx = greetings[0]

# print(greetings[1])
# print(indx)

# print(greetings[1:6])




# -------- Case Comversion ----------------

upper_case = greetings.upper()

# print(upper_case)

lower_case = greetings.lower()

# print(lower_case)

capitalize_case = greetings.capitalize()

# print(capitalize_case)
 
casefold_case = greetings.casefold()  #Similer to lowercase  

# print(casefold_case)

endswith_case = greetings.endswith("Dhina ")

# print(endswith_case)

title_case = greetings.title()
# print(title_case)

swap_case = greetings.swapcase()

# print(swap_case)


# --------------------- Searching ----------------------------------

find_index = greetings.find("Dhina")
print(find_index)

# start_with 

python_index = greetings.startswith("HI")

print(python_index)

# replace

replace_with = greetings.replace("is","great")

print(replace_with)