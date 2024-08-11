
# texto = "Abba"
# texto = "Reconocer"
# texto = "Isaac no ronca asi"
texto = "Hola mundo"

# función de eliminiar espacios
def eliminar_espacios(texto):
    palabra_sin_espacios = ""

    for letra in texto.lower():
        if letra != " ":
            palabra_sin_espacios += letra

    return palabra_sin_espacios

# función para poner en reversa la palabra
def reversa_palabra(texto_nuevo):

    texto_reversa = ""
    longitud = len(texto_nuevo)

    for i in range(longitud-1, 0 -1,-1):
       texto_reversa += texto_nuevo[i]
    return texto_reversa
      

def es_palindromo(texto):
    validacion = True

    # resultado de texto eliminando espacios
    texto_nuevo = eliminar_espacios(texto)
    longitud = len(texto_nuevo)

    # resultado de texto en reversa
    texto_reversa = reversa_palabra(texto_nuevo)

    for i in range(longitud -1):
        if texto_nuevo[i] == texto_reversa[i]:
            validacion =True
        else:
            validacion = False    
        
    return validacion

print(f"{texto}, {es_palindromo(texto)} ")


    




