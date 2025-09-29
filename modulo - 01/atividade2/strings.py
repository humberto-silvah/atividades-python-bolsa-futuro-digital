palavras = []
contaA = contaPalindromo = contaLonga = contaComun = 0

def testePalavras(teste):
    global contaA
    global contaPalindromo
    global contaLonga
    global contaComun

    teste = teste.lower().split()
    for i in teste:
        print(f"{i}:", end=" ")
        if (i[0] != "a") and (len(i) < 7) and (i[0] != i[-1]):
            contaComun += 1
            print("Palavra Comun")


        if i[0] == "a":
            contaA += 1
            print("Começa com A,", end=" ")


        if len(i) >= 7:
            contaLonga += 1
            print("Palavra longa")


        if i == i[::-1]:
            contaPalindromo += 1
            print("É palindromo")

def resumo(teste):
    print(
        f'\n\nResumo:\nPalavras que começam com "A": {contaA}\nPalindromos: {contaPalindromo}\nPalavras longas: {contaLonga}\nPalavras comuns: {contaComun}'
    )

# palavra = input('Digite palavras separadas por espaço: ')
palavras = "ana casa programacao ovo abacaxi mario computador ovo"

testePalavras(palavras)
resumo(palavras)