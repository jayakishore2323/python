n=input("Enter the string: ")
previous=n[0]
c=1
i=1
output=''
while i < len(n):
    if n[i] == previous:
        c+=1
    else:
        output=output+str(c)+previous
        previous=n[i]
        c=1
    if i == len(n) -1:
        output=output+str(c)+previous
    i+=1
print(output)