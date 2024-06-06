def shamel2or5(L):
    while L!=0:
        k=L%10
        if k!=2 and k!=5:
            return False
        L//=10
        return True
def function(n):
    for i in range(n):
        k=shamel2or5(i)
        if k:
            print(i)
x=int(input("number"))
function(x)

