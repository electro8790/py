set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}


intersection_two = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_two}")


intersection_multiple = set1.intersection(set2, set3)
print(f"Intersection of set1, set2, and set3: {intersection_multiple}")