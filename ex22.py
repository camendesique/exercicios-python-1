x = int(input("Digite o primeiro valor "))
y = int(input("Digite o segundo valor "))

if x == y:
    print(f"Inválido. Os números são iguais")
elif x > y:
    print(f"A ordem crescente é {y}, {x}")
else:
    print(f"A ordem crescente é {x}, {y}")
