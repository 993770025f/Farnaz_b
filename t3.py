def mean():
    counter=0
    sum=0
    i=0 
    while i!=1000 :
         i=int(input("number"))
         if i==1000 :
           break
         sum+=1
         counter+=1
    return ((sum-1000)/(counter-1))
print(mean())

