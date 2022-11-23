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
        image_font = calc_font_size(
            base_size,
            bottom,
            font_path,
            image_font,
            right,
            split_size,
            text
        )[0]
        image_draw.text(
            xy=(center, (split_size / 2) * count),
            text=text,
            fill=font_color,
            font=image_font,
            anchor="mm",
        )
        count += 2
    image.save(fp=file_name)


# todo: 重複ロジックの切り出し
def auto_font_size_change(texts, font_color="#000000"):
    file_stem = "_".join(texts.splitlines())
    file_suffix = ".png"
    file_name = file_stem + file_suffix
    background_color = (0, 0, 0, 0)
    base_size = 128 * 2
    center = base_size / 2
    image_font = None
    font_path = "rounded-mplus-20150529/rounded-mplus-1c-black.ttf"
    right = 2
    bottom = 3
    bounding_bottoms = []
    for text in texts.splitlines():
        bounding_box = calc_font_size(
            base_size,
            bottom,
            font_path,
            image_font,
            right,
            base_size,
            text
        )[1]
        bounding_bottoms.append(bounding_box[bottom])
    image = Image.new(
        mode="RGBA",
        size=(base_size, sum(bounding_bottoms)),
        color=background_color
    )
    image_draw = ImageDraw.Draw(im=image)
    for i, text in enumerate(texts.splitlines(), start=1):
        image_font = calc_font_size(
            base_size,
            bottom,
            font_path,
            image_font,
            right,
            base_size,
            text
        )[0]
        image_draw.text(
            xy=(center, calc_y_axis(bounding_bottoms, i)),
            text=text,
            fill=font_color,
            font=image_font,
            anchor="mm",
        )
    resize_base = 128
    image = image.resize((resize_base, resize_base))
    image.save(fp=file_name)


def calc_font_size(
        base_size,
        bottom,
        font_path,
        image_font,
        right,
        font_size,
        text):
    bounding_box = None
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
    return image_font, bounding_box


def calc_y_axis(bounding_boxs, count):
    # TODO: メソッドへの切り出し
    # 1個の時は0が1個
    # 2個の時は0が2個, 1が1個
    # 3個の時は0が2個, 1が2個, 2が1個
    # 4個の時は0が2個, 1が2個, 2が2個, 3が1個
    if count == 1:
        return (bounding_boxs[0]) / 2
    elif count == 2:
        return (bounding_boxs[0] + bounding_boxs[0] +
                bounding_boxs[1]) / 2
    elif count == 3:
        return (bounding_boxs[0] + bounding_boxs[0] +
                bounding_boxs[1] + bounding_boxs[1] +
                bounding_boxs[2]) / 2


if __name__ == '__main__':
    input_texts = [
        "hello\nworld",
        "H",
        "ポプテ\nピピ\nック",
        "Hello",
        "ある\nある",
        "弓",
        "弓引",
        "ゆみひき",
        "Scrap\nBox"
    ]
    for input_text in input_texts:
        main(input_text)
        # auto_font_size_change(input_text)
