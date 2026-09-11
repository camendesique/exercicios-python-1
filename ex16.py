horas_trabalhadas = float(input("Digite as horas trabalhadas "))
valor_hora = float(input("Digite o valor da hora trabalhada "))
percentual_desconto = float(input("Digite o percentual de desconto "))
numero_dependentes = int(input("Digite o número de dependentes "))

calculo_salario = horas_trabalhadas * valor_hora
desconto = calculo_salario * (percentual_desconto / 100)
salario_liquido = (calculo_salario - desconto) + (numero_dependentes * 100)

print(f"O salário líquido é de {salario_liquido}")