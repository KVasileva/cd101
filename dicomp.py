def inp ():
    composers = {"Full_name":[], "birth_year":[], "death_year":[]}
    while True:  
        com_data = input("first name, last name, birth year, death year separated by space:\n").split(" ")
        fname = com_data[0] + " " + com_data[1]
        birth = int(com_data[2])
        death = int(com_data[3])
        composers["Full_name"].append(fname)
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
    for birth, death in zip(composers ["birth_year"], composers["death_year"]):
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
    for i, val in enumerate (composers["Full_name"]) :
        #print(f"Name {i}: {val}, {composers["Vitality"][i]}")

comp= []
comp = inp()
comp = age(comp)
comp = avage(comp)
print (comp)
#printcomp (comp)