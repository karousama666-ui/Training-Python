idade = 0
altura  = 0.0
nome = ""
eh_brasileiro = False


idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
nome = input("Digite seu nome: ")
eh_brasileiro = input("A pessoa é brasileira? (s/n): ").lower() == 's'


print("Idade Digitada: ", idade)
print("Altura Digitada: ", altura)
print("Nome Digitado: ", nome)
if eh_brasileiro:
    print("A pessoa é brasileira")
