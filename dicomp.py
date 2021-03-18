def inp ():
    trigger = True
    composers = {"Full_name":[], "birth_year":[], "death_year":[]}
    while trigger:  
        com_data = input("first name, last name, birth year, death year separated by space:\n").split(" ")
        fname = com_data[0] + " " + com_data[1]
        birth = int(com_data[2])
        death = int(com_data[3])
        composers["Full_name"].append(fname)
        composers["birth_year"].append(birth)
        composers["death_year"].append(death)
        status  = input ("Would you like to continue? If yes press Y, if no press N  ")       
        if status == "N":
            trigger = False

    
    return composers

    

def age (composers):
    composers ["Vitality"] = []
    for birth, death in zip(composers ["birth_year"], composers["death_year"]):
        a = death-birth
        composers ["Vitality"].append(a)
    return composers


def avage (composers):
    composers ["Average_age"] = [] #вношу в словарь ключ с одним элементом
    s=0
    for a in composers["Vitality"]:
        s = (s+a)
    d = s/len(composers["Vitality"])
    composers["Average_age"].append(d)
    print (composers)
    return composers

 def printcomp(composers):
     for key in composers.keys():
        for i, val in enumerate (composers["Vitality"]):
             print(f"Age {i}: {val}, {composers["Full_name"][i]}")
     #print(f"Average age: {composers["Average_age"]}")
     print([value for value in composers.values()][4]) # ???

#def printthem(composers):
 
comp = {"Full_name":["ab","bc","fd"], "birth_year":[20,30,50], "death_year":[60,90,350]}
#comp = inp()
comp = age(comp)
comp = avage(comp)
#comp = printthem(comp)
printcomp (comp)