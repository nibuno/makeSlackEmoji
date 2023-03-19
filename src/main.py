# -*- coding: utf-8 -*-
from typing import Tuple, Optional, List

from PIL import Image, ImageDraw, ImageFont
from calc_y_axis import calc_y_axis


class MakeSlackEmoji:
    def __init__(self, text: str):
        self.text: str = text
        self.file_stem: str = "_".join(self.text.splitlines())
        self.file_suffix: str = ".png"
        self.file_name: str = self.file_stem + self.file_suffix
        self.save_file_path: str = "save/" + self.file_name
        self.background_color: Tuple[int, int, int, int] = (0, 0, 0, 0)
        self.font_path: str = "../fonts/rounded-mplus-20150529/rounded-mplus-1c-black.ttf"
        self.font_color: str = "#000000"
        self.base_size: int = 128
        self.bounding_right_num: int = 2
        self.bounding_bottom_num: int = 3

    def create(self):
        image: Image = Image.new(
            mode="RGBA",
            size=(self.base_size, self.base_size),
            color=self.background_color
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        count: int = 1
        for text in self.text.splitlines():
            image_font: ImageFont = self._calc_font_size(
                self._get_split_size(),
                text
            )[0]
            image_draw.text(
                xy=(self._get_center(), (self._get_split_size() / 2) * count),
                text=text,
                fill=self.font_color,
                font=image_font,
                anchor="mm",
            )
            count += 2
        image.save(fp=self.save_file_path)

    def auto_font_size_change(self):
        resize: int = self.base_size
        self.base_size: int = 128 * 2
        bounding_bottoms: List = []
        for text in self.text.splitlines():
            bounding_box = self._calc_font_size(
                self.base_size,
                text
            )[1]
            bounding_bottoms.append(bounding_box[self.bounding_bottom_num])
        image: Image = Image.new(
            mode="RGBA",
            size=(self.base_size, sum(bounding_bottoms)),
            color=self.background_color
        )
        image_draw: ImageDraw = ImageDraw.Draw(im=image)
        for i, text in enumerate(self.text.splitlines(), start=1):
            image_font: Tuple[int, int, int, int] = self._calc_font_size(
                self.base_size,
                text
            )[0]
            image_draw.text(
                xy=(self._get_center(), calc_y_axis(bounding_bottoms, i)),
                text=text,
                fill=self.font_color,
                font=image_font,
                anchor="mm",
            )
        image: Image = image.resize((resize, resize))
        image.save(fp=self.save_file_path)

    def _calc_font_size(self, font_size: int, text: str):
        image_font: Optional[ImageFont] = None
        bounding_box: Optional[Tuple[int, int, int, int]] = None
        while (bounding_box is None) or \
                (bounding_box[self.bounding_right_num] > self.base_size) or \
                (bounding_box[self.bounding_bottom_num] > self.base_size) \
                and (font_size > 0):
            image_font = ImageFont.truetype(
                font=self.font_path,
                size=font_size
            )
            bounding_box = image_font.getbbox(text=text)
            font_size -= 1
        return image_font, bounding_box

    def _get_split_size(self) -> int:
        return int(
            self.base_size / len(self.text.splitlines())
        )

    def _get_center(self) -> float:
        return self.base_size / 2


    def judgment(self, auto_font_size_mode):
        # todo: 判定ロジックを修正したい
        if auto_font_size_mode:
            self.auto_font_size_change()
        else:
            self.create()


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
    auto_font_size = False
    for input_text in input_texts:
        make_slack_emoji = MakeSlackEmoji(input_text)
        make_slack_emoji.judgment(auto_font_size)
