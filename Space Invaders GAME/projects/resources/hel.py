def average(array):
    # your code goes here
    x = set(array)
    print(x)
    y = sum(x)
    z= len(x)
    
    return y/z 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)