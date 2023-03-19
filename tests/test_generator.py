from src.generator import StandardGeneratorImpl


class TestStandardGeneratorImpl:
    def test__calc_font_size(self):
        generator = StandardGeneratorImpl("弓")
        generator.emoji.base_size = 100
        assert generator._calc_font_size(
            generator.emoji_use_case.get_split_size(),
            generator.emoji.text,
            generator.emoji.font,
            generator.emoji.base_size
        )[1] == (0, 23, 84, 100)
