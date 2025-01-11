import PyPDF2
a = PyPDF2.PdfFileReader('Gourav REsume.pdf')
print(a.documentInfo)