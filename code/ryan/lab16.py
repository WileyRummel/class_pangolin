from PIL import Image
img = Image.open("Lenna_(test_image).png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = int(0.299*r + 0.587*g + 0.114*b)
   

        # your code here

        pixels[i, j] = (y, y, y)
img.show()