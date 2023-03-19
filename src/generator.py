# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from src.calc_y_axis import calc_y_axis
from src.entity.bounding_box import BoundingBox
from src.find_best_font_and_box import find_best_font_and_box
from src.interface.image_generator import ImageGenerator
from src.use_case.emoji_use_case import EmojiUseCase
from typing import Tuple, List


class StandardGeneratorImpl(ImageGenerator):
    def __init__(self, emoji_use_case: EmojiUseCase):
        self.emoji_use_case: EmojiUseCase = emoji_use_case

    def generate(self):
        image: Image = Image.new(
            mode="RGBA",
            size=(self.emoji_use_case.get_base_size(),
                  self.emoji_use_case.get_base_size()),
            color=self.emoji_use_case.get_background_color()
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        count: int = 1
        for text in self.emoji_use_case.get_text().splitlines():
            image_font: ImageFont = find_best_font_and_box(
                self.emoji_use_case.get_split_size(),
                text,
                self.emoji_use_case.get_font(),
                self.emoji_use_case.get_base_size()
            )[0]
            image_draw.text(
                xy=(
                    self.emoji_use_case.get_center(),
                    (self.emoji_use_case.get_split_size() / 2) * count
                ),
                text=text,
                fill=self.emoji_use_case.get_font_color(),
                font=image_font,
                anchor="mm",
            )
            count += 2
        image.save(fp=self.emoji_use_case.get_save_file_path())



class AutoFontSizeChangeGeneratorImpl(ImageGenerator):
    def __init__(self, emoji_use_case: EmojiUseCase):
        self.emoji_use_case: EmojiUseCase = emoji_use_case

    def generate(self):
        resize: int = self.emoji_use_case.get_base_size()
        self.emoji_use_case.set_base_size(128 * 2)
        bounding_bottoms: List = []
        for text in self.emoji_use_case.get_text().splitlines():
            bounding_box = find_best_font_and_box(
                self.emoji_use_case.get_split_size(),
                text,
                self.emoji_use_case.get_font(),
                self.emoji_use_case.get_base_size()
            )[1]
            bounding_bottoms.append(bounding_box[BoundingBox.BOTTOM.value])
        image: Image = Image.new(
            mode="RGBA",
            size=(self.emoji_use_case.get_base_size(), sum(bounding_bottoms)),
            color=self.emoji_use_case.get_background_color()
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        for i, text in enumerate(self.emoji_use_case.get_text().splitlines(), start=1):
            image_font: Tuple[int, int, int, int] = find_best_font_and_box(
                self.emoji_use_case.get_split_size(),
                text,
                self.emoji_use_case.get_font(),
                self.emoji_use_case.get_base_size()
            )[0]
            image_draw.text(
                xy=(self.emoji_use_case.get_center(),
                    calc_y_axis(bounding_bottoms, i)),
                text=text,
                fill=self.emoji_use_case.get_font_color(),
                font=image_font,
                anchor="mm",
            )
        image: Image = image.resize((resize, resize))
        image.save(fp=self.emoji_use_case.get_save_file_path())
