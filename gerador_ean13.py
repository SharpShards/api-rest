# Importações
import math as m


# Main
cod = 153057800009

print("Código = ", cod)
print(" ")


# - Multiplica os dígitos do código por 1 e por 3, alternando entre 1 e 3.

control = 1
sum = 0
ver = 0

for loop in str(cod):
    if(control%2 == 0):
        sum += int(loop) * 3
    else:
        sum += int(loop) * 1
    
    control += 1

ver = sum 


# - Divide a soma por 10.

ver = ver / 10


# - Arredondando o resultado para baixo.

ver = m.floor(ver)


# - Some 1 ao resultado da divisão.

ver += 1


# - Multiplique o resultado dessa soma por 10.

ver = ver * 10


# - Subtraia desse resultado o valor da soma inicial das multiplicações.

ver = ver - sum

# Verificador

print("Verificador =", ver)
print(" ")

# - O resultado da subtração é o dígito verificador.
# - Se o resultado for um múltiplo de 10 → O dígito verificador será 0.

if(ver > 9):
    ver = 0

# Junta tudo
ean = str(cod) + str(ver)

print("EAN = ", ean)