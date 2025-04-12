from PIL import Image
from fpdf import FPDF

image_files = ["assets/sample_image.jpg",
                "assets/sample_image_2.jpg",
                  "assets/sample_image_3.jpg",
                    "assets/sample_image_4.jpg",
                      "assets/sample_image_5.jpg",
                        "assets/sample_image_6.jpg"
                        ]  

pdf = FPDF()
for img in image_files:
    image = Image.open(img)
    pdf.add_page()
    pdf.image(img, x = 10, y = 10, w = 190 )  

pdf.output("sample.pdf")

