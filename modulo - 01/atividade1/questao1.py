def contadorDeLetras(frase):
    contVogal = contConsoante = 0
    frase.lower()

    for letra in frase:
        if letra.isalpha():
            if letra in "aeiou":
                contVogal += 1
            else:
                contConsoante += 1

    print(f"Vogais: {contVogal} | Consoantes: {contConsoante}")


frase = input("Digite a frase: ")
contadorDeLetras(frase)
