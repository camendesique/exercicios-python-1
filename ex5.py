A = float(input ("Digite o coeficiente A"))
B = float(input ("Digite o coeficiente B"))
C = float(input ("Digite o coeficiente C"))

delta = (B * B) - (4*A*C)
x1 = (-B + delta) / (2*A)
x2 = (-B - delta) / (2*A)

print (f"A raiz 1 é {x1} e a raiz 2 é {x2}")