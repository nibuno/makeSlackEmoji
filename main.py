# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def main():
    file_name = "file" + ".png"
    im = Image.new("RGB", (256, 256), "#fff")
    draw = ImageDraw.Draw(im)
    font = None

    text = "Yumihiki\nKICK BACKScrapbox"

    font_path = "/Users/tatsuya/Library/Fonts/rounded-mplus-1c-black.ttf"

    base_size = 256
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
            print(size)
            font_size -= 1
            print(font_size)
        draw.multiline_text(
            xy=(0, (split_size / 2) * count),
            text=text,
            fill="#000",
            font=font,
            anchor="lm",
            align="center",
        )
        count += 2
    im.save(file_name)


if __name__ == '__main__':
    main()
