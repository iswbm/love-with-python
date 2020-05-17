from PIL import Image, ImageDraw, ImageFont

font_size, text = 7, "我喜欢你！"
input_img_path = "/Users/MING/Github/love-with-python/girl.jpeg"
output_img_path = "/Users/MING/Github/love-with-python/girl.png"

img_raw = Image.open(input_img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', font_size)

def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

img_new.convert('RGB').save(output_img_path)