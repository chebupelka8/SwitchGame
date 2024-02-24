from typing import Any

from ..shapes import RectangleShape, CollisionRectangle
from ..sprites import StaticSprite, AnimatedSprite

import pygame


class _Group:
    def __init__(self, *__items: Any) -> None:
        self.items = [*__items]

    def add(self, __item: Any) -> None:
        self.items.append(__item)

    def delete(self, __item: Any) -> None:
        self.items.remove(__item)

    def clear(self) -> None:
        self.items.clear()

    def __getitem__(self, __index: int) -> Any:
        return self.items[__index]

    def get(self) -> list[Any]:
        return self.items


class RectangleGroup(_Group):
    def __init__(self, *__rects: pygame.Rect | RectangleShape | CollisionRectangle) -> None:
        super().__init__(*__rects)

        self.items = self.__to_rectangle_items(self.items)

        map(self.__verify, self.items)

    @staticmethod
    def __verify(__rect) -> None:
        match __rect:
            case rect if not isinstance(rect, pygame.Rect):
                raise TypeError("Argument should be 'pygame.Rect'")

    @classmethod
    def __to_rectangle_items(cls, __items: list) -> list[pygame.Rect]:
        res = []

        for item in __items:
            res.append(cls.__to_rectangle(item))

        return res

    @staticmethod
    def __to_rectangle(__item: pygame.Rect | CollisionRectangle | RectangleShape) -> pygame.Rect:
        match __item:
            case item if isinstance(item, pygame.Rect):
                return item

            case item if isinstance(item, (RectangleShape, CollisionRectangle)):
                return item.rectangle

    def add(self, __item: Any) -> None:
        super().add(self.__to_rectangle(__item))

    def __repr__(self) -> str:
        return f"RectangleGroup(sprites={self.items})"


class SpriteGroup(_Group):
    def __init__(self, *__sprites: StaticSprite | AnimatedSprite) -> None:
        super().__init__(*__sprites)

        map(self.__verify, [*__sprites])

    @staticmethod
    def __verify(__sprite) -> None:
        match __sprite:
            case sprite if isinstance(sprite, (StaticSprite, AnimatedSprite)):
                ...
            case _:
                raise TypeError("Argument should be 'StaticSprite' or 'AnimatedSprite'")

    def to_rectangle_group(self) -> RectangleGroup:
        return RectangleGroup(*[sprite.rectangle for sprite in self.items])

    def __repr__(self) -> str:
        return f"SpriteGroup(sprites={self.items})"
