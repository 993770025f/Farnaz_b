def mohasebat(a,b):
    x1=[]
    x2=[]
    for i in range(6):
        n1=a[i] + b[i]
        x1.append(n1)
        n2=a[i]-b[i]
        x2.append(n2)

    print("jam:",x1,"tafrigh:",x2)

l1=[]
l2=[]
for i in range(6):
   print("x**",{5-i})
   a=int(input("zarib="))
   l1.append(a)
for i in range(6):
   f=5
   print("x**",{5-i})
   b=int(input("zarib="))
   l2.append(b)
mohasebat(l1,l2)
