tempo_percurso  = float(input("Digite o tempo do percurso "))
velocidade_media = float(input("Digite a velociade media no percurso"))

distancia  = velocidade_media * tempo_percurso

litros_gastos = distancia / 12

print(f"A quantidade de litros gastos na viagem é de {litros_gastos}")