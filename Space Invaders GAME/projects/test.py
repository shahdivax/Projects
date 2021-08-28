if __name__ == '__main__':
    n = int(input())
    i = 0

    s ={}

    while i < n :
        a,b,c,d = input().split()
        stu_name={a:[]}
        w = float(b)+float(c)+float(d)
        f = w/3
        dd = ("%.2f" % f)
        #print(dd)
        stu_name[a].append(dd)
        s.update(stu_name)
    
        i+=1

    e = input()

    k = list(s)


    j = 0
    while True:
        
        if k[j] == e:
            x = list(s.values())
            print(*x[j])
            break
        else:
            j+=1
         
        
    




