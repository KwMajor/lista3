c_dias = float(input('Quantos cigarros você fuma por dia:'))
c_anos = float(input('A quantos anos você fuma: '))
t_dias = c_dias * 10
t_anos = c_anos * 365
t_perdido = t_dias * t_anos /60
print(f'O tempo perdido por fumar foi de: {t_perdido} horas')