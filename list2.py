names= []
ages= []
age_sum=0
while True:
    data = input("Enter name and age separeted with space: ").split( )
    names.append(data[0])
    ages.append(int(data[1]))
    #age_sum = age_sum+ int(data[1])
    status  = input ("Would you like to continue? If yes press Y, if no press N  ")
    if status == "N":
        break
#avg_age =  age_sum/len(ages)
avage = int(sum(ages)/len(ages))
for idx, val in enumerate(names):
    print (f"Users {idx}: {val}, {ages[idx]}")  
print (f"Averade age: {avage}")

# x=11
# if x%2==0 :
#     print("x is even")
# else:
#     print("x is not even")

# lst = [1, 289, -84, 4, 3, 8,-9]
# for i in lst:
#     if i%2==0:
#         print (f"{i} even")
#     elif i%3==0:
#         print(f"{i} %3 true")
#     else:
#         print(f"{i} not even")

# for i in lst:
#     if i%2==0 and i>0:
#         print (f"{i} is even and >0")
#     else:
#         print(f"{i} is not")

# evn = []
# nevn = []
# for i in lst:
#     if i%2==0:
#         evn.append(i)
#     else:
#         nevn.append(i)

# print (f"{evn} is even, {nevn} is not")