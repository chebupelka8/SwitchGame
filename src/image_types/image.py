from typing import Any, Union

import pygame

from ..scripts.math import Vec2


class Image:
    def __init__(self, __arg: Union[str, pygame.Surface], should_convert: bool = True) -> None:
        self.__image = self.__load(__arg)
        if should_convert: self.__image = self.__image.convert_alpha()

    @classmethod
    def __load(cls, __arg: Union[str, pygame.Surface]) -> pygame.Surface:
        cls.__verify(__arg)

        return pygame.image.load(__arg) if isinstance(__arg, str) else __arg

    @staticmethod
    def __verify(__arg: Any) -> None:
        if not type(__arg) in (str, pygame.Surface):
            raise TypeError(f"Argument should be a string or a 'Surface', not {type(__arg)}")

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    @property
    def size(self) -> Vec2:
        return Vec2(*self.__image.get_size())

    @image.setter
    def image(self, image: pygame.Surface) -> None:
        self.__image = image

    def __repr__(self) -> str:
        return f"Image(size={self.image.get_size()}, alpha={self.image.get_alpha()})"