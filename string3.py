n=input("Enter the string:")
output=''
s=sorted(list(set(n)))
for x in s:
    output=output+str(n.count(x))+x
print(output)