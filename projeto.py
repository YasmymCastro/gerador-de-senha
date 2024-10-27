import random

senha = ""
caracteres = "zaqxswcdevfrbgtnhymjukilop0123456789!@#$%&*"
for digito in range(8):
    aleatorio = random.choice(caracteres)
    senha += aleatorio

print("-" * 20)
print(senha)
print("-" * 20)