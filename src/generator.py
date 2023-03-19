# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from src.calc_y_axis import calc_y_axis
from src.entity.bounding_box import BoundingBox
from src.entity.emoji import Emoji
from src.find_best_font_and_box import find_best_font_and_box
from src.interface.image_generator import ImageGenerator
from src.use_case.emoji_use_case import EmojiUseCase
from typing import Tuple, List


class StandardGeneratorImpl(ImageGenerator):
    def __init__(self, text: str):
        self.emoji: Emoji = Emoji(text)
        self.emoji_use_case: EmojiUseCase = EmojiUseCase(self.emoji)

    def generate(self):
        image: Image = Image.new(
            mode="RGBA",
            size=(self.emoji.base_size, self.emoji.base_size),
            color=self.emoji.background_color
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        count: int = 1
        for text in self.emoji.text.splitlines():
            image_font: ImageFont = find_best_font_and_box(
                self.emoji_use_case.get_split_size(),
                text,
                self.emoji.font,
                self.emoji.base_size
            )[0]
            image_draw.text(
                xy=(
                    self.emoji_use_case.get_center(),
                    (self.emoji_use_case.get_split_size() / 2) * count
                ),
                text=text,
                fill=self.emoji.font_color,
                font=image_font,
                anchor="mm",
            )
            count += 2
        image.save(fp=self.emoji_use_case.get_save_file_path())



class AutoFontSizeChangeGeneratorImpl(ImageGenerator):
    def __init__(self, text: str):
        self.emoji: Emoji = Emoji(text)
        self.emoji_use_case: EmojiUseCase = EmojiUseCase(self.emoji)

    def generate(self):
        resize: int = self.emoji.base_size
        self.emoji.base_size = 128 * 2
        bounding_bottoms: List = []
        for text in self.emoji.text.splitlines():
            bounding_box = find_best_font_and_box(
                self.emoji_use_case.get_split_size(),
                text,
                self.emoji.font,
                self.emoji.base_size
            )[1]
            bounding_bottoms.append(bounding_box[BoundingBox.BOTTOM.value])
        image: Image = Image.new(
            mode="RGBA",
            size=(self.emoji.base_size, sum(bounding_bottoms)),
            color=self.emoji.background_color
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        for i, text in enumerate(self.emoji.text.splitlines(), start=1):
            image_font: Tuple[int, int, int, int] = find_best_font_and_box(
                self.emoji_use_case.get_split_size(),
                text,
                self.emoji.font,
                self.emoji.base_size
            )[0]
            image_draw.text(
                xy=(self.emoji_use_case.get_center(),
                    calc_y_axis(bounding_bottoms, i)),
                text=text,
                fill=self.emoji.font_color,
                font=image_font,
                anchor="mm",
            )
        image: Image = image.resize((resize, resize))
        image.save(fp=self.emoji_use_case.get_save_file_path())
