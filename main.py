# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from calc_y_axis import calc_y_axis


class MakeSlackEmoji:
    def __init__(self, text):
        self.text = text
        self.file_stem = "_".join(self.text.splitlines())
        self.file_suffix = ".png"
        self.file_name = self.file_stem + self.file_suffix
        self.background_color = (0, 0, 0, 0)
        self.font_path = "rounded-mplus-20150529/rounded-mplus-1c-black.ttf"
        self.base_size = 128
        self.bounding_right_num = 2
        self.bounding_bottom_num = 3

    def judgment(self, auto_font_size_mode):
        # todo: 判定ロジックを修正したい
        if auto_font_size_mode:
            self.auto_font_size_change()
        else:
            self.main()

    def main(self, font_color="#000000"):
        image = Image.new(
            mode="RGBA",
            size=(self.base_size, self.base_size),
            color=self.background_color
        )
        image_draw = ImageDraw.Draw(im=image)
        count = 1
        for text in self.text.splitlines():
            image_font = self._calc_font_size(
                self._get_split_size(),
                text
            )[0]
            image_draw.text(
                xy=(self._get_center(), (self._get_split_size() / 2) * count),
                text=text,
                fill=font_color,
                font=image_font,
                anchor="mm",
            )
            count += 2
        image.save(fp=self.file_name)

    def auto_font_size_change(self, font_color="#000000"):
        resize = self.base_size
        self.base_size = 128 * 2
        bounding_bottoms = []
        for text in self.text.splitlines():
            bounding_box = self._calc_font_size(
                self.base_size,
                text
            )[1]
            bounding_bottoms.append(bounding_box[self.bounding_bottom_num])
        image = Image.new(
            mode="RGBA",
            size=(self.base_size, sum(bounding_bottoms)),
            color=self.background_color
        )
        image_draw = ImageDraw.Draw(im=image)
        for i, text in enumerate(self.text.splitlines(), start=1):
            image_font = self._calc_font_size(
                self.base_size,
                text
            )[0]
            image_draw.text(
                xy=(self._get_center(), calc_y_axis(bounding_bottoms, i)),
                text=text,
                fill=font_color,
                font=image_font,
                anchor="mm",
            )
        image = image.resize((resize, resize))
        image.save(fp=self.file_name)


    def _calc_font_size(
            self,
            font_size,
            text):
        image_font = None
        bounding_box = None
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

    def _get_split_size(self):
        return int(
            self.base_size / len(self.text.splitlines())
        )

    def _get_center(self):
        return self.base_size / 2


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
