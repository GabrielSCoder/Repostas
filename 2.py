def isPerfectSquare(x):
    s = int(x**0.5)
    return s*s == x
 
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

xx = int(input("digite um número para a pesquisa: "))

for i in range(1,xx+1):
    if xx == i:
         if (isFibonacci(i) == True):
             print (i,"Pertence a sequência")
         else:
             print (i,"Não pertence a sequência")