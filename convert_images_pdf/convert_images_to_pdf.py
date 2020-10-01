#Credits: https://www.instagram.com/python.hub/

from os import listdir
from fpdf import FPDF

files_path = "D:\\Downloads\\Images\\"
image_list = listdir(files_path)
image_list.sort()
pdf = FPDF('P', 'mm', 'A4')
x = 0
y = 0
w = 210
h = 297

for image in image_list:
    pdf.add_page()
    pdf.image(files_path + image, x, y, w, h)

pdf.output("D:\\Downloads\\Images\\New_pdf_file.pdf", "F")
