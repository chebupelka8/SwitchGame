import pygame

from .. import Image


class Alignment:

    @staticmethod
    def get_topleft(__rectangle: pygame.Rect, __image: Image) -> pygame.Rect:
        return __image.image.get_rect(topleft=__rectangle.topleft)

    @staticmethod
    def get_topright(__rectangle: pygame.Rect, __image: Image) -> pygame.Rect:
        return __image.image.get_rect(topright=__rectangle.topright)

    @staticmethod
    def get_center(__rectangle: pygame.Rect, __image: Image) -> pygame.Rect:
        return __image.image.get_rect(center=__rectangle.center)

    @staticmethod
    def get_bottomleft(__rectangle: pygame.Rect, __image: Image) -> pygame.Rect:
        return __image.image.get_rect(bottomleft=__rectangle.bottomleft)

    @staticmethod
    def get_bottomright(__rectangle: pygame.Rect, __image: Image) -> pygame.Rect:
        return __image.image.get_rect(bottomright=__rectangle.bottomright)


class AlignmentFlag:
    TOPLEFT = Alignment.get_topleft
    TOPRIGHT = Alignment.get_topright
    CENTER = Alignment.get_center
    BOTTOMLEFT = Alignment.get_bottomleft
    BOTTOMRIGHT = Alignment.get_bottomright
