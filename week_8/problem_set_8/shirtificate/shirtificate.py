# Week 8: Problem 3
# User input's their name, and change the text in that pdf file
# and output using fpdf2 a pdf file
from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__(orientation="portrait", format="A4")
        self.name = name

    def header(self):
        # add the CS50 Shirtificate line above the image in pdf file
        self.set_font('helvetica', '', 48)
        self.set_text_color(0, 0, 0)
        self.cell(0, 57, "CS50 Shirtificate", border=0, ln=1, align='C')

    def create_pdf(self):
        self.add_page()
        self.set_auto_page_break(auto=False)
        # Image in the middle of A4 page
        self.image('shirtificate.png', 10, 70, 190)
        # add user name on the image
        self.set_xy(10, 105)
        self.set_font('helvetica', '', 24)
        self.set_text_color(255, 255, 255)
        self.cell(190, 60, f'{self.name} took CS50', align='C')
        # output the pdf file
        self.output('shirtificate.pdf')


def main():
    name = input("Enter name: ").strip()
    shirt = Shirtificate(name)
    shirt.create_pdf()


if __name__ == "__main__":
    main()
