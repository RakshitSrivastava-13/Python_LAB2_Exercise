def add_element(s, element):                        #Function to add an element in a set.
    s.add(element)
    return s

def remove_element(s, element):                     #Function to remove an element from a set.
    s.discard(element)
    return s

def union_and_intersection(s1, s2):                 #Function to return union and intersection of two sets.
    return s1.union(s2), s1.intersection(s2)

def difference(s1, s2):                             #Function to return difference(s1-s2) of two sets.
    return s1.difference(s2)

def is_subset(s1, s2):                              #Function to check s1 is subset of s2 or not.
    return s1.issubset(s2)

def set_length(s):                                  #Function to return length of a set.
    count = 0
    for i in s:
        count += 1
    return count

def symmetric_difference(s1, s2):                    #Function to return symmetric difference of two sets.
    return s1.symmetric_difference(s2)

def power_set(s):                                     #Function to calculate power set.
    from itertools import chain, combinations
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def unique_subsets(s):                                #Function to get all unique subsets.
    from itertools import chain, combinations
    return set(frozenset(subset) for subset in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
