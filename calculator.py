#calculator
a=int(input("enter first number:-"))
b=int(input("ener second number:-"))
operator=input("enter an operator(+,-,*,/,%)")
if operator =='+':
    print("sum is ",a+b)
elif operator =='-':
    print("difference is ",a-b)
elif operator =='*':
    print("product is ",a*b)
elif operator =='/':
    print("quotient is ",a/b)
elif operator =='%':
    print("remaoinder is ",a%b)
else:
    print("you opted a wrong operator")
