from rembg import remove
from PIL import Image

input_path = '/PR_HUB/Parser_tutorial/15142141.jpg'
output_path = '111.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
