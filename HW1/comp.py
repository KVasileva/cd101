com_data = []
com_list = []
age=[]
a=0
s=0
n = int(input("Enter number of composers: "))
for m in range (n):
    com_data = input("first name, last name, birth age, death age separated by space:\n").split(" ") 
    com_list.append(com_data)
for i in range (n):
    a = int(com_list[i][3])-int(com_list[i][2])
    age.append(a)
    print (f"first name: {com_list[i][0]}, last name: {com_list[i][1]}, age:  {age[i]}")
s = int(sum (age)/n)
print(f"Average age: {s}")

