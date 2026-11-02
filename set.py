#sets are annoted by {} only separated by comma separated values or set()
#1. set are collection of unique items
#2. sets are hetrogenous
#3. as sets do not have indexing we cannot replace any value
#4. sets are unordered
#5. no duplicacy allowed
#empty{} -> dictionary but once we separate it with commas then its sets
#s=set() -> empty set
#dict->{1:20,3:30}
#set -> {20,30}
# s1 = {1,2,3,4,5,False,80.3,"sample"}
# #s2 = set () empty set

# a=22.78
# print(int(a))

# l=[1,1,2,3,4,4,5]
# print (set(l))

"""METHODS OF SET
.add() -> to add any element inside of set
s={1,1,2,3}
s.add(4)

#.remove() -> remove any element from the set
# s.remove(6)
# 
# .discard() -> if any is not present in the set it will not show any error
# s.discard (6)
# print(s)

SET OPERATIONS
1. UNION ->  merge both the sets
2. INTERSECTION -> common elements
3. DIFFERENCE -> ese elements jo ek set me ho pr dusre me nhi ho
4. SYMMETRIC DIFFERENCE -> common elements remove elements and gives us the incommon ones
s1 = {1,2,3,4}
s2 = {3,4,5,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.intersection(s2))


print(f"union -> {s1|s2}")
print(f"intersection -> {s1 & s2}") #& AND
print(f"difference -> {s1 - s2})
print(f"symmetric -> {s1^s2}")

#s=set()
s=frozenset{[1,2,3,4,5,]} -> when u want to have a set in which nothing can be added or subtracted then we make frozen set
s.add()
s.remove()
print(s)





"""
