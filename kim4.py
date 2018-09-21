import math

a = float(input("informe valor de a: "))
b = float(input("informe valor de b: "))
c = float(input("informe valor de c: "))

if a>b>c:
    print("o maior número é",a, "e o menor número é",c)
if a<b<c:
    print("o menor número é",a, "e o maior número é",c)
if a>c>b:
    print("o maior número é",a, "e o menor número é",b)
if b>a>c:
    print("o maior número é",b, "e o menor número é",c)
if c>b>a:
    print("o maior número é",c, "e o menor número é",a)