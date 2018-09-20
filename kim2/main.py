# distância entre dois pontos

import math

x1=int(input("Coordenada x1 de P1: "))
y1=int(input("Coordenada y1 de P1: "))
x2=int(input("Coordenada x2 de P2: "))
y2=int(input("Coordenada y2 de P2: "))

d = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

print("distância entre p1 e p2 é: ",d)

