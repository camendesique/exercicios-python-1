a = float(input("Digite o primeiro coeficiente "))
b = float(input("Digite o segundo coeficiente "))
c = float(input("Digite o terceiro coeficiente "))

delta = (b * b) - (4*a*c)

if delta >= 0:
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    print (f"as raízes reais são {x1} e {x2}")
else:
    print (f"as raízes não são reais")

