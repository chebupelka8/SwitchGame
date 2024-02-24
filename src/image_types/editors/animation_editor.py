from .image_editor import ImageEditor
from ..animation import Animation


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
