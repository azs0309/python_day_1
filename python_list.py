#2	list.count(obj)
aList = [123, 'xyz', 'zara', 'abc', 123]
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

#3	list.extend(seq)
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print("Extended List : ", aList) 

#4	list.index(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
print("Index for xyz : ", aList.index( 'xyz' )) 
print("Index for zara : ", aList.index( 'zara' )) 

#5	list.insert(index, obj)
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print("Final List : ", aList)

#6	list.pop(obj=list[-1])
aList = [123, 'xyz', 'zara', 'abc']
print("A List : ", aList.pop(1))
print("B List : ", aList.pop(2))
print(aList)

#7	list.remove(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print("List : ", aList)
aList.remove('abc')
print("List : ", aList)

#8	list.reverse()
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print ("List : ", aList)

#9	list.sort([func])
aList = ['xyz', 'zara', 'abc', 'xyz']
aList.sort()
print("List : ", aList)

#Indexing, Slicing, and Matrixes
L = ['spam', 'Spam', 'SPAM!']
print(L[2])
print(L[-2])
print(L[1:])
