user_data = input ("name, lastname, birth year separated by space: ").split(" ")


curr_year =2021
t = curr_year-int(user_data[2])
# age=curr_year-int(birth_year)

# print ( f"Yur name`s: {full}, age`s: {age}")

print (f"name {user_data[0]}, last name {user_data[1]}, age {t}")