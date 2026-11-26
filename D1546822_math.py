def fun(n,b):
    if n<b:
        return n
    else:
        return str(fun(n//b,b))+str(n%b)
def isPrime(n)->bool:
    flag = True
    if n>1:
        for i in range(2,n//2):
            if n%i==0:
                flag = False
                break
    return flag
def tArea(n,h)->float:
    return (n*h/2)
def ed(x1,y1,x2,y2)->float:
    return ((x1-x2)**2+(y1-y2)**2)**0.5
if __name__=="__main__":
    print(ed(2,1,7,3))
    print(f"isPrime={isPrime(17)}")