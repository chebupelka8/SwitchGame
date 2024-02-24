# import pygame
# from typing import Any
# import os
# from .exceptions import ImageLoadError
# from .math import Vec2

# from . import Vec2, ImageLoadError
from typing import Any
import pygame
import os

# import SwitchGame as sw
from .math import Vec2
from .exceptions import ImageLoadError


class Image:
    def __init__(self, __arg: str | pygame.Surface, should_convert: bool = True) -> None:
        self.__image = self.__load(__arg)
        if should_convert: self.__image = self.__image.convert_alpha()
    
    @classmethod
    def __load(cls, __arg: str | pygame.Surface) -> pygame.Surface:
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


class Animation:
    def __init__(self, __dir: str | list[str] | list[pygame.Surface] | list[Image]) -> None:
        self.__directory = self.__load(__dir)
    
    @classmethod
    def __load(cls, __dir: str | list[str] | list[pygame.Surface] | list[Image]) -> list[pygame.Surface]:
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
    def directory(self, __dir: str | list[str] | list[pygame.Surface] | list[Image]) -> None:
        self.__directory = self.__load(__dir)
    
    def count(self) -> int:
        return len(self.directory)
    
    def __repr__(self) -> str:
        return f"Animation(images={self.directory})"
    
    def __len__(self) -> int:
        return len(self.directory)
    
    def __getitem__(self, __index):
        return self.directory[__index]


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


class AnimationEditor:

    @staticmethod
    def __verify_animation(__animation) -> None:
        if not isinstance(__animation, Animation):
            raise TypeError("Argument should be an instance of the 'Animation' class")

    @classmethod
    def rotate(cls, __animation: Animation, degrees: int) -> Animation:
        cls.__verify_animation(__animation)

        return Animation(list(map(lambda i: ImageEditor.rotate(i, degrees), __animation.directory)))
    
    @classmethod
    def resize(cls, __animation: Animation, width: int, height: int) -> Animation:
        cls.__verify_animation(__animation)

        return Animation(list(map(lambda i: ImageEditor.resize(i, width, height), __animation.directory)))
    
    @classmethod
    def mult_size(cls, __animation: Animation, mult_width: int | float, mult_height: int | float) -> Animation:
        cls.__verify_animation(__animation)

        return Animation(list(map(lambda i: ImageEditor.mult_size(i, mult_width, mult_height), __animation.directory)))
    
    @classmethod
    def set_alpha(cls, __animation: Animation, alpha: int) -> Animation:
        cls.__verify_animation(__animation)

        return Animation(list(map(lambda i: ImageEditor.set_alpha(i, alpha), __animation.directory)))

    @classmethod
    def flip(cls, __animation: Animation, side: str) -> Animation:
        cls.__verify_animation(__animation)

        return Animation(list(map(lambda i: ImageEditor.flip(i, side), __animation.directory)))
    
    @classmethod
    def cut(cls, __animation: Animation, x: int | float, y: int | float, width: int, height: int) -> Animation:
        cls.__verify_animation(__animation)

        return Animation(list(map(lambda i: ImageEditor.cut(i, x, y, width, height), __animation.directory)))


class Tileset:

    @staticmethod
    def split_by_size(__image: Image, tile_size: Vec2) -> Animation:
        width, height = __image.size
        count = Vec2(width // tile_size.x, height // tile_size.y)

        res = []

        for y in range(count.y):
            for x in range(count.x):
                res.append(
                    ImageEditor.cut(__image, x * tile_size.x, y * tile_size.y, tile_size.x, tile_size.y)
                )
        
        return Animation(res)

    @staticmethod
    def split_by_count(__image: Image, count: Vec2) -> Animation:
        tile_size = Vec2(__image.size.x // count.x, __image.size.y // count.y)

        res = []

        for y in range(count.y):
            for x in range(count.x):
                res.append(
                    ImageEditor.cut(__image, x * tile_size.x, y * tile_size.y, tile_size.x, tile_size.y)
                )
        
        return Animation(res)

    