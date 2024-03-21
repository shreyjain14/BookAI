from fpdf import FPDF


def write_pdf(book):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
