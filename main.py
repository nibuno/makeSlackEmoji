# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def main():
    file_name = "file" + ".png"
    font_color = "#fff"
    base_size = 256
    image = Image.new(
        mode="RGB",
        size=(base_size, base_size),
        color=font_color
    )
    image_draw = ImageDraw.Draw(im=image)
    font = None
    text = "Hello\nWorld"
    font_path = "/Users/tatsuya/Library/Fonts/rounded-mplus-1c-black.ttf"
    split_size = base_size / len(text.splitlines())
    count = 1
    for text in text.splitlines():
        size = None
        font_size = 100
        while (size is None) or (size[2] > base_size) or (size[3] > base_size) \
                and (font_size > 0):
            font = ImageFont.truetype(
                font=font_path,
                size=font_size
            )
            size = font.getbbox(text=text)
            font_size -= 1
        image_draw.text(
            xy=(0, (split_size / 2) * count),
            text=text,
            fill="#000",
            font=font,
            anchor="lm",
            align="center",
        )
        count += 2
    image.save(fp=file_name)


if __name__ == '__main__':
    main()
