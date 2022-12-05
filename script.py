#!/usr/bin/python
import os
import sys
import subprocess
#check treepoem is installed or not
try:
    import treepoem
except ImportError:
    print("treepoem is not installed. Installing treepoem...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'treepoem'])
    import treepoem
#check pillow is installed or not
try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pillow'])
    from PIL import Image 

number=input("Enter the barcode number: ")
# number="92055900999723139098064168"
image = treepoem.generate_barcode(
    barcode_type="code128",  # One of the BWIPP supported codes.
    data=number,
)
image.convert("1").save("temp_barcode.png")

#change the size of the barcode
img = Image.open('temp_barcode.png')
img = img.resize((600, 110), Image.Resampling.LANCZOS)
output_file = "{}.png".format(number)
img.save(output_file)

#remove the barcode file
os.remove('temp_barcode.png')