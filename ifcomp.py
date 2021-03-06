

def inp ():
    names=[]
    ages=[]
    com_data1 = []
    com_data1 = input("first name, last name, birth age, death age separated by space:\n").split(" ")
    names.append(com_data1)
    a = int(com_data1[3])-int(com_data1[2])
    ages.append(a)
    return (f"{names}, {ages}")

def wultc ():     
    while True:          
        com = inp()             
        status  = input ("Would you like to continue? If yes press Y, if no press N  ")        
        if status == "N":
            break
        else:
            continue


print (inp())




#com_data = input("first name, last name, birth age, death age separated by space:\n").split(" ")


# for idx, val in enumerate(names):
#      print (f"User {idx}: {val}, {ages[idx]}")

# for i in range (n):
#     a = int(com_list[i][3])-int(com_list[i][2])
#     age.append(a)
#     print (f"first name: {com_list[i][0]}, last name: {com_list[i][1]}, age:  {age[i]}")
# s = int(sum (age)/n)
# print(f"Average age: {s}")