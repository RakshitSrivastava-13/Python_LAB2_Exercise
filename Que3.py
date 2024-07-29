def merging_Dict(*args):
    """Merges multiple dictionaries into one."""
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def common_keys(*args):
    """Finds common keys in multiple dictionaries."""
    if not args:
        return set()
    
    common = set(args[0].keys())
    for dictionary in args[1:]:
        common.intersection_update(dictionary.keys())
    
    return common

def invert_dict(d):
    """Inverts a dictionary, swapping keys and values.
    If multiple keys have the same value, group these keys in a list.
    """
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

def common_key_value_pairs(*args):
    """Finds common key-value pairs across multiple dictionaries."""
    if not args:
        return set()
    
    common = set(args[0].items())
    for dictionary in args[1:]:
        common.intersection_update(dictionary.items())
    
    return common

# Example usage:

# Initialize an empty dictionary
dict1 = {}
print("Enter key-value pairs for the dictionary1. Type 'done' when finished.")        # Prompt the user to enter key-value pairs
while True:
    key = input("Enter key (or type 'done' to finish): ")                            # Get the key from the user
    if key.lower() == 'done':
        break
    
    value = input("Enter value: ")                                                   # Get the value from the user
    dict1[key] = value                                                               # Add the key-value pair to the dictionary
print("The dictionary1 you entered is:", dict1)                                   # Print the resulting dictionary                  


dict2 = {}
print("Enter key-value pairs for the dictionary2. Type 'done' when finished.")        # Prompt the user to enter key-value pairs
while True:
    key = input("Enter key (or type 'done' to finish): ")                            # Get the key from the user
    if key.lower() == 'done':
        break
    
    value = input("Enter value: ")                                                   # Get the value from the user
    dict2[key] = value                                                               # Add the key-value pair to the dictionary
print("The dictionary2 you entered is:", dict2) 


dict3 = {}
print("Enter key-value pairs for the dictionary3. Type 'done' when finished.")        # Prompt the user to enter key-value pairs
while True:
    key = input("Enter key (or type 'done' to finish): ")                            # Get the key from the user
    if key.lower() == 'done':
        break
    
    value = input("Enter value: ")                                                   # Get the value from the user
    dict3[key] = value                                                               # Add the key-value pair to the dictionary
print("The dictionary3 you entered is:", dict3) 

# (a) Merging dictionaries
merged = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# (b) Finding common keys
common_keys_result = common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)

# (c) Inverting a dictionary
dict4 = {}
print("Enter key-value pairs for the dictionary4. Type 'done' when finished.")        # Prompt the user to enter key-value pairs
while True:
    key = input("Enter key (or type 'done' to finish): ")                            # Get the key from the user
    if key.lower() == 'done':
        break
    
    value = input("Enter value: ")                                                   # Get the value from the user
    dict4[key] = value                                                               # Add the key-value pair to the dictionary
print("The dictionary4 you entered is:", dict4) 
inverted = invert_dict(dict4)
print("Inverted Dictionary:", inverted)

# (d) Finding common key-value pairs
common_pairs = common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)
