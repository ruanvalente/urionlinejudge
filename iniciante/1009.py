nome_vendedor = input()
salario_vendedor = float(input())
total_vendas = float(input())

total_mes = salario_vendedor + (total_vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(total_mes))