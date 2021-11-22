def merge_the_tools(a,k):
    a=list(a)
    count=0
    result=''
    #iterating thru list
    for i in a:
        if i not in result:
            #adding char to the string
            result=result+i
        #increasing the count
        count+=1
        #check if size of count is same as the limit given
        if count==k:
        #if yes print result and reinitialize count and result
            print(result)
            count=0
            result=''
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
