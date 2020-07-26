n=input()
d={}
for i in n:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k,v)