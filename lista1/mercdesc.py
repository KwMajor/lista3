mercadoria = float(input('Digite o valor da mercadoria: '))
desconto = float(input('Digite o valor do desconto: '))
v_desconto = mercadoria * desconto /100
p_final = mercadoria - desconto
print(f'O valor do desconto é de: {v_desconto}')
print(f'O valor a pagar é de: {p_final}')
