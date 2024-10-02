from pdfminer.high_level import extract_text
from openpyxl import Workbook

#armazena todas as palavras do pdf em uma lista
lista = []

#cria variáveis para contagem dos alunos seguindo as características
branco, negro, pardo, amarelo, indigena = 0
jovem, adulto, idoso = 0

#extrai todas as palavras do pdf e armazena em uma lista
def extrair_texto_pdf(caminho_pdf):
        return lista.append(extract_text(caminho_pdf))

#faz a contagem etnica dos alunos seguindo os critérios explicitos na função
def contagem_etnica():
        for i in lista:
                if i == "BRANCO":
                        branco += 1
                if i == "NEGRO":
                        negro += 1
                if i == "PARDO":
                        pardo +=1
                if i == "AMARELO":
                        amarelo += 1
                if i == "INDIGENA":
                        indigena += 1


#faz a contagem etária dos alunos seguindo os critérios explicitos na função
def contagem_etaria():
        
        for i in lista:
                if i 