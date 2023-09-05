from rembg import remove
from PIL import Image

input_path = '/home/esaul/PycharmProjects/Parsing/PR_HUB/15142141.jpg'
output_path = '111.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
