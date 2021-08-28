
if __name__ == '__main__':
    n = int(input())
    i = 0 

    s=[]
    while i<n :
        x = list(map(str,(input().split)))
        i+=1

    if x[0] == "insert":
        a=int(x[1])
        b=int(x[2])
        s.insert(a,b)
    elif x[0] == "remove":
        s.remove(int(x[1]))

    elif x[0] == "append":
        s.append(int(x[1]))

    elif x[0] == "sort":
        s.sort()

    elif x[0] == "print":
        print(s)

    elif x[0] == "pop":
        s.pop()

    elif x[0] == "reverse":
        s.reverse


