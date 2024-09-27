dias = int(input('digite a quantidade de dias: '))
horas = int(input('digite a quantidade de horas: '))
minutos = int(input('digite a quantidade de minutos: '))
segundos = int(input('digite a quantidade de segundos: '))
resultado = 86400*dias + 3600*horas + 60*minutos + segundos
print(f'O total de tempo correspondete é de: {resultado} segundos!')