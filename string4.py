n='a4k3b2'
i=0
out=''
for x in n:
    if x.isalpha():
        tem=x
    else:
        dig=int(x)
        out=out+tem+chr(ord(tem)+dig)
print(out)