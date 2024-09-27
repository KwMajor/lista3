salario = int(input('Digite o seu salário: '))
a_salario = salario * int(input('Digite quantos % o seu salário aumentou: ')) / 100 
print(f'O valor do aumento do salário é de: R${a_salario}')
print(f'O novo valor do salário é de: R${salario + a_salario}')