from PIL import Image, ImageDraw, ImageFont


image = Image.open("bilde.jpg") # Image

draw = ImageDraw.Draw(image) # The ImageDraw module provides simple 2D graphics for Image objects

font = ImageFont.truetype("Antonio-Regular.ttf", size=150) # Load font

W, H = image.size # Get image size


def draw_text(text, draw):
    text_w, text_h = draw.textsize(text, font) # Get text size

    (x, y) = ((W - text_w)/2 + 10, (H - text_h)/2 + 20) # Text shadow coordinates

    color = '#000000' # Shadow color (black)

    draw.text((x, y), text, fill=color, font=font) # Draw shadow on image

    (x, y) = ((W - text_w)/2, (H - text_h)/2)  # Text coordinates

    color = '#ffffff' # Text color

    draw.text((x, y), text, fill=color, font=font) # Draw text on image


msg = input("Type some text: ")
draw_text(msg, draw)

image.save('tests.png')
image.show()
