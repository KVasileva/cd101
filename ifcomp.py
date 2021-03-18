
def inp ():
    composers = {"Fulname":[], "birth_year":[], "death_year":[] }
    while True:  
        com_data = input("first name, last name, birth year, death year separated by space:\n").split(" ")
        fname = com_data[0] + " " + com_data[1]
        birth = int(com_data[2])
        death = int(com_data[3])
        composers["Fulname"].append(fname)
        composers["birth_year"].append(birth)
        composers["death_year"].append(death)
        status  = input ("Would you like to continue? If yes press Y, if no press N  ")       
        if status == "N":
            break
        else:
            continue
    return composers

def age (composers):
    composers ["Vitality"] = []
    for birth, death in zip(composers ["birth_year"],composers ["death_year"]):
            a = death-birth
            composers ["Vitality"].append(a)
    return composers


def avage (composers):
    composers ["Average_age"] = []
    s=0
    for a in composers["Vitality"]:
        s = (s+a)/len(composers["Vitality"])
        composers["Average_age"].append(s)
    return composers

def printcomp(composers):
    for i, val in enumerate (composers["Fulname"]):
        print(f"Name {i}: {val}")

    # for i, val in enumerate (composers["Fulname"]):
    #     print(f"Name {i}: {val}, age: {composers["Vitality"][i]}")
    
    for v in (composers["Vitality"]):
        print(f"{v}")
    for c in (composers["Average_age"]):
            print(f"{c}")


comp = inp()
comp = age(comp)
comp = avage(comp)
printcomp(comp)



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