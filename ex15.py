cateto_oposto = float(input("Digite o valor do cateto oposto "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente "))

hipotenusa = ((cateto_oposto * cateto_oposto) + (cateto_adjacente * cateto_adjacente)) ** 0.5

print(f"O valor da hipotenusa é {hipotenusa}")