from typing import Any

import pygame

from ..image import Image


class ImageEditor:

    @staticmethod
    def __verify_image(__image: Any) -> None:
        if not isinstance(__image, Image): raise TypeError("Argument should be an instance of the 'Image' class")

    @classmethod
    def rotate(cls, __image: Image, degrees: int) -> Image:
        cls.__verify_image(__image)

        return Image(pygame.transform.rotate(__image.image, degrees))

    @classmethod
    def resize(cls, __image: Image, width: int, height: int) -> Image:
        cls.__verify_image(__image)

        return Image(pygame.transform.scale(__image.image, (width, height)))

    @classmethod
    def mult_size(cls, __image: Image, mult_width: int | float, mult_height: int | float) -> Image:
        cls.__verify_image(__image)

        return Image(pygame.transform.scale(__image.image, (__image.size.x * mult_width, __image.size.y * mult_height)))

    @classmethod
    def set_alpha(cls, __image: Image, alpha: int) -> Image:
        cls.__verify_image(__image)

        __image.image.set_alpha(alpha)
        return Image(__image.image)

    @classmethod
    def flip(cls, __image: Image, side: str) -> Image:
        cls.__verify_image(__image)

        match side:
            case "horizontal":
                return Image(pygame.transform.flip(__image.image, True, False))
            case "vertical":
                return Image(pygame.transform.flip(__image.image, False, True))
            case _:
                raise ValueError("Argument should be the string 'vertical' or 'horizontal'")

    @classmethod
    def cut(cls, __image: Image, x: int | float, y: int | float, width: int, height: int) -> Image:
        cls.__verify_image(__image)

        return Image(__image.image.subsurface(x, y, width, height))

    @classmethod
    def blur(cls, __image: Image, radius: int) -> Image:
        cls.__verify_image(__image)

        return Image(pygame.transform.gaussian_blur(__image.image, radius))
