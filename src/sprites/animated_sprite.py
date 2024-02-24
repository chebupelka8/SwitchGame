import pygame

from ..scripts.shape import CollisionRectangle
from ..scripts.math import Vec2
from ..scripts.image import Animation


class AnimatedSprite(CollisionRectangle):
    def __init__(self, position: Vec2, animation: Animation) -> None:
        super().__init__(position, animation[0].size.x, animation[0].size.y)

        self.__verify(animation)

        self.__animation: Animation = animation
        self.__frame = 0
        self.__is_freezed: bool = False

    @staticmethod
    def __verify(__animation) -> None:
        if not isinstance(__animation, Animation):
            raise TypeError("Argument should be an instanse of the 'Animtion' class")

    def draw(self, __display: pygame.Surface) -> None:
        self.rectangle.size = self.__animation[int(self.__frame)].size.xy
        self.update()

        __display.blit(self.__animation[int(self.__frame)].image, self.rectangle)

    def animating(self, __speed: int | float) -> None:
        if not self.__is_freezed:
            self.__frame += __speed
            if self.__frame >= self.__animation.count(): self.__frame = 0

    @property
    def animation(self) -> Animation:
        return self.__animation

    @animation.setter
    def animation(self, __animation: Animation) -> None:
        self.__animation = __animation

    def freeze(self) -> None:
        self.__is_freezed = True

    def unfreeze(self) -> None:
        self.__is_freezed = False

    def __repr__(self) -> str:
        return f"AnimatedSprite(position={self.position}, animation={self.__animation}, frame={int(self.__frame)})"
