
se=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s=[]
t=int(input())
w = 1
ee = 0
e=t-1
while ee < t+(t-1):
    if ee > t-1 :
        c = se[w]
        s.append(c)
        w+=1
        e-=1
        ee+=1
        #print(ee)
    else:   
        c = se[e]
        s.append(c)
        e-=1
        ee+=1
        #print(ee)
#print(s)

d = t*3
if t%2==0:
    b =int((t)//2)
else:
    b =int((t-1)//2)
a= ((d-7)//2)
f=1
i=0
j=0
kk=-1
while f < t+1:
    ff = '-'.join(s[len(s)-i:])
    #ff = '-'.join(s[kk])
    if t%2==0: 
        x= (b*4)-(2*(j))-2
    else:
         x= (b*4)-(2*(j))   
    #x= (30//2)-(2*(i)-1)
    #while :
    if i == 0:
        y=str(*s[:1])
        z=('-'*x+y+ff+'-'*x)
    else:     
        y='-'.join(s[:i+1])
        z=('-'*x+y+'-'+ff+'-'*x)
    
    #print(x)
    
    print(z)
    f+=1
    i+=1
    j+=1
    kk-=1
#print(i)

k=i-2
ddd=0
j=1
while ddd < t-1:
    #x= (30//2)-(2*(i)-1)
    #aa='-'.join(s[:k-1])
    #aa='-'.join(s[:i-1])
    ff = '-'.join(s[len(s)-i+2:])
    #print(aa)
    xx=x+(2*(j))
    if i == 2:
        aa=str(*s[:1])
        z=('-'*xx+aa+ff+'-'*xx)
    else:     
        aa='-'.join(s[:i-1])
        z=('-'*xx+aa+'-'+ff+'-'*xx)
    #z=('-'*xx+aa+'-'+ff+'-'*xx)
    print(z)
    i-=1
    j+=1
    k-=2
    ddd+=1

#cc=input()    


#print('{1:{d}d}'.format(1,2,3,d=5))