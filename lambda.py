#!/bin/python

numbers = [1,2,5,7,8,10,12,13,15,18]
total=0
print(sum(map(lambda x:x**2,filter(lambda x: x%2==0,numbers)))
