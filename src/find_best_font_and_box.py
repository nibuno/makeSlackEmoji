# -*- coding: utf-8 -*-
from PIL import ImageFont
from src.bounding_box import BoundingBox
from typing import Tuple, Optional


def find_best_font_and_box(
        font_size: int,
        text: str,
        font: str,
        base_size: int
):
    image_font: Optional[ImageFont] = None
    bounding_box: Optional[Tuple[int, int, int, int]] = None
    while (bounding_box is None) or \
            (bounding_box[BoundingBox.RIGHT.value] > base_size) or \
            (bounding_box[BoundingBox.BOTTOM.value] > base_size) \
            and (font_size > 0):
        image_font = ImageFont.truetype(
            font=font,
            size=font_size
        )
        bounding_box = image_font.getbbox(text=text)
        font_size -= 1
    return image_font, bounding_box
