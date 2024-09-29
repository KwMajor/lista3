km_percorrido = float(input('Quantos KM foram percorridos: '))
dias_alugado = float(input('Quantos dias o carro ficou alugado: '))
p_km = km_percorrido * 0.15
p_dia = dias_alugado * 60
p_total = p_km + p_dia
print(f'O preço do aluguem do carro é de: R${p_total:.2f}')