def wultc (com):
    while True: 
        com_data1 = input("first name, last name, birth age, death age separated by space:\n").split(" ")
        status  = input ("Would you like to continue? If yes press Y, if no press N  ")
        if status == "N":
            break
        else:
            continue
    return com
# com_data = input("first name, last name, birth age, death age separated by space:\n").split(" ") 

# print (wultc(com_data))


names = []
com_data = []
ages=[]
a=0
  
#com_data = input("first name, last name, birth age, death age separated by space:\n").split(" ")
b = wultc(com_data)
for i in range (len(b)-1):
    
    names.append(b[1])
    a = int(b[3])-int(b[2])
    ages.append(a)
#age_sum = age_sum+ int(data[1])

for idx, val in enumerate(names):
     print (f"User {idx}: {val}, {ages[idx]}")

# for i in range (n):
#     a = int(com_list[i][3])-int(com_list[i][2])
#     age.append(a)
#     print (f"first name: {com_list[i][0]}, last name: {com_list[i][1]}, age:  {age[i]}")
# s = int(sum (age)/n)
# print(f"Average age: {s}")
