#Q.Count tuple occurance in list of tuples:

l1=[(2,3,4,5,6,7,8),(6,7,4,3,2),"HEMA",(6,7,4,3,2),"MOKS",(1,2,3,4),"NIKKI",(4,6,8,9),(6,7,4,3,2),(1,2,3,4,5)]
x=set(l1)
for i in x:
    print(l1.count(i))
