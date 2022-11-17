# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def main():
    file_name = "file" + ".png"
    font_color = "#fff"
    base_size = 256
    image = Image.new("RGB", (base_size, base_size), font_color)
    image_draw = ImageDraw.Draw(image)
    font = None
    text = "Hello\nWorld"
    font_path = "/Users/tatsuya/Library/Fonts/rounded-mplus-1c-black.ttf"
    split_size = base_size / len(text.splitlines())
    count = 1
    for text in text.splitlines():
        size = None
        font_size = 100
        while (size is None
               or size[0] > base_size
               or size[1] > base_size) \
                and font_size > 0:
            font = ImageFont.truetype(font_path, font_size)
            size = font.getsize_multiline(text)
            font_size -= 1
        image_draw.multiline_text(
            xy=(0, (split_size / 2) * count),
            text=text,
            fill="#000",
            font=font,
            anchor="lm",
            align="center",
        )
        count += 2
    image.save(file_name)


if __name__ == '__main__':
    main()
