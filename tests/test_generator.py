from src.entity.emoji import Emoji
from src.find_best_font_and_box import find_best_font_and_box
from src.generator import StandardGeneratorImpl
from src.use_case.emoji_use_case import EmojiUseCase


class TestStandardGeneratorImpl:
    def test_find_best_font_and_box(self):
        emoji = Emoji("弓")
        emoji_use_case = EmojiUseCase(emoji)
        generator = StandardGeneratorImpl(emoji_use_case)
        generator.emoji_use_case.set_base_size(100)
        assert find_best_font_and_box(
            generator.emoji_use_case.get_split_size(),
            generator.emoji_use_case.get_text(),
            generator.emoji_use_case.get_font(),
            generator.emoji_use_case.get_base_size()
        )[1] == (0, 23, 84, 100)
