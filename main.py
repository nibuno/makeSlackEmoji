# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


class MakeSlackEmoji:
    def __init__(self, text):
        self.text = text
        self.file_stem = "_".join(self.text.splitlines())
        self.file_suffix = ".png"
        self.file_name = self.file_stem + self.file_suffix
        self.background_color = (0, 0, 0, 0)
        self.font_path = "rounded-mplus-20150529/rounded-mplus-1c-black.ttf"
        self.base_size = 128

    def main(self, font_color="#000000"):
        image = Image.new(
            mode="RGBA",
            size=(self.base_size, self.base_size),
            color=self.background_color
        )
        image_draw = ImageDraw.Draw(im=image)
        count = 1
        right = 2
        bottom = 3
        for text in self.text.splitlines():
            image_font = self._calc_font_size(
                self.base_size,
                self._get_split_size(),
                right,
                bottom,
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
        self.base_size = 128 * 2
        right = 2
        bottom = 3
        bounding_bottoms = []
        for text in self.text.splitlines():
            bounding_box = self._calc_font_size(
                self.base_size,
                self.base_size,
                right,
                bottom,
                text
            )[1]
            bounding_bottoms.append(bounding_box[bottom])
        image = Image.new(
            mode="RGBA",
            size=(self.base_size, sum(bounding_bottoms)),
            color=self.background_color
        )
        image_draw = ImageDraw.Draw(im=image)
        for i, text in enumerate(self.text.splitlines(), start=1):
            image_font = self._calc_font_size(
                self.base_size,
                self.base_size,
                right,
                bottom,
                text
            )[0]
            image_draw.text(
                xy=(self._get_center(), self._calc_y_axis(bounding_bottoms, i)),
                text=text,
                fill=font_color,
                font=image_font,
                anchor="mm",
            )
        image = image.resize((self.base_size, self.base_size))
        image.save(fp=self.file_name)


    def _calc_font_size(
            self,
            base_size,
            font_size,
            right,
            bottom,
            text):
        bounding_box = None
        while (bounding_box is None) or \
                (bounding_box[right] > base_size) or \
                (bounding_box[bottom] > base_size) \
                and (font_size > 0):
            image_font = ImageFont.truetype(
                font=self.font_path,
                size=font_size
            )
            bounding_box = image_font.getbbox(text=text)
            font_size -= 1
        return image_font, bounding_box


    def _calc_y_axis(self, bounding_boxs, count):
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
    for input_text in input_texts:
        # main(input_text)
        make_slack_emoji = MakeSlackEmoji(input_text)
        make_slack_emoji.main()
        make_slack_emoji.auto_font_size_change()
