n=input("Enter the string:")
output=''
for i in n:
    if i not in output:
        output+=i
for i in sorted(output):
    print(f"{i} present in string is {n.count(i)}")