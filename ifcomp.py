def inp ():
    while True:  
        composers = {"Full name":[], "birth year":[], "death year":[] }
        com_data = input("first name, last name, birth year, death year separated by space:\n").split(" ")
        fname = com_data[0] + " " + com_data[1]
        birth = int(com_data[2])
        death = int(com_data[3])
        composers["Full name"].append(fname)
        composers["birth year"].append(birth)
        composers["death year"].append(death)
        status  = input ("Would you like to continue? If yes press Y, if no press N  ")       
        if status == "N":
            break
        else:
            continue
    return composers

def age (composers):
    composers ["Vitality"] = []
    for birth, death in zip(composers ["birth year"], composers["death year"]):
        a = death-birth
        composers ["Vitality"].append(a)
    return composers


def avage (composers):
    composers ["Average age"] = []
    s=0
    for a in composers["Vitality"]:
        s = s+a
        composers["Average age"].append(s)
    return composers

comp = inp()
comp = age(comp)
comp = avage(comp)
print (comp)




#for i in c:
    #composers = {"name"[], "age"[]}
    #composers["name"].append("c[i][1]")
    #  a = int(c[i][3])-int(c[i][2])
    #composers["age"]. append (a)


#  a = int(com_data[3])-int(com_data[2])
#     ages.append(a)

# for idx, val in enumerate(names):
#      print (f"User {idx}: {val}, {ages[idx]}")

# for i in range (n):
#     a = int(com_list[i][3])-int(com_list[i][2])
#     age.append(a)
#     print (f"first name: {com_list[i][0]}, last name: {com_list[i][1]}, age:  {age[i]}")
# s = int(sum (age)/n)
# print(f"Average age: {s}")