s=set()
s_from_list=set([1,2,3,4])
print(s_from_list)
# adding element to the set
s.add(1)
s.add(2)
s.add(2)
# here we added 2 two times but only one time it will be added as in sets duplicacy is not allowed
print(s)
# .union function
s1=s.union({5,6,7})
print(s,s1)
s3=set([2,3,6,1])
print(s3)
print(s1.intersection(s3))
print(len(s3))