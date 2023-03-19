# -*- coding: utf-8 -*-
from src.generator import AutoFontSizeChangeGeneratorImpl, StandardGeneratorImpl
from src.entity.emoji import Emoji
from src.use_case.emoji_use_case import EmojiUseCase


def main(input_text: str, auto_font_size: bool):
    emoji = Emoji(input_text)
    emoji_use_case = EmojiUseCase(emoji)
    if auto_font_size:
        generator = AutoFontSizeChangeGeneratorImpl(emoji_use_case)
    else:
        generator = StandardGeneratorImpl(emoji_use_case)
    generator.generate()


if __name__ == '__main__':
    main("hello world", False)
