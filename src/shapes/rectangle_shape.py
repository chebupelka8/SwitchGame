from ..scripts.math import Vec2, PrivateVec2

import pygame


class RectangleShape:
    def __init__(self, position: Vec2, width: int, height: int) -> None:
        self.__rectangle = pygame.Rect(position.x, position.y, width, height)
        self.__size = Vec2(width, height)

    @property
    def size(self) -> Vec2:
        return self.__size

    @size.setter
    def size(self, __size: Vec2) -> None:
        self.__size = __size
        self.__rectangle.size = __size.xy

    @property
    def rectangle(self) -> pygame.Rect:
        return self.__rectangle

    @rectangle.setter
    def rectangle(self, __rectangle: pygame.Rect) -> None:
        self.__rectangle = __rectangle

    @property
    def center(self) -> PrivateVec2:
        return PrivateVec2(self.__rectangle.centerx, self.__rectangle.centery)

    @property
    def position(self) -> PrivateVec2:
        return PrivateVec2(self.__rectangle.x, self.__rectangle.y)

    def draw_rect(self, __display: pygame.Surface, __color: str | tuple = "#ffffff", __width: int = 1) -> None:
        pygame.draw.rect(__display, __color, self.__rectangle, __width)
