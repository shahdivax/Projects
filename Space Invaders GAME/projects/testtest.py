a = int(input())
'''
def getInvCount(ar, n):
  
    inv_count = 0
    for i in range(n):
        for j in range(i + 1 , n):
            if (ar[i] > ar[j]):
                inv_count+=1
                
  
    return inv_count 
'''



q=0
while q < a: 
    arr=[]
    n = int(input())
    l=0
    q+=1
    while l < n :
        b = list(map(int,input().split()))
        arr.append(b)
        #for k in b:
            #ar.append(k)
        l+=1
    # Python3 program to count the number of inversion
    # pairs in a 2D matrix
    
    # for simplicity, we are taking N as 4
    N = n
    
    # Function to update a 2D BIT. It updates the
    # value of bit[l][r] by adding val to bit[l][r]
    def update(l, r, val, bit):
        i = l
        while(i <= N):
            j = r
            while(j <= N): 
                bit[i][j] += val
                j += j & -j
            i += i & -i
    
    # function to find cumulative sum upto
    # index (l, r) in the 2D BIT
    def query(l, r, bit):
        ret = 0
        i = l
        while(i > 0):
            j = r
            while(j > 0):
                ret += bit[i][j]
                j -= j & -j
            i -= i & -i
        
        return ret
    
    # function to count and return the number
    # of inversion pairs in the matrix
    def countInversionPairs(mat):
        
        # the 2D bit array and initialize it with 0.
        bit = [[0 for i in range(N + 1)] for j in range(N + 1)]
        
        # v will store the tuple (-mat[i][j], i, j)
        v = []
        
        # store the tuples in the vector v
        for i in range(N):
            for j in range(N):
                
                # Note that we are not using the pair
                # (0, 0) because BIT update and query
                # operations are not done on index 0
                v.append([-mat[i][j], [i + 1, j + 1]])
        
        # sort the vector v according to the
        # first element of the tuple, i.e., -mat[i][j]
        v.sort()
        
        # inv_pair_cnt will store the number of
        # inversion pairs
        inv_pair_cnt = 0
        
        # traverse all the tuples of vector v
        i = 0
        while (i < len(v)):
            
            curr = i
            
            # 'pairs' will store the position of each element,
            # i.e., the pair (i, j) of each tuple of the vector v
            pairs = []
            
            # consider the current tuple in v and all its
            # adjacent tuples whose first value, i.e., the
            # value of –mat[i][j] is same
            while (curr < len(v) and (v[curr][0] == v[i][0])):
                
                # push the position of the current element in 'pairs'
                pairs.append([v[curr][1][0], v[curr][1][1]])
                
                # add the number of elements which are
                # less than the current element and lie on the right
                # side in the vector v
                inv_pair_cnt += query(v[curr][1][0], v[curr][1][1], bit)
                curr += 1
                
            # traverse the 'pairs' vector
            for it in pairs:
                x = it[0]
                y = it[1]
                
                # update the position (x, y) by 1
                update(x, y, 1, bit)
                
            i = curr
        
        return inv_pair_cnt
    
    # Driver code
    mat = arr
    
    inv_pair_cnt = countInversionPairs(mat)
    
    print(inv_pair_cnt)