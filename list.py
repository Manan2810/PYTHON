grocery=["rice","wheat","chocolate","potato"] #list of strings
grocery1=["rice","wheat","chocolate","potato",56] #mixed list [list of strings + numbers]
print(grocery)
print(grocery1)
numbers=[11,4,66,33,44,23]
# print(len(numbers)) ->tells the length of list numbers
# print(max(grocery))->returns the maximum value from the list
# print(min(grocery))->returns the minimum value from the list

#Accessing elements of list
print(grocery[0])
print(grocery[1])
print(numbers[0:5])
# list slicing
print(numbers[:]) # here the starting point default value is 0 and enp point default value is len(numbers)
print(numbers[1:4]) # in output we get a new string but it doesn't bring any changes to the orignal list
# print(numbers[start:end:step])->here default values are as start=0,end=0,step=1
print(numbers[::-1])
print(numbers)
# Funtions used with list

# .sort()-sort the list in increasing order and bring changes in actual list

# .reverse()-reverse the list and bring changes to orignal list

# numbers.append(4) add one value at the end of the orignal list(changes made in orignal list)
# print(numbers)
# print(len(numbers))

# numbers.insert(index,element)->syntax of insert function
# numbers.insert(2,89)
# print(numbers)

# numbers.remove(element in the list)->syntax
# numbers.remove(44)
# print(numbers)

# .pop()-remove elemnets from the end of the list
# numbers.pop()
# print(numbers)
# numbers.pop()
# print(numbers)

# tuples
# tuple are immutable
tp=(1,2,3,4)
print(tp)
# tp1=(1) here the element will be printed and not a tuple

# to print a single element tuple we will do this->tp1=(1,)
tp1=(1,)
print(tp1)