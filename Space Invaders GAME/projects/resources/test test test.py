if __name__ == '__main__':
    t={}
    x=int(input())
    i=0
    while i<x:

        name = input()
        s={name:[]}
        score = float(input())
        s[name].append(score)
        
        t.update(s)
        i+=1
    
    a=list(t.values())
    ss=set()
    jj=0
    for k in a:
        o = a[jj]
        for l in o:
            dd = o[0]
            ss.add(dd)
            jj+=1
    print(ss)        
    x = list(ss)
    xx= ss[0]
    print(x)
    
    cc=[]
    ccc=[]
    cc.append(x)
    ccc.append(cc)
                 
                
        
        
        
   
    print(ccc)
    print(a)
    '''
    d= list(t)
   
    y= []
    
    j = 0
    while True:
        
        if a[j] == ccc[0]:
            sortedDict = dict( sorted(t.items(), key=lambda x: x[0].lower()) )
            keys = [k for k, v in sortedDict.items() if v == a[1]]
            
            n = 0
            for l in keys:
                print(''.join(keys[n]))
                n+=1
                
            
            
            break
        else:
            j+=1  
    
        
            
    '''

            
