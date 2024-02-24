from ..scripts.math import Vec2

from ..image_types import Image, Animation, ImageEditor


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
