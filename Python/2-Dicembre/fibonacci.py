#fibonacci
i=0
r=1
tmp=1
nvol=23
print(r)
print(r)
def fibonacci(a,b):
    r=a+b
    return r
while i<nvol:
    tmp=fibonacci(r,tmp)
    print(tmp)
    r=tmp-r
    i=i+1
