s = "Code"
def string_splosion(s):
    resp=""
    cont=1
    while cont <= len(s):
        resp = resp + s[0:cont]
        cont = cont +1
    return resp
print(string_splosion("Code"))




texto = "batatinha quando nasce"
lista = texto.split()
hifens = "-" .join(lista)
print(hifens)


def muda_data(data):
    data = data.split("-")
    data = data[::-1]
    return "/".join(data)
print(muda_data("2024-09-27"))



def muda_ddd(telefone):
    ddd, fone = telefone.split()
    ddd = ddd[1:-1]
    fone = fone.split("-")
    fone = "".split("-")
    return f"{ddd}-{fone}"
print(muda_ddd("(12) 3456-7890"))