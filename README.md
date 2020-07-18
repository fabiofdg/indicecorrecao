#Índice de Correção
#!/usr/bin/env python
# coding: utf-8
print('''by Fábio Guimarães\n© Copyright 2020. All Rights Reserved.''')
import urllib.request, re, openpyxl
from urllib.request import Request, urlopen

def Luga(v1, v2, v3):
    l = sheet.max_row + 1
    sheet['A' + str(l)] = v1
    sheet['B' + str(l)] = v2
    sheet['C' + str(l)] = v3

criar_excel = openpyxl.Workbook()
sheet = criar_excel.active
sheet.title = 'A' + str(1)

Lugar = r'https://www.debit.com.br/tabelas/correcao-monetaria-trabalhista.php'
site = Request(Lugar, headers={'User-Agent': 'Mozilla/5.0'})
ponto = urllib.request.urlopen(site).read().decode('latin-1')

Buscar = re.compile("href='.*?(id=\d+)'\s+class='link1'>(.*?)<", re.I)
data = re.compile(r'<td>(\d+/\d{4})</td><td>\s?(\d,\d+)</td>', re.I)

guia = 1

for m in Buscar.findall(ponto):
    url = r"https://www.debit.com.br/tabelas/tabela-trabalhista-completa.php?" + m[0]


    print(url)
    url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(url).read().decode('latin-1')
    #print(data.findall(resp))
    for b in data.findall(resp):
        #print(m[1], b[0], b[1])
        Luga(m[1], b[0], b[1])
    guia =+ 1
    sheet = criar_excel.create_sheet('A' + str(guia), -1)

criar_excel.save(r'/content/drive/My Drive/Dados/INDICE.xlsx')
criar_excel = openpyxl.load_workbook(r'/content/drive/My Drive/Dados/INDICE.xlsx', keep_vba=True)
criar_excel.save(r'/content/drive/My Drive/Dados/INDICE.xlsm')
os.remove(r'/content/drive/My Drive/Dados/INDICE.xlsx')
