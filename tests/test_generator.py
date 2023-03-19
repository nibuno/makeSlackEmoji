from src.generator import StandardGeneratorImpl
from src.find_best_font_and_box import find_best_font_and_box


class TestStandardGeneratorImpl:
    def test__calc_font_size(self):
        generator = StandardGeneratorImpl("弓")
        generator.emoji.base_size = 100
        assert find_best_font_and_box(
            generator.emoji_use_case.get_split_size(),
            generator.emoji.text,
            generator.emoji.font,
            generator.emoji.base_size
        )[1] == (0, 23, 84, 100)
