# -*- coding: utf-8 -*-
from src.entity.emoji import Emoji


class EmojiUseCase:
    def __init__(self, emoji: Emoji):
        self.emoji = emoji

    def get_save_file_path(self) -> str:
        file_stem: str = "_".join(self.emoji.text.splitlines())
        file_name: str = file_stem + self.emoji.file_extension
        save_file_path: str = "save/" + file_name
        return save_file_path


    def get_split_size(self) -> int:
        return int(
            self.emoji.base_size / len(self.emoji.text.splitlines())
        )


    def get_center(self) -> float:
        return self.emoji.base_size / 2
