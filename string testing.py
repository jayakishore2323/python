n=input("Enter alphanumeric string: ")
output=""
for x in n:
    if x.isalpha():
        ch=x
    else:
        dig=int(x)
        output=output+ch*dig
output=''.join(sorted(output))
print(output)

        