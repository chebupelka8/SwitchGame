from typing import Any, Union

import pygame
import os

from ..scripts.exceptions import ImageLoadError
from .image import Image


class Animation:
    def __init__(self, __dir: Union[str, list[str], list[pygame.Surface], list[Image]]) -> None:
        self.__directory = self.__load(__dir)

    @classmethod
    def __load(cls, __dir: Union[str, list[str], list[pygame.Surface], list[Image]]) -> list[pygame.Surface]:
        cls.__verify(__dir)

        if isinstance(__dir, str):
            return [Image(f"{__dir}/{p}").image for p in os.listdir(__dir)]
        elif all(map(lambda obj: isinstance(obj, str), __dir)):
            return [Image(p).image for p in __dir]
        elif all(map(lambda obj: isinstance(obj, pygame.Surface), __dir)):
            return __dir
        elif all(map(lambda obj: isinstance(obj, Image), __dir)):
            return [p.image for p in __dir]
        else:
            raise ImageLoadError("Something went wrong when uploading the image")

    @staticmethod
    def __verify(__arg: Any) -> None:
        try:
            match __arg:
                case arg if isinstance(arg, str):
                    ...
                case arg if all(map(lambda i: isinstance(i, str), arg)):
                    ...
                case arg if all(map(lambda i: isinstance(i, pygame.Surface), arg)):
                    ...
                case arg if all(map(lambda i: isinstance(i, Image), arg)):
                    ...
                case _:
                    raise TypeError(
                        """Argument should be a string, a list of strings 
                        or a list of 'Surfaces' or a list of instances of the 'Image' class"""
                    )

        except TypeError:
            raise TypeError(
                """Argument should be a string, a list of strings 
                or a list of 'Surfaces' or a list of instances of the 'Image' class"""
            )

    @property
    def directory(self) -> list[Image]:
        return list(map(Image, self.__directory))

    @directory.setter
    def directory(self, __dir: Union[str, list[str], list[pygame.Surface], list[Image]]) -> None:
        self.__directory = self.__load(__dir)

    def count(self) -> int:
        return len(self.directory)

    def __repr__(self) -> str:
        return f"Animation(images={self.directory})"

    def __len__(self) -> int:
        return len(self.directory)

    def __getitem__(self, __index):
        return self.directory[__index]
