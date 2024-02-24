# import pygame
# from .math import Vec2, PrivateVec2
# from .collision import Collider
# from typing import TYPE_CHECKING

import SwitchGame as sw

# from .collision import Collider
from .math import Vec2, PrivateVec2

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
    
    @property
    def center(self) -> PrivateVec2:
        return PrivateVec2(self.__rectangle.centerx, self.__rectangle.centery)
    
    @property
    def position(self) -> PrivateVec2:
        return PrivateVec2(self.__rectangle.x, self.__rectangle.y)

    def draw_rect(self, __display: pygame.Surface, __color: str | tuple = "#ffffff", __width: int = 0) -> None:
        pygame.draw.rect(__display, __color, self.__rectangle, __width)


class CollisionRectangle(RectangleShape):
    def __init__(self, position: Vec2, width: int, height: int, *, movement: Vec2 = Vec2(0, 0)) -> None:
        super().__init__(position, width, height)

        self.__movement = movement
        self.__collide_groups = None
        self.__object_groups = None
        self.__collide_side = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False
        }
    
    @property
    def movement(self) -> Vec2:
        return self.__movement

    @movement.setter
    def movement(self, __movement: Vec2) -> None:
        self.__movement = __movement
    
    def set_collision_groups(self, *__groups) -> None:
        self.__collide_groups = [*__groups]

    def set_object_groups(self, *__groups) -> None:
        self.__object_groups = [*__groups]
    
    def get_collision_side(self, __side: str) -> bool:
        return self.__collide_side.get(__side)

    def __repr__(self) -> str:
        return f"""CollisionRectangle(
        position={self.position}, movement={self.movement}, collisions={self.__collide_side})"""
    
    def update(self) -> None:
        # horizontal
        self.rectangle.x += self.movement.x
        
        if self.__collide_groups is not None:
            collisions = sw.Collider.group_collider(self, *self.__collide_groups)

            for sprite in collisions:
                if self.movement.x > 0:
                    self.rectangle.right = sprite.rectangle.left
                    self.__collide_side["right"] = True
                if self.movement.x < 0:
                    self.rectangle.left = sprite.rectangle.right
                    self.__collide_side["left"] = True
            
            if len(collisions) == 0:
                self.__collide_side["right"] = self.__collide_side["left"] = False

        # if self.__object_groups is not None:
        #     collisions = sw.Collider.group_collider(self, *self.__object_groups)
        #
        #     for sprite in collisions:
        #         print(sprite)
        #         if sprite.movement.x > 0:
        #             sprite.rectangle.right = self.rectangle.left
        #             sprite.__collide_side["right"] = True
        #         if sprite.movement.x < 0:
        #             sprite.rectangle.left = self.rectangle.right
        #             sprite.__collide_side["left"] = True

            # if len(collisions) == 0:

        
        # vertical
        self.rectangle.y += self.movement.y

        if self.__collide_groups is not None:
            collisions = sw.Collider.group_collider(self, *self.__collide_groups)

            for sprite in collisions:
                if self.movement.y > 0:
                    self.rectangle.bottom = sprite.rectangle.top
                    self.__collide_side["bottom"] = True
                if self.movement.y < 0:
                    self.rectangle.top = sprite.rectangle.bottom
                    self.__collide_side["top"] = True

            if len(collisions) == 0:
                self.__collide_side["top"] = self.__collide_side["bottom"] = False