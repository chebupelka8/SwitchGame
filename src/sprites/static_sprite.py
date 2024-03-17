import pygame

from typing import Optional

from ..shapes import CollisionRectangle
from ..scripts.math import Vec2
from ..image_types import Image
from ..config import AlignmentFlag


class StaticSprite(CollisionRectangle):
    def __init__(self, position: Vec2, image: Image) -> None:
        super().__init__(position, image.size.x, image.size.y)

        self.__image = image

    def draw(self, __display: pygame.Surface, image: Optional[Image] = None,
             alignment_flag=AlignmentFlag.TOPLEFT) -> None:
        self.update()

        if image is None:
            self.rectangle = alignment_flag(self.rectangle, self.__image)
            __display.blit(self.__image.image, self.rectangle)
        else:
            self.rectangle = alignment_flag(self.rectangle, image)
            __display.blit(image.image, self.rectangle)

    @property
    def image(self) -> Image:
        return self.__image

    @image.setter
    def image(self, __image: Image) -> None:
        self.__image = __image
        self.size = __image.size

    def __repr__(self) -> str:
        return f"StaticSprite(position={self.position}, image={self.__image})"
