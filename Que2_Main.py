import Que2 as mso


set1 = input("Enter elements separated by spaces: ")
set1 = set(set1.split())
print("The set you entered is:", set1)

set2 = input("Enter elements separated by spaces: ")
set2 = set(set2.split())
print("The set you entered is:", set2)

# Add element
print("Original Set1:", set1)
x=int(input("Enter the element you wanna add:"))
set1 = mso.add_element(set1, x)
print(f"After adding {x}:", set1)
print()

# Remove element
print("Original Set2:", set2)
x=int(input("Enter the element you wanna remove:"))
set2 = mso.remove_element(set2, x)
print(f"After removing {x}:", set2)
print()

# Union and intersection
union, intersection = mso.union_and_intersection(set1, set2)
print("Union of Set1 and Set2:", union)
print("Intersection of Set1 and Set2:", intersection)
print()

# Difference
diff = mso.difference(set1, set2)
print("Difference of Set1 - Set2:", diff)
print()

# Subset check
is_sub = mso.is_subset({1, 2}, set1)
print("Is {1, 2} a subset of Set1:", is_sub)
print()

# Set length
length = mso.set_length(set1)
print("Length of Set1:", length)
print()

# Symmetric difference
sym_diff = mso.symmetric_difference(set1, set2)
print("Symmetric difference of Set1 and Set2:", sym_diff)
print()

# Power set
power_set = mso.power_set(set1)
print("Power set of Set1:", power_set)
print()

# Unique subsets
unique_subs = mso.unique_subsets(set1)
print("Unique subsets of Set1:\n", unique_subs)
print()
