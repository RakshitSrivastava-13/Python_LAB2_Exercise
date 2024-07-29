import module_ListFunction as mlf



n=int(input("Enter the total length of list1:"))
list1=[]

for i in range(n):
    num=float(input("Enter a number:"))
    list1.append(num)
print(list1)


print("List 1:", list1)
print("Maximum:", mlf.find_max(list1))
print("Minimum:", mlf.find_min(list1))
print("Sum:", mlf.calculate_sum(list1))
print("Average:", mlf.compute_average(list1))
print("Median:", mlf.determine_median(list1))
print()

n=int(input("Enter the total length of list2:"))
list2=[]

for i in range(n):
    num=float(input("Enter a number:"))
    list2.append(num)
print(list2)

print("List 2:", list2)
print("Maximum:", mlf.find_max(list2))
print("Minimum:", mlf.find_min(list2))
print("Sum:", mlf.calculate_sum(list2))
print("Average:", mlf.compute_average(list2))
print("Median:", mlf.determine_median(list2))
print()

n=int(input("Enter the total length of list3:"))
list3=[]

for i in range(n):
    num=float(input("Enter a number:"))
    list3.append(num)
print(list3)

print("List 3:", list3)
print("Maximum:", mlf.find_max(list3))
print("Minimum:", mlf.find_min(list3))
print("Sum:", mlf.calculate_sum(list3))
print("Average:", mlf.compute_average(list3))
print("Median:", mlf.determine_median(list3))
print()

n=int(input("Enter the total length of list4:"))
list4=[]

for i in range(n):
    num=float(input("Enter a number:"))
    list4.append(num)
print(list4)

print("List 4:", list4)
print("Maximum:", mlf.find_max(list4))
print("Minimum:", mlf.find_min(list4))
print("Sum:", mlf.calculate_sum(list4))
print("Average:", mlf.compute_average(list4))
print("Median:", mlf.determine_median(list4))
