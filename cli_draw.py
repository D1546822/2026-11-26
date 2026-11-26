def fun1(n, c):
    for i in range(n):
        print(i+1,c)
fun1(3,'#')
def fun2(n,c):
    for i in range(n):
        for _ in range(i):
            print(c,end="")
        print()