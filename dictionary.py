d1={}
# print(type(d1))
d2={"abc":"value1","def":"value2","ghi":"value3","jkl":"value4","mno":"value5","mnp":5}
print(d2)

# accessing elements in a dictionary
d3={"abc":"value1","abd":"value2","abe":{"manan":4,"manav":5}}
print(d3)
print(d3["abe"])
print(d3["abe"]["manan"])

# adding elements in a dictionary
d3["tre"]="value4"
d3["ert"]="value5"
print(d3)

# deleting element from the list
del d3["abc"]
print(d3)

# funtions used with dictionary
# 1. .copy()-copy one dictionary to another
print("dictionary d3",d3)
d4=d3.copy()
print("the copied dictionary is",d4)

# d5=d2; ->here d2 is not copied in d5 , so changes made in d5 will bring changes in d2.
d5=d2
del d5["abc"]
print(d2)

# 2. .get() function -> .get(key)->returns the corresponding value of the key
print(d2.get("def"))

# 3. .update()_ funtion
d3.update({"mnp":"pqrr"})
print(d3)

# 4. .key()
print(d2.keys())

#5. .item()
print(d2.items())

# <------------   Exercise  ------------->
# create a dictionry and take input from the user and return the meaning of the word from the dictioary
d1={"Disparate ":"of a distinct kind","Denigrate":"belittle someone","Construe":"interpret or assign meaning"}
keys=input("enter keys(Denigrate/Disparate/Construe)")
print("the meaning of the word is->",d1[keys])