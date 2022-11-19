# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def main():
    text = "Hello\nWorld"
    file_stem = "_".join(text.splitlines())
    file_suffix = ".png"
    file_name = file_stem + file_suffix
    background_color = (0, 0, 0, 0)
    base_size = 256
    image = Image.new(
        mode="RGBA",
        size=(base_size, base_size),
        color=background_color
    )
    image_draw = ImageDraw.Draw(im=image)
    image_font = None
    font_path = "rounded-mplus-20150529/rounded-mplus-1c-black.ttf"
    split_size = base_size / len(text.splitlines())
    count = 1
    for text in text.splitlines():
        size = None
        font_size = 256
        while (size is None) or (size[2] > base_size) or (size[3] > base_size) \
                and (font_size > 0):
            image_font = ImageFont.truetype(
                font=font_path,
                size=font_size
            )
            size = image_font.getbbox(text=text)
            font_size -= 1
        image_draw.text(
            xy=(0, (split_size / 2) * count),
            text=text,
            fill="#000",
            font=image_font,
            anchor="lm",
            align="center",
        )
        count += 2
    image.save(fp=file_name)


if __name__ == '__main__':
    main()
