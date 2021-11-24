if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    res=[]
    # to remove duplicate element
    for i in arr:
        if i not in res:
            res.append(i)
    #sort list
    res=sorted(res)
    #by popping we will be removing largest element
    res.pop()
    #printing the second largest element remaining
    print(res[-1])
