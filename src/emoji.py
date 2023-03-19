# -*- coding: utf-8 -*-
from typing import Tuple
from pathlib import Path


class Emoji:
    def __init__(
            self,
            text: str,
            extension: str = ".png",
            background_color: Tuple[int, int, int, int] = (0, 0, 0, 0),
            font: str = "fonts/rounded-mplus-20150529/rounded-mplus-1c-black.ttf",
            font_color: str = "#000000",
            base_size: int = 128
    ):
        self.text: str = text
        self.file_extension: str = extension

        self.background_color: Tuple[int, int, int, int] = background_color
        project_root = Path(__file__).resolve().parents[1]
        self.font: str = str(project_root / font)
        self.font_color: str = font_color
        self.base_size: int = base_size

    def get_save_file_path(self) -> str:
        file_stem: str = "_".join(self.text.splitlines())
        file_name: str = file_stem + self.file_extension
        save_file_path: str = "save/" + file_name
        return save_file_path

    def get_split_size(self) -> int:
        return int(
            self.base_size / len(self.text.splitlines())
        )

    def get_center(self) -> float:
        return self.base_size / 2
