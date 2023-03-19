from src.entity.emoji import Emoji
from src.find_best_font_and_box import find_best_font_and_box
from src.generator import StandardGeneratorImpl
from src.use_case.emoji_use_case import EmojiUseCase


class TestStandardGeneratorImpl:
    def test__calc_font_size(self):
        emoji = Emoji("弓")
        emoji_use_case = EmojiUseCase(emoji)
        generator = StandardGeneratorImpl(emoji, emoji_use_case)
        generator.emoji.base_size = 100
        assert find_best_font_and_box(
            generator.emoji_use_case.get_split_size(),
            generator.emoji.text,
            generator.emoji.font,
            generator.emoji.base_size
        )[1] == (0, 23, 84, 100)
