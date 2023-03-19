# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Tuple


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
        project_root = Path(__file__).parent.parent.parent
        self.font: str = str(project_root / font)
        self.font_color: str = font_color
        self.base_size: int = base_size
