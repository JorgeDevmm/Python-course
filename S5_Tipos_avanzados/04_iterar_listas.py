paises = ["Perú","Chile","Canada","Colombia","Ecuador","Argentina","Brasil","Venezuela","Bolivia"]

# for pais in paises:
#     print(pais, end=" ")

print("##############")    

# acceder elemneto de una lista con su indice
for pais in enumerate(paises):
    print(pais[1]) 

print("##############")    

for indice, pais in enumerate(paises):
    print(indice, pais) 


# print("##############")    

# for i in range(len(paises)):
#     print(f"{i}, {paises[i]}")
