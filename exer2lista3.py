usuario = str(input("usuario: "))
senha = str(input("senha: "))
while usuario == senha:
    print("erro")
    usuario = str(input("usuario"))
    senha = str(input("senha"))
print("usuario e senha correto!")
