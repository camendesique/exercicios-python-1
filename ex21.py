N1 = float(input("Digite a primeira nota "))
N2 = float(input("Digite a segunda nota "))
N3 = float(input("Digite a terceira nota "))
N4 = float(input("Digita a quarta nota "))

media = (N1 + N2 + N3 + N4) / 4 

if media >= 6.00:
    print(f"APROVADO")
elif media >= 3.00 and media < 6.00:
    print(f"EXAME")
else:
    print(f"RETIDO")
