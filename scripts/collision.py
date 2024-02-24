from .group import SpriteGroup, RectangleGroup
from .shape import CollisionRectangle
from .math import Vec2

import pygame


class Collider:
    
    @classmethod
    def group_collider(cls, __sprite, *__groups: SpriteGroup | RectangleGroup) -> list[CollisionRectangle]:
        collisions = []

        for group in __groups:
            for sprite in group.get():
                if isinstance(group, SpriteGroup):
                    if cls.__collide_rect(__sprite.rectangle, sprite.rectangle):
                        collisions.append(
                            CollisionRectangle(
                                Vec2(*sprite.position.xy),
                                sprite.rectangle.width,
                                sprite.rectangle.height
                            )
                        )

                if isinstance(group, RectangleGroup):
                    if cls.__collide_rect(__sprite.rectangle, sprite):
                        collisions.append(
                            CollisionRectangle(
                                Vec2(sprite.x, sprite.y), sprite.width, sprite.height
                            )
                        )
        
        return collisions
    
    @classmethod
    def __collide_rect(cls, __rect_0: pygame.Rect, __rect_1: pygame.Rect) -> bool:
        return __rect_0.colliderect(__rect_1)