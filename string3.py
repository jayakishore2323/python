n=input("Enter the string:")
output=''
s=sorted(list(set(n)))
for x in s:
    output=output+x+str(n.count(x))
print(output)