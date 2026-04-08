import unicodedata
import textwrap
import os
from collections import Counter


# Trabalho em grupo
#
# Formar um banco de dados com diversos textos (66 textos por grupo)
# Analisar a probabilidade de letras que apareceram nos textos
# Juntar esses dados (cerca de 660 textos no total) para formar uma tabela de probabilidade
#
# Util para a analise criptografica de textos, em especial na lingua portuguesa.

def calcFrequencia(texto):
    # normaliza o texto
    texto_desmontado = unicodedata.normalize('NFD',texto)
    textoSemAcentos = ""
    for c in texto_desmontado:
        if unicodedata.category(c) != 'Mn':
            textoSemAcentos = textoSemAcentos+c

    textoSemAcentos = textoSemAcentos.upper()

    # Filtra so as letras (retira espacos, numeros e pontos)
    letrasValidas = []
    textoValido = ""
    for char in textoSemAcentos:
        if char.isalpha():
            letrasValidas.append(char)
            textoValido = textoValido+char
    # organiza o texto formatado em 120 colunas
    textoFormatado = textwrap.fill(textoValido,120)

    totalLetras = len(letrasValidas)

    # se a lista tiver vazia o script para
    if totalLetras == 0:
        print("Nenhuma letra valida foi encontrada no texto.")
        return

    # conta as vezes que uma letra aparece no texto
    contagem = Counter(letrasValidas)

    ####################################################################################################################
    # SALVAR COMO ARQUIVO
    nomeGrupo = "vigenere"
    lingua = input("Qual a lingua do texto? (Portugues, Ingles)\n")
    tipoTexto = input("Qual tipo de texto? (ILT - ILL - CLS - CLL - LMR - LMJ - LMC - LEP - LER - DPA - DPB)\n")
    nmrMembro = input("Qual seu numero de membro?\n")

    titulo = nomeGrupo + "_" + lingua + "_" + nmrMembro + "_" + tipoTexto + ".txt"
    titulo2 = nomeGrupo + "_" + lingua + "_" + nmrMembro + "_" + tipoTexto + "BRUTO.txt"

    # Diretorio de output (vai ser na mesma pasta do arquivo .py
    caminhoOutput = "Output"
    if not os.path.exists(caminhoOutput):
        os.makedirs(caminhoOutput)

    # Formatado
    with open(os.path.join(caminhoOutput,titulo), "w", encoding="utf-8") as arquivo:
        arquivo.write(textoFormatado)
    # Dados
    with open(os.path.join(caminhoOutput,titulo2),"w", encoding="utf-8") as arquivo2:
        arquivo2.write(textoSemAcentos + "\n\n")
        arquivo2.write(f"total de letras: {totalLetras}\n")
        arquivo2.write("Letra - Frequencia - Probabilidade\n")
        for let, qtd in contagem.most_common():
            prob = qtd/totalLetras
            arquivo2.write((f"{let} {qtd} {prob:.3f}") + "\n")

    print("Texto salvo na mesma pasta do codigo.")

    ####################################################################################################################
    # print dos resultados
    '''
    print(textoFormatado)

    print(f"Total de letras: {totalLetras}")
    print("Letra | Frequencia | Probabilidade")
    print("-"*30)

    for letra, quantidade in contagem.most_common():
        probabilidade = (quantidade/totalLetras)*100

        # o "^4" centraliza o texto no centro
        print(f"{letra} {quantidade: ^4} {probabilidade:.3f}%")
    '''


def workspace():
    print("Digite ou cole o texto. Para indicar que o texto acabou, aperte Enter em uma linha vazia!")

    # normalmente o texto vem com varios paragrafos
    # para evitar que o python exploda com os paragrafos
    # a gente faz um loop que junta esses paragrafos ate o input achar um "".

    textoComParagrafos = []
    while True:
        linha = input()
        if linha == "":
            break
        textoComParagrafos.append(linha)

    # para juntar os paragrafos de volta
    # ele faz um loop que adiciona um '\n' antes de um novo paragrafo na lista

    textoCompleto = "\n".join(textoComParagrafos)

    # chama a funcao com o texto

    calcFrequencia(textoCompleto)

if __name__ == "__main__":
    workspace()