#!/bin/python
def multiply(msg,*n):
        ans=1
        arr=list(n)
#        print(arr)
        if len(arr) == 0:
                print("no values passed")
                #ans=1
        else:
                for i in arr:
                	ans *=i
        return msg + str(ans)

print(multiply("The answer is:",4,9,7,8))
