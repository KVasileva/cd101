com_data = []
com_list = []
age=[]
a=0
n = int(input("Enter number of composers: "))
for m in range (n):
    com_data = input("First Name, Last Name, Birth Age, Death Age separated by space:\n").split(" ") 
    com_list.append(com_data)
#print (com_list)
for i in range (n):
    #for j in (0,i):
    for j in com_data:
        a = int(com_data[3])-int(com_data[2])
        age.append(a)

print (f"First Name: {com_list[i][0]}, Last Name: {com_list[i][1]}, Age:  {age}")