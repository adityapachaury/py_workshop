my_set = {1, 2, 3, 4}
#add ele.
my_set.add(5)
print(my_set)

##union
myset = {5, 6, 7}
a = my_set.union(myset)
print(a)

#intersection
myset1 = {1, 5, 3}
b = my_set.intersection(myset1)
print(b)

#difference
myset2 = {2, 4, 6, 8}
c = my_set.difference(myset2)
print(c)

#remove ele.
my_set.remove(1)
my_set.discard(5)
print(my_set) 

def find_intersection(set1, set2):
    intersection = set1.intersection(set2)
    return intersection
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
intersection = find_intersection(set1, set2)
print(intersection)
