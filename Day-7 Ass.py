#Day-7 Ass


#1.Append
elements = [10,20,30,40,50]

print("before", elements)
elements.append(60)
print("after append", elements)


#2.insert
elements.insert(1,15)
print("after insert", elements)

#3.remove
elements.remove(60)
print("after removing 60", elements)

#4.pop
result= elements.pop(1)
print("after pop", elements, "poped element is", result)



#5.negative index can also be supported
elements = [10,20,30,40,50]

print( '  elements[-1]  ', elements[-1] )
print( '  elements[-5]  ', elements[-5] )


#6.ordered collection
elements=[10,20,30,40,50]
print( elements )

#7.reverse

elements = [ 10,20,30,40,50,60, 70,80,90,100 ]
print(  'elements[9:  :-1]', elements[9:  :-1] )


#8.
print( ' elements[0:8:2] ', elements[0:10:2])# 0,2, 4, 6, =10,30, 50, 70



#9. duplicates  are allowed
elements = [ 10, 20,30, 'arjun', 10.5, 10,20,30 ]
print( ' elements ' , elements )
