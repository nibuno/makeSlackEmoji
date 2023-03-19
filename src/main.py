# -*- coding: utf-8 -*-
from src.generator import AutoFontSizeChangeGeneratorImpl, StandardGeneratorImpl


def main(input_text: str, auto_font_size: bool):
    if auto_font_size:
        generator = AutoFontSizeChangeGeneratorImpl(input_text)
    else:
        generator = StandardGeneratorImpl(input_text)
    generator.generate()


if __name__ == '__main__':
    main("hello world", False)
