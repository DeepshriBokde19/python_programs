n = int ( input ("enter a number"))
print("natural number from" ,n,"-1 in reverse order")
while(n>=1):
    print (n)
    n-=1
#natural number in reverse order
#fibo
def fibo (n):
    if n<2:
        return n 
    return fibo(n-1)+fibo(n-2)
    print(fibo(4))
