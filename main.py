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
    for i in range(24):
        pdf.line(10, 28 + (i * 10), 200, 28 + (i * 10))
    pdf.ln(227)
    pdf.set_font(family="Times", style="I", size=6)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(txt=row["Topic"], w=0, h=8, border=0, align="R", ln=1)
    for i in range(1, row["Pages"]):
        pdf.add_page()
        for i in range(28):
            pdf.line(10, 10 + (i * 10), 200, 10 + (i * 10))
        pdf.ln(268)
        pdf.set_font(family="Times", style="I", size=6)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(txt=row["Topic"], w=0, h=8, border=0, align="R", ln=1)
pdf.output("pdf_file")
