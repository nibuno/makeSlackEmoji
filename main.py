# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def main(text, font_color="#000000"):
    file_stem = "_".join(text.splitlines())
    file_suffix = ".png"
    file_name = file_stem + file_suffix
    background_color = (0, 0, 0, 0)
    base_size = 128
    center = base_size / 2
    image = Image.new(
        mode="RGBA",
        size=(base_size, base_size),
        color=background_color
    )
    image_draw = ImageDraw.Draw(im=image)
    image_font = None
    font_path = "rounded-mplus-20150529/rounded-mplus-1c-black.ttf"
    split_size = int(
        base_size / len(text.splitlines())
    )
    count = 1
    right = 2
    bottom = 3
    for text in text.splitlines():
        bounding_box = None
        font_size = split_size
        while (bounding_box is None) or \
                (bounding_box[right] > base_size) or \
                (bounding_box[bottom] > base_size) \
                and (font_size > 0):
            image_font = ImageFont.truetype(
                font=font_path,
                size=font_size
            )
            bounding_box = image_font.getbbox(text=text)
            font_size -= 1
        image_draw.text(
            xy=(center, (split_size / 2) * count),
            text=text,
            fill=font_color,
            font=image_font,
            anchor="mm",
        )
        count += 2
    image.save(fp=file_name)


if __name__ == '__main__':
    input_texts = [
        "hello\nworld",
        "H",
        "弓引",
        "ゆみひき",
        "Scrap\nBox"
    ]
    for input_text in input_texts:
        main(input_text)
