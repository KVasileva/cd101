def sum_foo (ages):
    s=0
    for age in ages:
        s = s+age
    avg = s/ len (ages)
    return avg

print (sum_foo([1, 23, 56, 5, 5]))
print (sum_foo([1, 25, 6, 51, 5]))



# def first (a,b,c):
#     z = a+b+c
#     return z

# zo = first(1,2,5)
# print (zo)



# def first ():
#     print ("Hello")
# first()

# def first (x,y):
#   a = x+y
#     print (a)
# first (39, 88)
# first (60, 88)