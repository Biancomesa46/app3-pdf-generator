from fpdf import FPDF
import pandas

pdf = FPDF(orientation="p", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pandas.read_csv('topics.csv')


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(txt=row["Topic"], w=0, h=24, border=0, align="l", ln=1)
    pdf.line(10, 28, 200, 28)

    pdf.ln(245)
    pdf.set_font(family="Times", style="B", size=6)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(txt=row["Topic"], w=0, h=8, border=0, align="R", ln=1)
    for i in range(1, row["Pages"]):
        pdf.add_page()
        pdf.ln(268)
        pdf.set_font(family="Times", style="B", size=6)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(txt=row["Topic"], w=0, h=8, border=0, align="R", ln=1)
pdf.output("pdf_file")
