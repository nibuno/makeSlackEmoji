# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from src.calc_y_axis import calc_y_axis
from src.emoji import Emoji
from src.interface.image_generator import ImageGenerator
from typing import Tuple, Optional, List


class StandardGeneratorImpl(ImageGenerator):
    def __init__(self, text: str):
        self.emoji: Emoji = Emoji(text)
        self.bounding_right_num: int = 2
        self.bounding_bottom_num: int = 3

    def generate(self):
        image: Image = Image.new(
            mode="RGBA",
            size=(self.emoji.base_size, self.emoji.base_size),
            color=self.emoji.background_color
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        count: int = 1
        for text in self.emoji.text.splitlines():
            image_font: ImageFont = self._calc_font_size(
                self.emoji.get_split_size(),
                text,
                self.emoji.font,
                self.emoji.base_size
            )[0]
            image_draw.text(
                xy=(
                    self.emoji.get_center(),
                    (self.emoji.get_split_size() / 2) * count
                ),
                text=text,
                fill=self.emoji.font_color,
                font=image_font,
                anchor="mm",
            )
            count += 2
        image.save(fp=self.emoji.get_save_file_path())

    def _calc_font_size(self, font_size: int, text: str, font: str, base_size: int):
        image_font: Optional[ImageFont] = None
        bounding_box: Optional[Tuple[int, int, int, int]] = None
        while (bounding_box is None) or \
                (bounding_box[self.bounding_right_num] > base_size) or \
                (bounding_box[self.bounding_bottom_num] > base_size) \
                and (font_size > 0):
            image_font = ImageFont.truetype(
                font=font,
                size=font_size
            )
            bounding_box = image_font.getbbox(text=text)
            font_size -= 1
        return image_font, bounding_box


class AutoFontSizeChangeGeneratorImpl(ImageGenerator):
    def __init__(self, text: str):
        self.emoji: Emoji = Emoji(text)
        self.bounding_right_num: int = 2
        self.bounding_bottom_num: int = 3

    def generate(self):
        resize: int = self.emoji.base_size
        self.emoji.base_size = 128 * 2
        bounding_bottoms: List = []
        for text in self.emoji.text.splitlines():
            bounding_box = self._calc_font_size(
                self.emoji.get_split_size(),
                text,
                self.emoji.font,
                self.emoji.base_size
            )[1]
            bounding_bottoms.append(bounding_box[self.bounding_bottom_num])
        image: Image = Image.new(
            mode="RGBA",
            size=(self.emoji.base_size, sum(bounding_bottoms)),
            color=self.emoji.background_color
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        for i, text in enumerate(self.emoji.text.splitlines(), start=1):
            image_font: Tuple[int, int, int, int] = self._calc_font_size(
                self.emoji.get_split_size(),
                text,
                self.emoji.font,
                self.emoji.base_size
            )[0]
            image_draw.text(
                xy=(self.emoji.get_center(), calc_y_axis(bounding_bottoms, i)),
                text=text,
                fill=self.emoji.font_color,
                font=image_font,
                anchor="mm",
            )
        image: Image = image.resize((resize, resize))
        image.save(fp=self.emoji.get_save_file_path())

    def _calc_font_size(self, font_size: int, text: str, font: str, base_size: int):
        image_font: Optional[ImageFont] = None
        bounding_box: Optional[Tuple[int, int, int, int]] = None
        while (bounding_box is None) or \
                (bounding_box[self.bounding_right_num] > base_size) or \
                (bounding_box[self.bounding_bottom_num] > base_size) \
                and (font_size > 0):
            image_font = ImageFont.truetype(
                font=font,
                size=font_size
            )
            bounding_box = image_font.getbbox(text=text)
            font_size -= 1
        return image_font, bounding_box
