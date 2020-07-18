#!/usr/bin/env python
# coding: utf-8
print('''by Fábio Guimarães
© Copyright 2020. All Rights Reserved.
''')
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import tkinter
from tkinter import filedialog

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)
        #print(interpreter.process_page(page))
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

root = tkinter.Tk()
root.withdraw()
file_path = tkinter.filedialog.askopenfilename(title='Selecione um Aquivo', filetypes=(("Arquivo PDF", '*.pdf'), ("Todos arquivos", "*.*")))
print(convert_pdf_to_txt(file_path))

arquivo = open(file_path[:len(file_path) - 4] + '.txt', 'a', encoding='utf-8')
arquivo.writelines('{}\n'.format(convert_pdf_to_txt(file_path)))
arquivo.close()