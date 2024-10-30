from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Title
        self.set_font("Arial", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)
        self.ln(10) 

    def footer(self):
        # Page footer
        self.set_y(-20)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f'Page {self.page_no()}', align="C")

# Get user input for the name
name = input("Enter your name: ")

# Create a PDF object
shirt = PDF(orientation="P", unit="mm", format="A4")
shirt.add_page()

# Load the shirt image
shirt.image("shirtificate.png", x=10, y=40, w=190)

# Set the font for the user's name
shirt.set_font("Arial", "B", 40)
shirt.set_text_color(255, 255, 255)

# Center the user's name on the shirt
name_width = shirt.get_string_width(name)

# Center horizontally above the shirt
shirt.set_xy((210 - name_width) / 2, 90)
shirt.cell(name_width, 20, name + " " + "took CS50", align="C")

# Save the output PDF
shirt.output("shirtificate.pdf")
