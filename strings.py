mystr="Harry is a gOod boy"
# printing of string , printing at particular index and printing characters between two indices
# # print(mystr)
# print(mystr[4])
# print(mystr[0:5])

#length function of string(len())
# n=len(mystr) # length function len() tells the length of the string
# print(n)
# print(mystr[0:n])
# m=len(mystr[2:8])
# print(m)
# # print(mystr[78]) will give error
# print(mystr[0:78]) # will not give error
# print(mystr[0:5:2]) #print(mystr(start:stop:step))
# print(mystr[0::2])
# # print(mystr[start:end:step]) -> default values start=0,end=len(mystr),step=1


# # negative indices traversal
# newstr= "my name is salman khan"
# print(newstr[-4:-2:1]) # negative value of step traverse the string in the reverse direction
# print(mystr[::-1])


# # functions used with string

# # 1-> .isalnum()-
# # true conditions-> alnumstr="thth",alnumstr="2323",alnumstr="2323abcd"
# # false conditions-> alnumstr="678 abc"  if space is introduced between number and character it returns false
#
#
# print(mystr.isalnum())
# # print(alnumstr.isalnum())
#
#
# # 2-> .isalpha()-
# # true-> str="hhthht"
# #false-> str="233strg",str="h amm",str="man33 3"
# str="helloji"
# print(str.isalpha())

# 3-> .endswith(last word of string)
# print(mystr.endswith(""))

# 4-> .count() function - count the character/word/letter occured in the parent string
# print(mystr.count("y")) # here parent string is mystr and it has 2 y letters.

# 5-> .capitalize() function-  it captitalizes the first letter of the given string if it is a lower character
# print(mystr.capitalize())


# 6-> .find()
# print(mystr.find(" b"))

# 7-> .lower()
# print(mystr.lower())

# 8-> .upper()
# print(mystr.upper())

# 9-> .replace(part of strung u want to replace, string with whih u want to replace)
# print(mystr.replace("is","are"))
